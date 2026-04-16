#6. Find list of common unique items from two list. and show in increasing order

num1 = [23,45,67,78,89,34]
num2 = [34,89,55,56,39,67]
num3 = []

for i in range(len(num1)) :
    for j in range(len(num1)):
        if num1[i] == num2[j] :
            num3.append(num1[i])

for i in range(len(num3)):
    for j in range(i+1, len(num3)):
        if num3[i] > num3[j]:
            num3[i], num3[j] = num3[j], num3[i]

print(num3)

    

