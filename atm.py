#! /usr/bin/env python3

#Create an Account class with all necessary attributes and getters and setters
class Account:
    def __init__(self, accountNum, pin, balance):
        self.accountNum = accountNum
        self.pin = pin
        self.balance = [int(balance)]

    def addBalance(self, balance):
        self.balance.append(balance)

    def selectBalance(self, balanceNum):
        return self.balance[balanceNum-1]

    def withdraw(self,balanceNum, amount):
        self.balance[balanceNum-1] -= amount

    def deposit(self, balanceNum, amount):
        self.balance[balanceNum-1] += int(amount)

    def correctPin(self, user_pin):
        return user_pin == self.pin

    def getAccountNum(self):
        return self.accountNum

    def getPin(self):
        return self.pin

    def getBalanceArray(self):
        return self.balance

#List of Account objects   
accounts = {}
#List of all account numbers
accountNums = []
#Generate test accounts, accounts and accountNums
#accounts is a dictionary, so indices do not need to match account numbers
#Would be populated differently if used by actual bank
#Would be populated with actual accounts, balances, and pins
def createTestAccounts():
    for i in range (20):
        accountNumber = i
        accounts[accountNumber]= Account(accountNumber, 1234+accountNumber, 10000+accountNumber)
        accountNums.append(i)
        accounts[i].addBalance(2000+i)
        accounts[i].addBalance(3000+i)

#function that checks to see if the input account exists
def accountExists(accountNum):
    return accountNum in accounts

#function that checks to see if the input number is actually a number
def accountInt(inputAccount):
    try:
        int(inputAccount)
        return True
    except ValueError:
        return False

#call the function created to generate accounts
createTestAccounts()

#main section on console
while(True):
    #Put name of bank here
    bankName = 'Calvin Bank'
    #Welcoming statement, starting screen
    print('#### Welcome to %s, what is your account number? ####' % bankName)
    account_input = input()

    #Check to see if account number is valid
    if accountInt(account_input) != True:
        print('#### Please enter a number ####')
        continue
    if int(account_input) not in accountNums:
        print('#### That account does not exist #####')
        continue
    #load the correct account into currAccount
    currAccount = accounts[int(account_input)]
    pinTrue = False

    #check if pin is correct, give 3 tries
    print('#### Please enter your pin ####')
    for i in range(3):
        #check to see if the pin is valid
        try:
            pin_input = int(input())
            if (currAccount.correctPin(pin_input)) != True :
                if(i!=2):
                    print('#### Pin is incorrect, %d tries left ####' % (2-i))
            else:
                pinTrue = True
                break
        except ValueError:
            print('##### Please enter a number ####')
            if(i!=2):
                print('#### %d tries left ####' % (2-i))
            pinTrue = False

    #if pin was not matched go back to beginning screen
    if pinTrue == False:
        print('Incorrect too many times, reverting to starting screen')
        continue
    
    print('#### Which balance would you like access? ####')
    #List all balance options in given account
    for i in range(0, len(currAccount.getBalanceArray())):
        print('Balance %d' % (i+1))

    
    try:
        balanceNum = int(input())
    except ValueError:
        print('#### Please enter a number ####')
        continue
        
    #check to see if balance number is valid
    if int(balanceNum) > len(currAccount.getBalanceArray()) | int(balanceNum)<1:
        print('Invalid Balance Number')
        continue

    print('#### How can we help you with this account? ####')
    print('#### 1. View Balance           ####')
    print('#### 2. Deposit                ####')
    print('#### 3. Withdraw               ####')
    print('#### 4. Exit                   ####')
    #check to see if service input was a number
    try:
        service = int(input())
    except ValueError:
        print('Invalid service number')
        continue

    #check to see if service input was valid
    if service > 4 | service <1:
        print('#### Invalid service number, please input a number between 1 and 4 ####')
        continue
    #View balance
    if service == 1:
        print('#### Current Balance : $%d ####' % (currAccount.selectBalance(balanceNum)))
        print('#### Press enter to exit ####')
        input()
        break
    #Deposit
    elif service == 2:
        print('#### How much would you like to deposit? ####')
        try:
            deposit = int(input())
        except ValueError:
            print('#### Please enter a number ####')
            continue
        if deposit < 1:
            print('#### Invalid amount, please deposit at least 1 dollar ####')
        else:
            currAccount.deposit(balanceNum, deposit)
            print('#### Deposited $%d         ####' % (deposit))
            print('#### Current Balance : $%d ####' % (currAccount.selectBalance(balanceNum)))
            print('#### Press enter to exit')
            input()
            break
    #Withdraw
    elif service == 3:
        print('#### How much would you like to withdraw? ####')
        try:
            withdraw = int(input())
        except ValueError:
            print('#### Please enter a number ####')
            continue
        if withdraw > currAccount.selectBalance(balanceNum):
            print('#### Invalid amount, please withdraw less than the current balance ####')
            print('#### Current Balance : $%d ####' % (currAccount.selectBalance(balanceNum)))
            print('#### Press enter to exit')
            input()
            break                           
        else:
            currAccount.withdraw(balanceNum, withdraw)
            print('#### Withdrawal of $%d         ####' % (withdraw))
            print('#### Current Balance : $%d ####' % (currAccount.selectBalance(balanceNum)))
            print('#### Press enter to exit')
            input()
            break
    #Exit
    else:
        break
#Exitting message
print('#### Thank you for using %s, come again! ####' % bankName)
        
        
