import re


f = open('./sample.txt', 'r')
# print(dir(f))
# f.readline(), f.read(), f.readlines(), f.read().splitlines()
txt = f.read()
words = re.sub(r'[^a-zA-Z ]', '', txt.lower(), re.I).replace('.', '').split(' ')
print(words)
unique_words = set(words)
print(unique_words)

total_num_words = len(words)
total_unique_words = len(unique_words)
print(total_num_words, total_unique_words)
print( (total_unique_words /total_num_words) * 100 )
f.close()
