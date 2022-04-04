# Python program to find smallest
# number in a list
 
# creating empty list
list1 = []
 
# asking number of elements to put in list
num = int(input("Please enter number of elements in list: "))
 
# iterating till num to append elements in list
for i in range(1, num + 1):
    element= int(input("Enter elements: "))
    list1.append(element)
     
# print maximum element
print("Smallest element is:", min(list1))