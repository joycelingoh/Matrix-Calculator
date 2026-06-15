# Matrix Calculator

A web-based Matrix Calculator developed using Flask, NumPy, and SciPy. This application allows users to perform various matrix operations, including diagonalization analysis, LU decomposition, Singular Value Decomposition (SVD), and the Power Method for dominant eigenvalue computation.

## Live Demo

https://joycelingoh.pythonanywhere.com/

## Features

- Matrix input with customizable dimensions
- Diagonalization check
  - Eigenvalue computation
  - Eigenvector computation
  - Diagonalizability verification
- LU Decomposition
- Singular Value Decomposition (SVD)
- Power Method for dominant eigenvalue approximation

## Technologies Used

### Backend
- Python
- Flask
- NumPy
- SciPy

### Frontend
- HTML
- CSS
- JavaScript

## Project Structure

```text
matrix-calculator/
│
├── app.py
├── requirements.txt
│
└── templates/
    └── index.html
```

## Mathematical Operations

### 1. Diagonalization
Determines whether a matrix is diagonalizable by comparing the algebraic multiplicity and geometric multiplicity of each eigenvalue.

### 2. LU Decomposition
Decomposes a square matrix A into:

A = LU

where:
- L = Lower triangular matrix
- U = Upper triangular matrix

### 3. Singular Value Decomposition (SVD)
Factorizes a matrix into:

A = UΣVᵀ

where:
- U = Left singular vectors
- Σ = Singular values
- Vᵀ = Right singular vectors

### 4. Power Method
Iteratively approximates:
- Dominant eigenvalue
- Corresponding eigenvector

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/matrix-calculator.git
cd matrix-calculator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app.py
```

Open:

```text
http://127.0.0.1:5000
```

## Example Use Cases

- Linear Algebra learning
- Matrix decomposition demonstrations
- Educational purposes
- Numerical computation practice
- Eigenvalue and eigenvector analysis

## Future Improvements

- Matrix determinant calculation
- Matrix inverse computation
- QR decomposition
- Matrix visualization
- Export results to PDF
- Step-by-step calculation display
- Matrix history tracking

## Author

- Ann Abigail Halim
- Hania Nayma Zahra
- Joycelin
- Richelle Marvela
