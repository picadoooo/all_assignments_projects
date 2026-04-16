#4. Running Sum on list Write a program to print a list after performing running sum on it

list1 = [1, 2, 3, 4, 5, 6] 
list2 = []
total = 0

for  i in list1 :
     
     total += i
     list2.append(total)

print(list2)
