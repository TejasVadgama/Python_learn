import numpy as np

#Tejas Vadgama -EK3 -92510133044.

A = np.arange(1, 17).reshape(4,4)
print(A[0:2,0:4]) #Que.1
print(A) #Here We Get the Our Slice Matrix.

# B = np.arange(1,26).reshape(5,5)
# print(B)
# print(B[1:4,1:4])  #Que2 Here We Take The Between Middle Of it and Print It.

# # C = B[B%2==0]
# # print(C)
# print([B%2==0]) #For If Ask Boolean #Que.3

# D="pythonprogramming"
# print(D[0:6]) #Que.4

# E = np.array([1,2,3,4,5])
# F = np.array([6,7,8,9,10])
# G = np.concatenate((E,F))
# print(G) #Que.5

# H = np.array([10,5,8,3])
# print(np.sort(H)) #Que.6

I = np.concatenate([
    A[0, :],                  # First row
    A[1:3, [0, 3]].flatten(), # First and last of middle rows
    A[3, :]                   # Last row
])
print(I) #Que.7

# J = np.arange(1,101)
# #print(J)
# J[4::5]=0 #4 Here For the From 0 to 4 Index is 5 Value Or, 5 For the 5th value range = 0 means change to 0.
# print(J) #Que.8

# J[1::2]=0
# print(J) #Que.9

# l1 = [1,2,3]
# l2 = [4,5,6]
# list = (l1[0]+l2[0]+l1[2]+l2[2])
# print(list) #List QUe. Answer Two List Addition.