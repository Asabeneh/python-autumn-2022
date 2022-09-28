""" Create an acronym or an abbreviation for the name 'Python For Everyone'.
Create an acronym or an abbreviation for the name 'Coding For All'. """

# PFE

txt = 'Python For Everyone'
words = txt.split()
print(words[0][0])
print(words[1][0])
print(words[2][0])

abbr = words[0][0] + words[1][0] + words[2][0]
print(txt[0])
print(txt[7])
print(txt[11])

sent =  'You cannot end a sentence with because because because is a conjunction'
start = sent.find('because')
end = sent.rfind('because')
print(sent[start:end + 1])




