#s = input()
s = 'thegorillaiswatching'
word = 'sheriff'
letters = {i:0 for i in word}

for letter in s:
    if letter in letters:
        letters[letter] = letters.get(letter) + 1

print(letters)
print(min(letters.values()))