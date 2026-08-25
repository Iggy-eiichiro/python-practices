word = ['apple','bat','ant']
result = {}
for word in word:
    first_letter = word[0]
    if first_letter not in result:
        result[first_letter] = []
    result[first_letter].append(word)

print(result)