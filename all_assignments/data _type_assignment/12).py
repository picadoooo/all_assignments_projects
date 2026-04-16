#  Intersection of two lists. Intersection of two list means we need to take all those elements which are common to both of the initial lists and store them into another list. Only use using list-comprehension.Example 1:

lst1 = {4, 9, 1, 17, 11, 26, 28, 54, 69}
lst2 = {9, 9, 74, 21, 45, 11, 63, 28, 26} 

list3 = [ i  for i in lst1 if i in lst2]
print(list3)


