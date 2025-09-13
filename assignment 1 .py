import numpy as np
print("= = = Mathematical operations= = =")
a=np.array([1,2,3,4,5])
#1.exponenetiation
exp_a=np.exp(a)
print("Exponentiation (e^x):",exp_a)
#2.trigonometric sum
sin_a=np.sin(a)
print("sine values:",sin_a)
print("\n = = = Linear Algebra= = =")
# define two matrices
A=np.array([[1,2],[3,4]])
B=np.array([[2,0],[1,2]])
#.1 matrix multiplication
mat_mul=np.dot(A,B)
print("Matrix Multiplication \n",mat_mul)
#2.determinant of A
det_A=np.linalg.det(A)
print("\n Random Number Generation= =")
#1.random integers between 10 and 50
rand_ints=np.random.randint(10,50,size=5)
print ("random integers:",rand_ints)
#2.random 3*3 float matrix
rand_floats=np.random.rand(3,3)
print("Random 3*3 Float Matrix:\n",rand_floats)
print("\n = = = Statistics= = =")
#define a new array
data=np.array([10,20,30,40,50])
#1.mean
mean_val=np.mean(data)
print("Mean:",mean_val)
#2.standard deviation
std_val=np.std(data)
print("Standard Deviation:",std_val)