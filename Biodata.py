name=input('Enter your name')
age=input('Enter your age')
with open('File.txt', 'w') as file:
    file.write(f'Name: {name}\n')
    file.write(f'Age: {age}\n')
print(name)
print(age) 
file.close()
   