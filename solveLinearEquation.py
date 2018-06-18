#https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.linalg.solve.html

import numpy as np
import fractions

#the translate decimal to fraction
np.set_printoptions(formatter={'all':lambda x: str(fractions.Fraction(x).limit_denominator())})

def solveLinearEquation(left, right):
	left = np.array(left)
	right = np.array(right)

	result = np.linalg.solve(left, right)

	print result

solveLinearEquation([[3, 2], [2,3]], [7, 8])
solveLinearEquation([[5, 7], [20, -18]], [11, 39])

