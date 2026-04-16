#17. Write a Python function to concatenate any no of dictionaries to create a new one.

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
# dis4 = dic1 | dic2 | dic3
dis4 = dict()

for i in(dic1,dic2,dic3):
 dis4.update(i)

print(dis4)

