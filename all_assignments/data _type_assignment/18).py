data = [13,42,15,37,22,39,41,50]
result = {"11-20" : 0 , "21-30" : 0 , "31-40" : 0 , "41-50" : 0}
# Output:
# 	{11-20:2,21-30:1,31-40:2,41-50:3}



for i in data :
      if i >= 10 and i <= 20 :
            result["11-20"] += 1
      elif i >= 21 and i <= 30 :
            result["21-30"] += 1
      elif i >= 31 and i <= 40 :
            result["31-40"] += 1
      elif i >= 41 and i <= 50 :
            result["41-50"] += 1
         
        
print(result)
