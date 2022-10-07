counts = dict()
print('Enter a line of text: ')
line = input('')

words = line.split()

print('Words:', words)

print('Counting...')
for words in words :
    counts[words] = counts.get(words, 0) + 1
print('counts', counts)   