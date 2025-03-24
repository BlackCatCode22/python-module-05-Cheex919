import re
x = 'just got $60.00 from selling that game!'
y = re.findall (r'\$[0-9.]+',x)
print(y)
