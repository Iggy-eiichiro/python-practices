numbers = [1,2,3,4,5]
n=2

results = []

for i in range(0,len(numbers),n):
    results.append(numbers[i:i+n])

print(results)