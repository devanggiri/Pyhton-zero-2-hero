import numpy as np

# Create a matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original matrix:\n", matrix)

# Access an element
element = matrix[1, 2]
print("\nElement at (1, 2):", element)

# Access a row
row = matrix[1, :]
print("\nRow 1:", row)

# Access a column
column = matrix[:, 1]
print("\nColumn 1:", column)

# Add a scalar
added_scalar = matrix + 10
print("\nMatrix + 10:\n", added_scalar)

# Multiply by a scalar
multiplied_scalar = matrix * 2
print("\nMatrix * 2:\n", multiplied_scalar)

# Element-wise addition
matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
elementwise_add = matrix + matrix2
print("\nElement-wise addition:\n", elementwise_add)

# Element-wise multiplication
elementwise_mult = matrix * matrix2
print("\nElement-wise multiplication:\n", elementwise_mult)

# Matrix multiplication
matrix_mult = np.dot(matrix, matrix2)
print("\nMatrix multiplication:\n", matrix_mult)

# Transpose
transpose = matrix.T
print("\nTranspose:\n", transpose)

# Determinant
determinant = np.linalg.det(matrix)
print("\nDeterminant:", determinant)

# Inverse (Note: matrix must be square and non-singular)
matrix_square = np.array([[1, 2], [3, 4]])
inverse = np.linalg.inv(matrix_square)
print("\nInverse:\n", inverse)

# Eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix_square)
print("\nEigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Sum of all elements
sum_all = matrix.sum()
print("\nSum of all elements:", sum_all)

# Sum along an axis
sum_axis0 = matrix.sum(axis=0)
sum_axis1 = matrix.sum(axis=1)
print("\nSum along axis 0:", sum_axis0)
print("Sum along axis 1:", sum_axis1)

# Mean of all elements
mean_all = matrix.mean()
print("\nMean of all elements:", mean_all)

# Mean along an axis
mean_axis0 = matrix.mean(axis=0)
mean_axis1 = matrix.mean(axis=1)
print("\nMean along axis 0:", mean_axis0)
print("Mean along axis 1:", mean_axis1)

# Reshape the matrix
reshaped_matrix = matrix.reshape(1, 9)
print("\nReshaped matrix (1x9):\n", reshaped_matrix)

# Flatten the matrix
flattened = matrix.flatten()
print("\nFlattened matrix:", flattened)

# Stack matrices vertically
vertical_stack = np.vstack((matrix, matrix2))
print("\nVertical stack:\n", vertical_stack)

# Stack matrices horizontally
horizontal_stack = np.hstack((matrix, matrix2))
print("\nHorizontal stack:\n", horizontal_stack)

# Split the matrix
split_matrices = np.hsplit(matrix, 3)
print("\nSplit matrix into 3 parts:\n", split_matrices)

# Create a zero matrix
zero_matrix = np.zeros((2, 3))
print("\nZero matrix (2x3):\n", zero_matrix)

# Create an identity matrix
identity_matrix = np.eye(3)
print("\nIdentity matrix (3x3):\n", identity_matrix)

# Create a diagonal matrix
diagonal_matrix = np.diag([1, 2, 3])
print("\nDiagonal matrix:\n", diagonal_matrix)

# Create a matrix with random values
random_matrix = np.random.rand(2, 3)
print("\nRandom matrix (2x3):\n", random_matrix)
