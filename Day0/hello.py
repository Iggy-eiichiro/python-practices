def palindrome(word):
    return word==word[::-1]

if __name__ == "__main__":
    word = input("Enter a word: ")
    if palindrome(word):
        print(f"{word} is a palindrome.")
    else:
        print(f"{word} is not a palindrome.")
