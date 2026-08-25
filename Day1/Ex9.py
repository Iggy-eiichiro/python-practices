numbers = [1,2,3,4]
n = 2

results =[]
for i in range(len(numbers)-n+1): # How many times I want to iterate over the list(3 times)
    results.append(numbers[i:i+n])# i is the starting index and i+n is the ending index of the sublist

print(results)