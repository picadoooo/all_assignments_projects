#7. Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.

list1 = ['1ac21', '23fg', '456', '098d','1','kls',3]

for i in range(len(list1)) :
    if(type(list1[i]) == str and list1[i].isalpha()) :
        print("")
        list1[i] = "1"
    

print(list1)

list1 = ['1ac21', '23fg', '456', '098d','1','kls',3]

list1 = ["1" if isinstance(x, str) and x.isalpha() else x for x in list1]

print(list1)

        