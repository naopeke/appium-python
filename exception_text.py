import csv
import json

try:
    a = 5/0
    print(a)
except ZeroDivisionError:
    print("Can't divisible by 0")
except TypeError:
    print("unsupported operand type(s) for /: str")
finally:
    print("Run")


with open('textfile.txt', 'r') as file:
    text = file.read()
    print(text)

with open('textfile.txt', 'w') as file:
    file.write('\nThis is an additional text')

with open('test_csv.csv', mode='w', newline="") as file:
    csv_content = csv.writer(file)
    csv_content.writerow(["Name", "Age"])
    csv_content.writerow(["Tanjiro", "15"])
    csv_content.writerow(["Nezuko", "14"])

with open('test_csv.csv', mode='r') as file:
    csv_content = csv.reader(file)
    for con in csv_content:
        print(con)


with open('test.json', 'w') as file:
   data = {
       "name":"Giyu",
       "age":21
   }
   json.dump(data, file)

with open('test.json', 'r') as file:
    data = json.load(file)
    print(data)