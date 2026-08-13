words = ['eat','tea','tan','nat']
anagrams = {}

for word in words:
    sorted_word = ''.join(sorted(word))# sort the letters of the word and join them back together to form a new string.'' is used for join the letters together without any spaces.      
    if sorted_word in anagrams:
        anagrams[sorted_word].append(word)
    else:
        anagrams[sorted_word] = [word]# if the sorted_word is not in the anagrams dictionary, create a new key-value pair with the sorted_word as the key and a list containing the original word as the value.

print(list(anagrams.values()))#anagrams.values() take the values, example:[['eat','tea'],['tan','nat']]. list() convert the values of the dictonary into alist.