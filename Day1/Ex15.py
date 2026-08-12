text = 'Race Car!'
cleaned = ''

for char in text:
    if char.isalnum():#isalnum() is method that cheks if the character is alphanumeric(a letter or a number).
        cleaned += char.lower()#lower() is method that converts the character to lowercase.
if cleaned == cleaned[::-1]:#[::-1] is a slice that reverses the string.
    result = True
else:
    result = False

print(result)