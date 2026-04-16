#13. Convert a list of Tuples into Dictionary.
#method 1
list1 = [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]

# print(dict(list1))

#mthod 2


for i in range(len(list1)):
  print(list1[i][0], list1[i][1])
