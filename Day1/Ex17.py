letters = ['a','b','a']
results = {}
for letter in letters:
    letter_count = letters.count(letter)# count() method counts the number how many times the leter apperas in the list.
    results[letter] = letter_count
print(results)