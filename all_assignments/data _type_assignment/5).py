#5. You are given a list of integers. You are asked to make a list by running through elements of the list by adding all elements greater and itself.

list1 = [2,4,6,10,1]
list2 = []



for i in range(len(list1)) :
    print("a")
    total = 0
    for j in range(len(list1)) :
     if list1[j] >= list1[i]:
        total += list1[j]
    list2.append(total)

print(list2)