import re


file = open('Week2_text.txt')


text = file.read() 
number_regex = '[0-9]+'
numbers = re.findall(number_regex, text) 


total = sum(int(num) for num in numbers)

print(total)


file.close()