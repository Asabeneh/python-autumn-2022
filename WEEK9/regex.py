import re

# re.match, re.search, re.findAll, re.split,re.sub

txt = 'Python is the best language'
pattern = 'python'

matches = re.match(pattern, txt, re.I)
print(matches)
print(matches.span())

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.search('first', txt, re.I)
print(matches)

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language. Python can be used for data analysis, ml, ds and for web development'''

print()
matches = re.findall('Python', txt, re.I)
print(len(matches))


txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)


txt = '''%I@ a%m te%%a%%che%r% a%n%d %% I# l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%chi$ng m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u t@o b%e a t%e%a%cher?'''

print(re.sub(r'[^a-zA-Z ]', '', txt))