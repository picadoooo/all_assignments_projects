# #2. Write a program to add item 7000 after 6000 in the following Python List

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1.insert(list1[2][2][1],[7000])
list1[2][2].insert(3, 7000)
print(list1[2][2])


# if len(list1) > 1 :
#     for  i in list1 :
#          if len(i) > 1 :

# def find_value(lst, target, path=[]):
#     for i, item in enumerate(lst):
#         if item == target:
#             return path + [i]
#         elif isinstance(item, list):
#             result = find_value(item, target, path + [i])
#             if result:
#                 return result
#     return None


# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

# result = find_value(list1, 5000)

# print(result)


# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# def check(list8 ,target) :
#      print(list8[2])
#      list8[2].insert(2,500)
#      return True     

# check(list1[2],300)
# print(list1)
         

# def insert_after_target(lst, target, value):
#     for i in range(len(lst)):
#         if lst[i] == target:
#             lst.insert(i + 1, value)
#             return True
#         elif isinstance(lst[i], list):
#             if insert_after_target(lst[i], target, value):
#                 return True
#     return False

# insert_after_target(list1, 6000, 7000)

# print(list1)
               
# def insert(list5,traget,value) :
#     for i in range(len(list)) :
#         if list5[i] == value :
#             list5.insert(i + 1 ,traget)
#             return True
#         elif isinstance(list5[i],list) :
#             if insert(list5[i] , traget , value) :
#                 return True

#     return False        