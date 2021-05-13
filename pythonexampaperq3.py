




L1 = [1,2,3,7,8,9]
L2 = [4,5,6]
print("L1:",L1)
print("L2:",L2)

#1
SL1=sorted(L1)
print("largest from l1 :",SL1[-1])
print("Second largest from l1 :",SL1[-2])

#2
print("\nL2 after deleting last element:")
L2.pop()
print(L2)


#3
print("\nAdd L1 and L2 and store in L3")
L3 = L1+L2
print("L3:",L3)

#4
print("\nInserting new number 14 in L1 and printing its position too")
L1.append(14)
print(L1)
print(L1.index(14))



