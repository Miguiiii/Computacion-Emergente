import numpy as np 

sig = lambda x: 1/(1+np.exp(-x))

"""X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
WI = np.random.randn(2, 4)
WO = np.random.randn(4, 1)
BI = np.zeros((1,1,4))
BO = np.random.randn(1, 1)

print(X)
print(WI)
print(WO)
print(BI)
print(BI[0])
print(BO)

calc = np.dot(X, WI)
print(calc)"""


test = lambda x: 1 if x>0 else 0

print(type(test))

"""print(X.shape)
print(type(X))
for i in X:
	print(i,type(i))

print(X[0])



t = np.array([[0,0]])
print(t.shape)
print(X)

print(WI)

print(WO)

R = np.dot(X, WI)+1

print(R)

R = sig(R)

print(R)"""
