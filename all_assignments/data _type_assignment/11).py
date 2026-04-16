#Write a program to count unique number of vowels using sets in a given string. Lowercase and upercase vowels will be taken as different.

#aeiou
count = 0

Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
set1 =set()
for ch in Str1 :
    if ch in "aeiou"+ str.upper("aeiou") :
        set1.add(ch)

print(f"No of unique vowels : {len(set1)} {set1}")
list4 = []


for ch in Str1 :
    if ch in "aeiou"+ str.upper("aeiou") :
        list4.append(ch)

print(count)



print(len(list(dict.fromkeys(list4))))