# Python Basics – My Learning Notes

This file documents my foundational Python knowledge, including code snippets I have written and understood.

## Variables & Data Types
- `name = "Isaac"` → string (text)
- `age = 25` → integer (whole number)
- `height = 1.75` → float (decimal number)
- `is_learning = True` → boolean (True/False)

## Lists
- `fruits = ["apple", "banana", "orange"]` → stores multiple items.
- Access items: `fruits[0]` → returns "apple"

## Dictionaries
- `person = {"name": "Isaac", "age": 25}` → key-value pairs.
- Access: `person["name"]` → returns "Isaac"

## Control Flow
- **If-Else:**
  ```python
  if age >= 18:
      print("Adult")
  else:
## For loop
for fruit in fruits:
    print(fruit)
## While loop 
  count = 0
while count < 5:
    print(count)
    count += 1
## Functions
def greet(name):
    print("Hello", name)

greet("Isaac")  # Output: Hello Isaac
## File Handing 
with open("file.txt", "r") as f:
    content = f.read()
    print(content)
## Write to a file 
with open("newfile.txt", "w") as f:
    f.write("Hello World")
## Automated Project
import os
import shutil

source = "."
destination = "organized"

if not os.path.exists(destination):
    os.mkdir(destination)

for file in os.listdir(source):
    if file.endswith(".txt"):
        shutil.move(file, destination)
        
