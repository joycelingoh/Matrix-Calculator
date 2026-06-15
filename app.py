from flask import Flask, render_template, request, jsonify
import numpy as np
from scipy.linalg import lu
from numpy.linalg import svd, eig

app = Flask(__name__)

def check_diagonalizability(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    unique_eigenvalues = np.unique(eigenvalues)
    for eigenvalue in unique_eigenvalues:
        am = np.count_nonzero(np.isclose(eigenvalues, eigenvalue))
        gm = np.linalg.matrix_rank(matrix - eigenvalue * np.eye(matrix.shape[0]))
        gm = matrix.shape[0] - gm
        if am != gm:
            return False, eigenvalues, eigenvectors
    return True, eigenvalues, eigenvectors

def lu_decomposition(matrix):
    n = matrix.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):
        # Upper Triangular
        for j in range(i, n):
            U[i][j] = matrix[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        
        # Lower Triangular
        for j in range(i, n):
            if i == j:
                L[i][i] = 1  # Diagonal as 1
            else:
                L[j][i] = (matrix[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    return L, U

def singular_value_decomposition(matrix):
    U, S, VT = svd(matrix)
    return U, S, VT

def power_method(matrix, tol=1e-6, max_iter=100):
    n = len(matrix)
    vector = np.ones(n)

    eigenvalue = 0
    for i in range(max_iter):  
        new_vector = np.dot(matrix, vector)
        new_vector_norm = np.linalg.norm(new_vector)
        new_vector = new_vector / new_vector_norm  # Normalize the new vector
        new_eigenvalue = np.dot(new_vector, np.dot(matrix, new_vector)) / np.dot(new_vector, new_vector)
        if abs(new_eigenvalue - eigenvalue) < tol:
            break
        eigenvalue = new_eigenvalue
        vector = new_vector

    return eigenvalue, vector

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            data = request.get_json()
            if not data:
                return jsonify({"error": "No data received"}), 400

            matrix_data = data.get('matrix')
            rows = data.get('rows')
            cols = data.get('cols')
            operation = data.get('operation')

            if not all([matrix_data, rows, cols, operation]):
                return jsonify({"error": "Missing required data"}), 400

            matrix = np.array(matrix_data).reshape(rows, cols).astype(float)
            result = None

            if operation in ["diagonalization", "lu_decomposition", "power_method"] and rows != cols:
                return jsonify({"error": "Matrix must be square for this operation"}), 400

            if operation == "diagonalization":
                is_diagonalizable, eigenvalues, eigenvectors = check_diagonalizability(matrix)
                result = {
                    "operation": "diagonalization",
                    "is_diagonalizable": bool(is_diagonalizable),
                    "eigenvalues": eigenvalues.tolist(),
                    "eigenvectors": eigenvectors.tolist(),
                    "input_matrix": matrix.tolist()
                }

            elif operation == "lu_decomposition":
                L, U = lu_decomposition(matrix)
                result = {
                    "operation": "lu_decomposition",
                    "input_matrix": matrix.tolist(),
                    "L": L.tolist(),
                    "U": U.tolist()
                }

            elif operation == "svd":
                U, S, VT = singular_value_decomposition(matrix)
                result = {
                    "operation": "svd",
                    "input_matrix": matrix.tolist(),
                    "U": U.tolist(),
                    "S": S.tolist(),
                    "VT": VT.tolist()
                }

            elif operation == "power_method":
                eigenvalue, eigenvector = power_method(matrix)
                result = {
                    "operation": "power_method",
                    "input_matrix": matrix.tolist(),
                    "eigenvalue": float(eigenvalue),
                    "eigenvector": eigenvector.tolist()
                }

            else:
                return jsonify({"error": f"Unknown operation: {operation}"}), 400

            if result is not None:
                return jsonify(result)
            else:
                return jsonify({"error": "Operation failed"}), 400

        except Exception as e:
            return jsonify({"error": str(e)}), 400

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
