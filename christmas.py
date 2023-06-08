import os

with open('employees.txt', 'r') as file:
    names = file.read().splitlines()

with open('template.txt', 'r') as file:
    template = file.read()

os.makedirs('christmasCards', exist_ok=True)


for employee_name in names:

    card_content = template.replace('NAME', employee_name)

    file_name = f'christmasCards/{employee_name}.txt'
    with open(file_name, 'w') as file:
        file.write(card_content)

print("Your christmas cards have been created successfully in the folder sub-directorie christmasCards!")
