# Palindromes bois!
word = input('Word/sentence?').lower()
word = ''.join(filter(str.isalpha, word))
reverse = []
for i in word[::-1]:
    reverse.append(i)
reverse = ''.join(reverse)
print (reverse)
if reverse == word:
    print('Palindrome yo.')
else:
    print('Not palindrome yo.')