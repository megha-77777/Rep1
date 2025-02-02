import getpass
import string
import os

# Creating a list of users, their PINs, and bank statements
users = ['abc', 'def', 'ghi']
pins = ['1111', '2222', '3333']
amounts = [1000, 2000, 3000]
count = 0

# While loop checks existence of the entered username
while True:
    user = input('\nENTER USER NAME: ')
    user = user.lower()
    if user in users:
        if user == users[0]:
            n = 0
        elif user == users[1]:
            n = 1
        else:
            n = 2
        break
    else:
        print('INVALID USERNAME')

# Comparing PIN
while count < 3:
    pin = str(input('PLEASE ENTER PIN: '))
    if pin.isdigit():
        if user == users[0] and pin == pins[0]:
            break
        elif user == users[1] and pin == pins[1]:
            break
        elif user == users[2] and pin == pins[2]:
            break
        else:
            count += 1
            print('INVALID PIN')
            print()
    else:
        print('PIN CONSISTS OF 4 DIGITS')
        count += 1

# In case of a valid pin- continuing, or exiting
if count == 3:
    print('***********************************')
    print(' 3 UNSUCCESSFUL ATTEMPTS, EXITING ')
    print('!!!!!YOUR CARD HAS BEEN BLOCKED!!!!!')
    print('***********************************')
    exit()

print('*************************')
print('LOGIN SUCCESSFUL, CONTINUE')
print('*************************')
print()
print('**************************')
print(str.capitalize(users[n]), 'WELCOME TO ATM')
print('**************************')
print('----------ATM SYSTEM-----------')

# Main menu
while True:
    print()
    print('*******************************')
    response = input('SELECT FROM FOLLOWING OPTIONS: \nStatement__(S)\nWithdraw___(W) \nLodgement__(L) \nChange PIN_(P) \nQuit_______(Q) \n: ')
    print('*******************************')
    valid_responses = ['s', 'w', 'l', 'p', 'q']
    response = response.lower()
    
    if response == 's':
        print('*********************************************')
        print(str.capitalize(users[n]), 'YOU HAVE', amounts[n], 'RUPEES IN YOUR ACCOUNT.')
        print('*********************************************')
    
    elif response == 'w':
        print('*********************************************')
        cash_out = int(input('ENTER AMOUNT TO WITHDRAW: '))
        print('*********************************************')
        
        if cash_out % 500 != 0:
            print('******************************************************')
            print('AMOUNT YOU WANT TO WITHDRAW MUST MATCH 500 RUPEES NOTES')
            print('******************************************************')
        elif cash_out > amounts[n]:
            print('*****************************')
            print('YOU HAVE INSUFFICIENT BALANCE')
            print('*****************************')
        else:
            amounts[n] = amounts[n] - cash_out
            print('***********************************')
            print('YOUR NEW BALANCE IS:', amounts[n], 'RUPEES')
            print('***********************************')
    
    elif response == 'l':
        print()
        print('*********************************************')
        cash_in = int(input('ENTER AMOUNT YOU WANT TO LODGE: '))
        print('*********************************************')
        print()
        
        if cash_in % 500 != 0:
            print('AMOUNT YOU WANT TO LODGE MUST MATCH 500 RUPEES NOTES')
        else:
            amounts[n] = amounts[n] + cash_in
            print('****************************************')
            print('YOUR NEW BALANCE IS:', amounts[n], 'RUPEES')
            print('****************************************')
    
    elif response == 'p':
        new_pin = str(input('ENTER A NEW PIN: '))
        if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
            print('******************')
            new_ppin = str(input('CONFIRM NEW PIN: '))
            if new_ppin != new_pin:
                print('PIN MISMATCH')
            else:
                pins[n] = new_pin
                print()
                print('~~NEW PIN SAVED~~')
        else:
            print(' NEW PIN MUST CONSIST OF 4 DIGITS \nAND MUST BE DIFFERENT TO PREVIOUS PIN')
    
    elif response == 'q':
        exit()
    else:
        print('RESPONSE NOT VALID')
