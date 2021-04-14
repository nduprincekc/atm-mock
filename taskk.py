import random

data = {}  # Blank database for the storing of details of the user

dept = '****' * 20 # demactor for separating the stages


def man():
    is_valid = False
    print('Welcome to KC BANK')

    while not is_valid:
        new_account = int(input(' Do you have any account with us\n'
                                'type (1) for Yes or (2) for No \n').lower())
        if new_account == 1:
            is_valid = True
            print('login to your account')
            login()
        elif new_account == 2:
            print('\n')
            ask = input('Do you wish to open an account with us ?:\n'
                        'Enter \'yes\' if you wish or Enter \'no\' if you do not wish to open an account with us  ')

            if ask == 'yes'.lower():
                is_valid = True

                reg()
            elif ask == 'no'.lower():

                print('\nThanks for banking with us.\nGoodBye')
                is_valid = True

        elif new_account != 1 or new_account != 2:
            print("incorrect")
            man()
    else:
        print("incorrect")
        man()


# code for the main banking operation


def bank_operation(user):
    check = True
    while check:
        print('Welcome To KC BANK %s' % user[0], user[1])
        promo = float(500)
        print('*****' * 5)
        print('You have been credited with: N', promo, 'as promo offer ')
        print('These are the available options: \n ')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Account Balance')
        print('4. Complaint')
        print('5. Logout')
        print('6. Recover Your account')
        print('7. Change Phone number')
        print('8. Exist')
        selected_option = int(input('Please select an option\n'))

        if selected_option == 1:

            print("How much would you like to withdraw")
            withdraw = float(input())
            reference = random.randint(1000, 2000)
            print('Take your cash', withdraw, 'Naira\n Thanks for banking with us')
            check = False
            bank_operation(user)
            if withdraw > promo:
                print('Insufficient Account')
                print('try again')
                check = False
                bank_operation(user)
            else:
                pass
            print('Your remaining Balance is: ', promo - withdraw)
            print('Your Reference Number is', reference)

        elif selected_option == 2:
            r_balance = float(input('How much would you like to deposit\n'))
            currentBalance1 = promo + r_balance
            print('Deposit Transaction Completed')
            print('You deposited', r_balance,
                  '\nYour new Current balance is now: N', currentBalance1)
            check = False
            bank_operation(user)

        elif selected_option == 3:
            print('Your Account Balance is ', promo)
            check = False
            login()
        elif selected_option == 4:
            complaint = input('What issue will you like to report?\n')
            print('Your ', complaint, 'have been noted down')
            print('Thanks for contacting us, We will look into the matter')
            check = False
            login()
            print(dept)
        elif selected_option == 5:
            print('You have been logged out')
            print('Thank You for Banking with us')
            login()
            check = False
            print(dept)

        elif selected_option == 6:
            recover_details()
            check = False
            print(dept)

        elif selected_option == 7:
            number_checker()
            check = False
            print(dept)

        elif selected_option == 8:
            print('Good Bye')
            exit()
        else:
            print('invalid option')
            check = True
    else:
        print('invalid')
        bank_operation(user)


def login(): # login page
    print('\n\n******* Login ********')
    isloginsuccessful = False

    while not isloginsuccessful:
        print(dept)
        user_account = int(input('Enter your account number: \n'))
        password = input('Enter your password\n')
        for num, detail in data.items():
            if num == user_account:
                if detail[3] == password:
                    isloginsuccessful = True
                    bank_operation(detail)
            else:
                print('incorrect account')
                login()


def reg(): # registration page
    print('\n*********** Account Opening Page ***********\n')
    print(dept)

    check = True
    print('fill in the below information')
    f_name = input('Enter your First name: ').capitalize()
    l_name = input('Enter your Last name: ').capitalize()
    password = input('Enter Your Pin: ')
    if len(password) < 4:
        print('Pin is too short\n try Again')
        reg()
    email = input('Enter your Email Address: ')
    phone_number = int(input('Enter your phone number: '))
    while check:
        if '@' and '.com' not in email:
            print('\nincorrect email check your email and type again')
            reg()
        else:
            check = False
    act = account()
    data[act] = [f_name, l_name, email, password, phone_number]
    print('Your account have been created successfully')
    print(dept)
    print('\nWe  Welcome You to KC BANK')
    print('Your account details are as follows:')
    print('Your Account number is:', act)
    print('Your Full Name is:', f_name, l_name)
    print('Your Mobile Number is:', phone_number)
    print('Please Note that your Mobile number will be used to receive your Transaction Alerts \n')
    print(dept)
    print("You are given N500.00 as Account Opening Bonus")

    print("Thank you for choosing us")
    print("_________________" * 4)

    login()


def account():
    return random.randrange(6534245221, 9928931223)


def recover_details():
    print("______________" * 4 + "\nRecover your Account Details\n" + "______________" * 4)
    print("| 1 | Lost Account Number"
          "\n| 2 | Forgot Pin\n| 3 | Change Mobile Number\n" + "***********" * 4)
    UserInput = int(input("\nSelect Option: "))
    if UserInput == 1:
        account_recovery = input('Enter your Email ')
        if '.com' and '@' not in account_recovery:
            print('incorrect details')
            bank_operation(data)
        else:
            print('We will get back to you')

    if UserInput == 2:
        account_recovery = input('Enter your Email ')
        if '.com' and '@' not in account_recovery:
            print('incorrect details')
            bank_operation(data)
        else:
            print('We will send you your pin via your email')

    if UserInput == 3:
        number_checker()
        print(dept)
    else:
        print("You have selected invalid option")
        print(dept)

def number_checker():
    print(dept)
    print("Change Mobile Number Page")
    ninCheck = input("Have you registered for NIN? ")
    if ninCheck.lower() == 'yes' or ninCheck.lower() == 'y':
        ninn_Check = True
        while ninn_Check:
            UserInp = input("Enter NIN Number: ")
            print("Your NIN: %s \nThank You, we will get back to you!" % UserInp)
            ninn_Check = False
            login()
    else:
        print("Wrong input")
        number_checker()
    print(dept)
    print(dept)
man()
