#Statement
age = 20
if age >= 18:
    print('eligible')
else:
    print('not eligible')

score = 75
if score >= 90:
    print('A')
elif score >= 75:
    print('B')
else:
    print('C')

#Loop
for i in range(10):
    print(i)

name= 'nao'
for i in name:
    print(i)

#While
count = 0
while count < 5:
    count+= 1
    print(count)

#Break
name = 'nao'
for i in name:
    if i =='a':
        break
    print(i)

#String
text = 'Hello World'
print(len(text))
print(text.count("is"))
print(text.lower())
print(text.upper())
print(text.replace('Hello', 'Good morning'))

names = text.split(' ')
print(names)

joins = ','.join(names)
print(joins)

print('Hello' in text)