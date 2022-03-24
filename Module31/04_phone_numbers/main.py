import re

phone_numbers = ['9999999999', '999999-999', '99999x9999']
pettern = r'\b[8-9]\d{9}'
for number in phone_numbers:
    if re.findall(pettern,number):
        print(f'{number} номер: всё в порядке')
    else:
        print(f'{number} номер: не подходит')