a = [1,2,3]
b = [2,3,4]

results = []
for i in a:# take 1,2,3
    if i in b: # check if 1,2,3 is in b
        results.append(i)
print(results)