words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

for idx in range(len(words)):
    words[idx] = set(words[idx])
print(words)

for word in words:
    word & words[:]