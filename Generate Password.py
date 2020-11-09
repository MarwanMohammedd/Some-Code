import numpy as np
X = int(input("Enter Number Of Password Length:"))
def generate(X : int)->str:
	__strList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	password = ''
	for i in range(X):
		password += __strList[np.random.randint(len(__strList))]
	return password
print(f"Your Password Is:{generate(X)}")