import random
name = input('Type your name: ').capitalize()
print(f'Welcome {name} to this survival game')
age = int(input('In order to make this survival simulation more realistic, please type your age: '))
location = input(f'Alright {name}, you are {age} years old. Where do you live?\nLocation: ')
salary = random.randrange(3000,8000)
houserent = random.randrange(2000,4000)
houserent2= random.randrange(4000,6000)
averagebills = random.randrange(500,1250)
print(f'Okay {name}, let us find your salary range. It will be randomly appointed to you')

print(f'Your salary is {salary}')


if salary >= 5500:
    print(f'Your salary is {salary} so your avarage house rent will be {houserent2}')
    print(f'You have {salary-houserent2} left')
    print('So you are in a troubling situation right now. You did not pay your monthly bills yet')
    answer = input(f"{name} would you like to learn your average spend on bills? Yes/No/Hell No: ").lower()
    if answer == 'Yes'.lower(): 
        remainingmoneyhigh = (salary-houserent2) - averagebills
        print(f'Your monthly average amount for bills is {averagebills} and you have now: {remainingmoneyhigh}')
        if remainingmoneyhigh >= 1000:
            print(f'{name}! You are lucky to made it so far. You have {remainingmoneyhigh} TL')
            answer2 = input(f'Would you like to spend some time outside to have fun {name}: Yes or No: ').lower()
            if answer2 == 'Yes'.lower():
                print(f'Dear {name}, you have some money you need to be carefully spend it. Hope you will survive. Thanks for playing :)')
                exit
            elif answer2 == 'No'.lower():
                print('Congratulations! You managed to survive for another month. Deep depression awaits you :)')
            else:
                print('Not a valid option. You lose.')
                exit
        elif 0<= remainingmoneyhigh <= 1000:
            print(f'You have little money left: {remainingmoneyhigh} TL. Hope you will survive. Thanks for playing :)')
        else:
            print(f'Dear {name}, you could not managed to survive you lose again: {remainingmoneyhigh} TL')
            exit
    elif answer == 'No'.lower():
        print(f'Your ignorance will let you live just another month you lose')
        exit    
    elif answer == 'Hello No'.lower():
        print(f'How do manage to live in your real life? Sorry you lose')
        exit
    else:
        print('Not a valid option. You lose.')
        exit
elif 3000 < salary < 5500:
    print(f'Your salary is {salary} so your avarage house rent will be {houserent}')
    print(f'You have {salary-houserent} left')
    print('So you are in a troubling situation right now. You did not pay your monthly bills yet')
    answer = input(f"{name} would you like to learn your average spend on bills? Yes/No/Hell No: ").lower()
    if answer == 'Yes'.lower(): 
        remainingmoneylow = (salary-houserent) - averagebills
        print(f'Your monthly average amount for bills is {averagebills} and you have now: {remainingmoneylow}')
        if remainingmoneylow >= 1000:
            print(f'{name}! You are lucky to made it so far. You have {remainingmoneylow} TL')
            answer2 = input(f'Would you like to spend some time outside to have fun {name}: Yes or No: ').lower()
            if answer2 == 'Yes':
                print(f'Dear {name}, you have some money you need to be carefully spend it. Hope you will survive. Thanks for playing :)')
                exit
            elif answer2 == 'No':
                print('Congratulations! You managed to survive for another month. Deep depression awaits you :)')
            else:
                print('Not a valid option. You lose.')
                exit
        elif 0<= remainingmoneylow <= 1000:
            print(f'You have little money left: {remainingmoneylow}')
            print(f'{name}! You are lucky to made it so far. You have {remainingmoneylow} TL')
            answer2 = input(f'Would you like to spend some time outside to have fun {name}: Yes or No: ').lower()
            if answer2 == 'Yes':
                print(f'Dear {name}, you have some money you need to be carefully spend it. Unfortunately you did not survive. Thanks for playing :)')
                exit
            elif answer2 == 'No':
                print('Congratulations! You managed to survive for another month. Deep depression awaits you :)')
            else:
                print('Not a valid option. You lose.')
                exit
        else:
            print(f'Dear {name}, you could not managed to survive you lose again: {remainingmoneylow}')
            exit
    elif answer == 'No'.lower():
        print(f'Your ignorance will let you live just another month you lose')
        exit    
    elif answer == 'Hello No'.lower():
        print(f'How do manage to live in your real life? Sorry you lose')
        exit
    else:
        print('Not a valid option. You lose.')
        exit
else:
    print(f'Dear {name} with your salary you could not survive in Turkey')
