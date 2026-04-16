#8. Write a program that can find the max number of each row of a matrix
import math as m
list1 = [[1,2,3],[4,5,6],[7,8,9]]
list3 = []


def loop(list2) :
    for i in range(len(list2)) :
         print(max(list1[i]))
         list3.append(max(list1[i]))

        #  for j in range(len(list1[i])) :
        #     print(list1[i][j])
           
loop(list1)
print(list3)



   
     