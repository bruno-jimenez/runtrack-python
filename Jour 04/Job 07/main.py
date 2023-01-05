L = [8,24,48,2,16,9,7,84,91]
i = 0
rslt = 0
while i < len(L): 
    if L[i]% 2 == 0:
     rslt = rslt + L[i]
    i = i + 1
print (rslt)