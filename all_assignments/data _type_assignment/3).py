#3. Suppose you are given a list of candy and another list of same size representing no of items of respective candy.

candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items = [10,20,34,74,32]

if len(candy_list) == len(no_of_items) :
    for i in range(len(candy_list)) :
        print(f"{candy_list[i]} - {no_of_items[i]}")