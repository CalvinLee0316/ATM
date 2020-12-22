#! /usr/bin/env python3

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
    
accounts = []
accountNums = []
def createTestAccounts():
    for i in range (20):
        accounts.append(Account(i, 1234+i, 10000+i))
        accountNums.append(i)
        accounts[i].addBalance(2000+i)
        accounts[i].addBalance(3000+i)

    
def accountExists(accountNum):
    return accountNum in accounts

def accountInt(inputAccount):
    try:
        int(inputAccount)
        return True
    except ValueError:
        return False

createTestAccounts()
#TODO main section on console
while(True):
   
    bankName = 'Calvin Bank'
    print('#### Welcome to %s, what is your account number? ####' % bankName)
    account_input = input()
    if accountInt(account_input) != True:
        print('#### Please enter a number ####')
        continue
    if int(account_input) not in accountNums:
        print('#### That account does not exist #####')
        continue
    print('#### Welcome, account number %s, please enter your pin ####' % account_input)
    currAccount = accounts[int(account_input)]
    try:
        pin_input = int(input())
    except ValueError:
        print('##### Please enter a number ####')
        continue
    if (currAccount.correctPin(pin_input)) != True :
        print('#### Pin is incorrect ####')
        continue

    print('#### Which balance would you like access? ####')
    for i in range(0, len(currAccount.getBalanceArray())):
        print('Balance %d' % (i+1))

  
    try:
        balanceNum = int(input())
    except ValueError:
        print('#### Please enter a number ####')
        continue
        
    if int(balanceNum) > len(currAccount.getBalanceArray()) | int(balanceNum)<1:
        print('Invalid Balance Number')
        continue

    print('#### How can we help you with this account? ####')
    print('#### 1. View Balance           ####')
    print('#### 2. Deposit                ####')
    print('#### 3. Withdraw               ####')
    print('#### 4. Exit                   ####')
    try:
        service = int(input())
    except ValueError:
        print('Invalid service number')
        continue
    if service > 4 | service <1:
        print('#### Invalid service number, please input a number between 1 and 4 ####')
        continue
    if service == 1:
        print('#### Current Balance : $%d ####' % (currAccount.selectBalance(balanceNum)))
        print('#### Press enter to exit ####')
        input()
        break
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
    else:
        break
print('#### Thank you for using %s, come again! ####' % bankName)
        
        
