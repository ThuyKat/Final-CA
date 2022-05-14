from datetime import date
import random
class Bank(object):
    def __init__(self, CID):
        self.TID = 0
        self.CID = CID
        self.AccountName = ''
        self.BSB = '123-456'
        self.AccountNo = ''
        self.Balance = 0

    def create_account(self):
        """This function extract customer details in customer.txt to generate a new bank account"""
         # extract information from customer.txt into a dict
        dict = {}
        dict_string = ""
        dict['ID'] = []
        dict['Name'] = []
        dict['Age'] = []
        dict['Gender']=[]
        dict['Password']=[]
        dict['NationalID']=[]
        with open('customer.txt', 'r') as customer_file:
            for line in customer_file:
                dict_string += line
            dict_list = dict_string.split('\n')
            dict_list.remove('')
            for el in dict_list:
                list_el = el.split()
                dict['ID'].append(list_el[0])
                dict['Name'].append(list_el[1])
                dict['Age'].append(list_el[2])
                dict['Gender'].append(list_el[3])
                dict['Password'].append(list_el[4])
                dict['NationalID'].append(list_el[5])
        # find account name in dict base on provided Customer ID (CID) via ID input when customer signing in
        self.AccountName = dict['Name'][int(self.CID)-1]
        # Define transactionID & AccountNo
        # AccountNo has 9 number which consist of TID as very first numbers and the remaining is randomly generated
        try:
            with open('Account.txt', 'r') as account_file:
                self.TID = len(account_file.readlines()) + 1
                self.AccountNo = (str(self.TID) + str(random.randint(10**7,10**8-1)))[0:10]
        except FileNotFoundError:
            self.TID = 1
            self.AccountNo = str(self.TID) + str(random.randint(10**7,10**8-1))

    def view_account(self):
        """View all accounts of the same Customer ID"""

        dict2_string = ""
        dict2['ACID'] = []
        dict2['CID'] = []
        dict2['Name'] = []
        dict2['Type'] = []
        dict2['BSB']=[]
        dict2['AccountNo']=[]
        dict2['Balance']=[]
        try:
            account_file = open('Account.txt', 'r')
            account_file.close()
        except FileNotFoundError:
            account_file = open('Account.txt', 'a+')
            account_file.close()
        with open('Account.txt', 'r') as account_file:
            for line in account_file:
                dict2_string += line
            dict2_list = dict2_string.split('\n')
            dict2_list.remove('')

            for el in dict2_list:
                list2_el = el.split()
                dict2['ACID'].append(list2_el[0])
                dict2['CID'].append(list2_el[1])
                dict2['Name'].append(list2_el[2])
                dict2['Type'].append(list2_el[3])
                dict2['BSB'].append(list2_el[4])
                dict2['AccountNo'].append(list2_el[5])
                dict2['Balance'].append(list2_el[6])

        dict3['Type'] = []
        dict3['BSB'] = []
        dict3['AccountNo'] =[]
        dict3['Balance']=[]
        dict3['OrderNo']=[]
        dict3['ACID']=[]

        print("{0:-^20s}{1:-^15s}{2:-^15s}{3:-^15s}{4:-^15s}---".format('Select Options', 'Account Type','BSB','AccountNo','Balance'))
        count = 1
        for index,CID in enumerate(dict2['CID']):
            if CID == self.CID:

                dict3['Type'].append(dict2['Type'][index])
                dict3['BSB'].append(dict2['BSB'][index])
                dict3['AccountNo'].append(dict2['AccountNo'][index])
                dict3['Balance'].append(dict2['Balance'][index])
                dict3['OrderNo'].append(count)
                dict3['ACID'].append(dict2['ACID'][index])
                print("{0:^20}{1:^15s}{2:^15s}{3:^15s}{4:^15s}".format(count, dict2['Type'][index], dict2['BSB'][index], dict2['AccountNo'][index], dict2['Balance'][index]))

                count+=1
        return dict2, dict3,count
    def view_transaction(self,option):
        """View transaction history of the same CustomerID(CID) and Account CreationID(ACID)"""
        try:
            transaction_file = open('transaction.txt','r')
            transaction_file.close()
        except FileNotFoundError:
            transaction_file = open('transaction.txt','w')
            print('This is transaction history',file = transaction_file)
            transaction_file.close()
        with open('transaction.txt','r+') as transaction_file:
            dict4_string = ''
            for line in transaction_file:
                dict4_string += line
                dict4_list = dict4_string.split('\n')
                dict4_list.remove('')
                if 'This is transaction history' in dict4_list:
                    dict4_list.remove('This is transaction history')
            print("{0:-^15s}{1:-^15s}{2:-^15s}{3:-^15s}{4:-^15s}{5:-^15s}{6:-^15s}{7:-^15s}{8:-^15s}---".format('TransactionID', 'AccountID','Date','CustomerID','Activity','BSB','AccountNo','Amount','Balance'))
            for el in dict4_list:
                if dict3['ACID'][option -1] == el.split()[1]:

                    el1,el2,el3,el4,el5,el6,el7,el8,el9 = el.split()
                    print("{0:^15s}{1:^15s}{2:^15s}{3:^15s}{4:^15s}{5:^15s}{6:^15s}{7:^15s}{8:^15s}".format(el1,el2,el3,el4,el5,el6,el7,el8,el9))


    def withdraw_transaction_update(self,type,request_amount,select_account):
        """Update withdrawal transactions on transaction.txt and account.txt"""
    # only withdraw within daily limit $100 (balance +withdraw amount <=100) for checking account if balance = 0
    # saving account: only withdraw or transfer once per month
    # transaction.txt: TID,date, CID,type,BSB,AccountNo,amount,balance
        try:
            with open('transaction.txt','r') as transaction_file:
                TID = len(transaction_file.readlines()) + 1
        except FileNotFoundError:
                TID = 1

        with open('transaction.txt','a+') as transaction_file:
            withdraw_amount = request_amount
            CID = self.CID
            ACID = dict3['ACID'][select_account-1]
            BSB = dict3['BSB'][select_account-1]
            AccountNo = dict3['AccountNo'][select_account-1]
            Balance = int(dict3['Balance'][select_account-1]) - withdraw_amount
            transaction_date = date.today()
            print(TID,ACID,transaction_date,CID,type,BSB,AccountNo,withdraw_amount,Balance,file = transaction_file)

            #update account.txt balance: update dict2 then rewrite dict2 on account.txt as the original order
            #TID,CID,AccountName,Type,BSB,AccountNo,Balance
            dict2['Balance'][int(ACID)-1] = Balance
            n = 0
            with open('Account.txt','w') as account_file:
                while True:
                    if n in range (0,len(dict2['ACID'])):
                        print(dict2['ACID'][n],dict2['CID'][n],dict2['Name'][n],dict2['Type'][n],dict2['BSB'][n],dict2['AccountNo'][n],dict2['Balance'][n],file = account_file)
                        n+=1
                    else:
                        break
        print( type +" successfully!")
    def deposit_transaction_update(self,request_amount,select_account):
        """Update deposit transaction on transaction.txt and account.txt """
        try:
            with open('transaction.txt','r') as transaction_file:
                TID = len(transaction_file.readlines()) + 1
        except FileNotFoundError:
                TID = 1
        with open('transaction.txt','a+') as transaction_file:
            deposit_amount = request_amount
            CID = self.CID
            type = "deposit"
            ACID = dict3['ACID'][select_account-1]
            BSB = dict3['BSB'][select_account-1]
            AccountNo = dict3['AccountNo'][select_account-1]
            Balance = int(dict3['Balance'][select_account-1]) + deposit_amount
            transaction_date = date.today()
            print(TID,ACID,transaction_date,CID,type,BSB,AccountNo,deposit_amount,Balance,file = transaction_file)

            #update account.txt balance: update dict2 then rewrite dict2 on account.txt as the original order
            #TID,CID,AccountName,Type,BSB,AccountNo,Balance
            dict2['Balance'][int(ACID)-1] = Balance
            n = 0
            with open('Account.txt','w') as account_file:
                while True:
                    if n in range (0,len(dict2['ACID'])):
                        print(dict2['ACID'][n],dict2['CID'][n],dict2['Name'][n],dict2['Type'][n],dict2['BSB'][n],dict2['AccountNo'][n],dict2['Balance'][n],file = account_file)
                        n+=1
                    else:
                        break
        print("Deposit successfully!")
    def transfer_transaction_update(self,request_amount,transfer_from,transfer_to):
        """Update transfer transaction on account.txt and transaction.txt"""
        try:
            with open('transaction.txt','r') as transaction_file:
                TID = len(transaction_file.readlines()) + 1
        except FileNotFoundError:
                TID = 1
        with open('transaction.txt','a+') as transaction_file:
            transfer_amount = request_amount
            CID = self.CID
            type1 = "transfer-from"
            type2 ='transfer-to'
            ACID1 = dict3['ACID'][transfer_from-1]
            ACID2 = dict3['ACID'][transfer_to-1]
            BSB1 = dict3['BSB'][transfer_from-1]
            BSB2 = dict3['BSB'][transfer_to-1]
            AccountNo1 = dict3['AccountNo'][transfer_from-1]
            AccountNo2 = dict3['AccountNo'][transfer_to-1]
            Balance1 = int(dict3['Balance'][transfer_from-1]) - transfer_amount
            Balance2 = int(dict3['Balance'][transfer_to-1]) + transfer_amount
            transaction_date = date.today()
            print(TID,ACID1,transaction_date,CID,type1,BSB1,AccountNo1,transfer_amount,Balance1,file = transaction_file)
            print(TID+1,ACID2,transaction_date,CID,type2,BSB2,AccountNo2,transfer_amount,Balance2,file = transaction_file)
            #update account.txt balance: update dict2 then rewrite dict2 on account.txt as the original order
            #TID,CID,AccountName,Type,BSB,AccountNo,Balance
            dict2['Balance'][int(ACID1)-1] = Balance1
            dict2['Balance'][int(ACID2)-1] = Balance2
            n = 0
            with open('Account.txt','w') as account_file:
                while True:
                    if n in range (0,len(dict2['ACID'])):
                        print(dict2['ACID'][n],dict2['CID'][n],dict2['Name'][n],dict2['Type'][n],dict2['BSB'][n],dict2['AccountNo'][n],dict2['Balance'][n],file = account_file)
                        n+=1
                    else:
                        break
        print("Transfer successfully!")

    def __str__(self):
        return " TID:{} \n CID:{} \n AccountName:{} \n BSB:{}\n AccountNo:{}\n Balance:{}\n".format(self.TID,self.CID,self.AccountName,self.BSB,self.AccountNo,self.Balance)

class SavingAccount(Bank):
    def __init__(self,CID):
        Bank.__init__(self,CID)
        self.Type = 'SA'

    def create_account(self):
        """Creating saving account"""
        Bank.create_account(self)
        with open('Account.txt', 'a+') as account_file:
            print(self.TID,self.CID,self.AccountName,self.Type,self.BSB,self.AccountNo,self.Balance,file=account_file)

    def withdraw(self,request_amount,select_account):
        """withdraw from a saving account. Transaction is restricted for only once per month, account need balance >o"""
        if dict3['Type'][select_account-1]=='SA':
            # check the account balance
            if int(dict3['Balance'][select_account -1]) <request_amount:
                print('Not enough money in the account')
            # open transaction file and check for transaction history
            # when saving account has balance >=  the amount requested
            # open transaction history and check the past transactions of the relevant account
            else:
                try:
                    transaction_file = open('transaction.txt','r')
                    transaction_file.close()
                except FileNotFoundError:
                    transaction_file = open('transaction.txt','w')
                    print('This is transaction history',file = transaction_file)
                    transaction_file.close()
                with open('transaction.txt','r+') as transaction_file:
                    dict4_string = ''
                    for line in transaction_file:
                        dict4_string += line
                        dict4_list = dict4_string.split('\n')
                        dict4_list.remove('')
                        if 'This is transaction history' in dict4_list:
                            dict4_list.remove('This is transaction history')
                    countloop = 0
                    for el in dict4_list:
                        list4_el = el.split()
                        countloop +=1
                        if list4_el[1] == dict3['ACID'][select_account -1] and  (list4_el[4] in ['withdraw','transfer-from','send']) and  int(list4_el[2].split('-')[1]) == date.today().month and int(list4_el[2].split('-')[0])==date.today().year:
                                print('Request is declined.Withdrawal limit of the month has been reached ')
                                break
                        else:
                            if countloop == len(dict4_list):
                                type = 'withdraw'
                                Bank.withdraw_transaction_update(self,type,request_amount,select_account)
                                break
                    if countloop == 0:
                        type = 'withdraw'
                        Bank.withdraw_transaction_update(self,type,request_amount,select_account)

    def send(self,request_amount,select_account):
        """send money to other person from a saving account"""
        if dict3['Type'][select_account-1]=='SA':
            # check the account balance
            if int(dict3['Balance'][select_account -1]) <request_amount:
                print('Not enough money in the account')
            # open transaction file and check for transaction history
            # when saving account has balance >=  the amount requested
            # open transaction history and check the past transactions of the relevant account
            else:
                try:
                    transaction_file = open('transaction.txt','r')
                    transaction_file.close()
                except FileNotFoundError:
                    transaction_file = open('transaction.txt','w')
                    print('This is transaction history',file = transaction_file)
                    transaction_file.close()
                with open('transaction.txt','r+') as transaction_file:
                    dict4_string = ''
                    for line in transaction_file:
                        dict4_string += line
                        dict4_list = dict4_string.split('\n')
                        dict4_list.remove('')

                        if 'This is transaction history' in dict4_list:
                            dict4_list.remove('This is transaction history')

                    countloop = 0
                    for el in dict4_list:
                        list4_el = el.split()
                        countloop +=1
                        if list4_el[1] == dict3['ACID'][select_account -1] and  (list4_el[4] in ['withdraw','transfer-from','send']) and  int(list4_el[2].split('-')[1]) == date.today().month and int(list4_el[2].split('-')[0])==date.today().year:
                                print('Request is declined.Send limit of the month has been reached ')
                                break
                        else:
                            if countloop == len(dict4_list):
                                type = 'send'
                                Bank.withdraw_transaction_update(self,type,request_amount,select_account)
                                break
                    if countloop == 0:
                        type = 'send'
                        Bank.withdraw_transaction_update(self,type,request_amount,select_account)



    def __str__(self):
        return " TID:{} \n CID:{} \n AccountName:{} \n BSB:{}\n AccountNo:{}\n Balance:{}\n Type:{}\n".format(self.TID,self.CID,self.AccountName,self.BSB,self.AccountNo,self.Balance,self.Type)

class CheckingAccount(Bank):
    def __init__(self,CID):
        Bank.__init__(self,CID)
        self.Type = 'CA'

    def create_account(self):
        """Creating a checking account"""
        Bank.create_account(self)
        with open('Account.txt', 'a+') as account_file:
            print(self.TID,self.CID,self.AccountName,self.Type,self.BSB,self.AccountNo,self.Balance,file=account_file)

    def withdraw(self,request_amount,select_account):
        """Withdraw from a checking account"""
        if  request_amount - int(dict3['Balance'][select_account -1]) >100:
            print('Request is declined.Credit limit has been reached, please top up to avoid fees')
        else:
            type = 'withdraw'
            Bank.withdraw_transaction_update(self,type,request_amount,select_account)

    def send(self,request_amount,select_account):
        """send money from a checking account. Credit limit is $100"""

        if  request_amount - int(dict3['Balance'][select_account -1]) >100:
            print('Request is declined.Credit limit has been reached, please top up to avoid fees')
        else:
            type = 'send'
            Bank.withdraw_transaction_update(self,type,request_amount,select_account)

    def __str__(self):
        return " TID:{} \n CID:{} \n AccountName:{} \n BSB:{}\n AccountNo:{}\n Balance:{}\n Type:{}\n".format(self.TID,self.CID,self.AccountName,self.BSB,self.AccountNo,self.Balance,self.Type)

class Customer(object):
    def __init__(self,Name,Age,Gender,Pass,NationalID):
        self.Name = Name
        self.Age = Age
        self.Gender = Gender
        self.Pass = Pass
        self.ID = 0
        self.NationalID = NationalID
    def register_customer(self):
        """registering a new customer"""
        try: # check if NationalID is exit in customer.txt or not
            with open('customer.txt', 'r') as customer_file:
                self.ID = len(customer_file.readlines()) + 1
        except FileNotFoundError:

            self.ID = 1
        with open('customer.txt', 'a+') as customer_file:
            dict = {}
            dict_string = ""
            dict['NationalID']=[]
            with open('customer.txt', 'r') as customer_file:
                for line in customer_file:
                    dict_string += line
                dict_list = dict_string.split('\n')
                dict_list.remove('')

                for el in dict_list:
                    list_el = el.split()
                    dict['NationalID'].append(list_el[5])

            if str(self.NationalID) in dict['NationalID']:
                print('You arealdy registered with CatBank.Please sign in with your ID and password')
            else:
                with open('customer.txt', 'a+') as customer_file:
                    print(self.ID,self.Name,self.Age,self.Gender,self.Pass,self.NationalID,file=customer_file)
                    print('Your userID is:',self.ID)
                    print('Register successful')
    def sign_in(self,IDinput,passinput):
        """sigining in a customer with provided ID and password"""
        # extract details from customer.txt to validate ID and password
        dict = {}
        dict_string = ""
        dict['ID'] = []
        dict['Name']=[]
        dict['Password']=[]
        dict['Age']=[]
        #avoiding FileNotFoundError
        try:
            customer_file = open('customer.txt', 'r')
            customer_file.close()
        except FileNotFoundError:
            customer_file = open('customer.txt','a+')
            customer_file.close()
        with open('customer.txt', 'r') as customer_file:
            for line in customer_file:
                dict_string += line
            dict_list = dict_string.split('\n')
            dict_list.remove('')
            for el in dict_list:
                list_el = el.split()
                dict['ID'].append(list_el[0])
                dict['Name'].append(list_el[1])
                dict['Age'].append(list_el[2])
                dict['Password'].append(list_el[4])
        if IDinput in dict['ID']: # ID found
            if passinput == dict["Password"][int(IDinput)-1]: #password found
                print("Wellcome "+dict["Name"][int(IDinput)-1].split('-')[0]+". Login successful!") # successful login
                while True: # bank functions start: list of options
                    prompt2 = input("PLEASE SELECT OPTIONS:""\n""1.Open a new account""\n""2.View your account""\n""3.Make a deposit""\n""4.Withdraw""\n""5.Transfer""\n""6.Send money""\n""7.Quit""\n")
                    if prompt2 == str(1):

                        if int(dict["Age"][int(IDinput)-1]) > 18: #If customer age is > 18, eligible to open either saving or check accounts
                            while True: # options to either open saving or checking account
                                prompt3 = input("PLEASE CHOOSE TYPE OF ACCOUNT:""\n""1.Checking Account""\n""2.Savings Account""\n""3.Quit""\n")
                                if prompt3 == str(1):
                                    while True: # checking account condition - seeking consent from customer to proceed
                                        prompt4 = input("Checking account has a credit limit and overdraft fees of $5 each transaction, interest rate = 0. Happy to proceed?(Y/N):")
                                        if prompt4 == "N" or prompt4 == 'n':
                                            print("Returning to the main screen")
                                            break
                                        elif prompt4 =="Y" or prompt4=='y': # create new checking account under the customer ID
                                            CID = IDinput
                                            customer1 = CheckingAccount(CID) # Call to Checking Account class
                                            customer1.create_account() # inherited functions of Bank class - parent of Checking Account
                                            print("Your checking account is successfully created!")
                                            break

                                elif prompt3 == str(2): # customer select to open saving account
                                    while True: # saving account condition. seek for customer consent
                                        prompt5 = input("Savings account pays 4% interest annually and you are only allowed to withdraw or transfer once per month. Happy to procceed?(Y/N):")
                                        if prompt5 == "Y" or prompt5 =='y': # create a saving account under customer ID

                                            CID = IDinput
                                            customer1 = SavingAccount(CID)
                                            customer1.create_account()
                                            print("Your savings account is successfully created!")
                                            break
                                        elif prompt5 == "N" or prompt5=='n':
                                            print("Returning to the main screen")
                                            break
                                        else:
                                            print("Please enter again")
                                else:
                                    break

                        elif int(dict["Age"][int(IDinput)-1]) in range (14,19): # if cutomer age is greater than 14 but less than or equal 18
                            while True: # let customer know the bank's age restriction. Seek for consent to create saving account only
                                prompt6 = input("Since you are over 14 year old and under 18 year old, you can only open Savings Account. Happy to procceed? (Y/N):")
                                if prompt6 == 'Y' or prompt6 == 'y':

                                    while True: # seeking consent on saving account conditions
                                        prompt5 = input("Savings account pays 4% interest annually and you are only allowed to withdraw or transfer once per month. Happy to procceed?(Y/N):")
                                        if prompt5 == 'Y' or prompt5 =='y': # customer said yes, creating a saving account
                                            CID = IDinput
                                            account1 = SavingAccount(CID)
                                            account1.create_account()
                                            print("Your savings account is successfully created!")
                                            break
                                        elif prompt5 == 'N' or prompt5 == 'n':
                                            print("returning to the main screen")
                                            break

                                        else: # if customer entering anything but Y or N
                                            print('value entered is not valid.Please try again')
                                    break
                                elif prompt6 =='N'or prompt6 =='n':
                                    break
                                else:
                                    print('value entered is not valid.Please try again')

                        else: # customer age does not meet minimum threshold to create an account
                            print("You need to be over 14 year old to open a bank account under your name.Please contact CATBANK for more information.")
                    elif prompt2 == str(2): # view bank account and their transaction history
                        CID = IDinput
                        account1 = Bank(CID)
                        account1.view_account() # view bank accounts
                        while True: # from the list of viewed accounts, select one to view transaction history
                            try:
                                option = int(input('Select account you want to view or press any key to quit:'))
                                if option in dict3['OrderNo']:
                                    account1.view_transaction(option)
                            except ValueError:
                                break
                    elif prompt2 == str(3):# deposit money

                        CID=IDinput
                        account1=Bank(CID)
                        account1.view_account() # view account to select which account to deposit to
                        if len(dict3['OrderNo']) > 0: # if there is account(s) created under provided customer ID
                            while True:
                                try:
                                    select_account = int(input('please select which account you want to deposit to:'))
                                    if select_account in dict3['OrderNo']: # check if the selection is on the viewed account list
                                        while True:
                                            try:
                                                request_amount = int(input ('how much you want to deposit  :'))
                                                # deposit money and update on transaction.txt and account.txt
                                                CID = IDinput
                                                account1=Bank(CID)
                                                account1.deposit_transaction_update(request_amount,select_account)
                                                break
                                            except ValueError:
                                                print('the value entered is invalid. Try again')
                                        break

                                    else:
                                        print('selection is not in the list. Please try again!')
                                except ValueError: # if customer entered a value not an integer
                                    answer_to = input('Do you want to quit?(Y/N):') # customer may want to quit
                                    if answer_to == 'Y'or answer_to =='y':
                                        break
                        else: # if there is no account recorded under provided customer ID
                            print('No account available to deposit')


                    elif prompt2 == str(4): # withdraw function
                        # view accounts under the same provided Customer ID to see which one to withdraw
                        CID=IDinput
                        account1=Bank(CID)
                        account1.view_account()

                        if len(dict3['OrderNo']) > 0: # if at least one account exist
                            while True:
                                try: # prompt customer to select one of the account on the list to withdraw from
                                    select_account = int(input('please select which account you want to withdraw:'))
                                    if select_account in dict3['OrderNo']: # check if selection is on the list
                                        request_amount = int(input ('how much you want to withdraw  :'))
                                        if dict3['Type'][select_account-1]=='CA': #check if the account is checking account
                                            CID = IDinput
                                            account1=CheckingAccount(CID) # call CheckingAccount class and its function
                                            account1.withdraw(request_amount,select_account)
                                            break
                                        else: # if the selected account is saving account
                                            CID = IDinput
                                            account1=SavingAccount(CID) # call SavingAccount class and its function
                                            account1.withdraw(request_amount,select_account)
                                            break
                                    else: # selection is not on the list
                                        print('selection is not in the list. Please try again!')
                                except ValueError: # customer entered something other than an integer
                                    answer_to = input('Do you want to quit?(Y/N):') # customer might want to exit?
                                    if answer_to == 'Y'or answer_to =='y':
                                        break
                        else:
                            print('No account available to withdraw')

                    elif prompt2 == str(5):# transfer to other account under the same customer ID
                        # view all account to perform transfer
                        CID = IDinput
                        account1 = Bank(CID)
                        account1.view_account()
                        while True: # select transfer to and from accounts
                            try:
                                transfer_from = int(input('Please select account you want to transfer from:'))
                                if transfer_from in dict3['OrderNo']: # if selected transfer-from account is on the list

                                    if int(dict3['Balance'][transfer_from-1]) > 0: # balance must be >0 to continue
                                        while True:
                                            try:
                                                request_amount = int(input('How much you want to transfer:'))
                                                # transfering amount must not exceed current account balance to continue
                                                if request_amount <= int(dict3['Balance'][transfer_from-1]):
                                                    account1.view_account() # view accounts once more to select transfer-to account
                                                    while True:
                                                        transfer_to = int(input('Please select account you want to transfer to:'))
                                                        if transfer_to in dict3['OrderNo']:# check if account is on the list
                                                            # calling function of Bank class to perform transfer transaction
                                                            account1.transfer_transaction_update(request_amount,transfer_from,transfer_to)
                                                            break
                                                        else: # customer entered something out of the list
                                                            print('selection is not in the list')
                                                            answer_to = input('Do you want to cancel transaction?(Y/N):')
                                                            if answer_to == 'Y' or answer_to =='y':
                                                                break
                                                    break
                                                else: # transfering amount exceed current balance
                                                    print('Not enough money to transfer')


                                            except ValueError: # in case customer entered something else rather than amount of money to transfer
                                                print('invalid amount, try again')
                                                answer_to = input('Do you want to cancel transaction?(Y/N):')
                                                if answer_to == 'Y' or answer_to =='y':
                                                    break
                                    else: # transfering amount is greater than current balance
                                        print('Not enough money to transfer')
                                else: # in case customer entered something else not on the list
                                    print('selection is not in the list, try again')
                                    answer_to = input('Do you want to cancel transaction?(Y/N):')
                                    if answer_to == 'Y' or answer_to =='y':
                                        break
                            except ValueError:
                                print('invalid entry. Please try again')
                                answer_to = input('Do you want to cancel transaction?(Y/N):')
                                if answer_to == 'Y' or answer_to =='y':
                                    break
                    elif prompt2 ==str(6):# send money to other person
                        # view all accounts
                        CID=IDinput
                        account1=Bank(CID)
                        account1.view_account()
                        if len(dict3['OrderNo']) > 0:# check if at least one account recorded under provided ID
                            while True: # select an account from the above list
                                try:
                                    select_account = int(input('please select which account you want to send money:'))
                                    if select_account in dict3['OrderNo']:
                                        request_amount = int(input ('how much you want to send:'))
                                        if dict3['Type'][select_account-1]=='CA':
                                            # the selected account is checking account
                                            print('Please enter details of recipient:')
                                            while True: # recepient's details need to be entered before continue
                                                try:
                                                    RBSB = int(input('BSB:'))
                                                    RAccountNo =int(input('AccountNo:'))
                                                    RName =str(input('Account Name:'))
                                                    Reference =str(input('Reference:'))
                                                    if len(RBSB) == 6 and len(RAccountNo)==9: # check for length of BSB and AccountNo
                                                        CID = IDinput
                                                        account1=CheckingAccount(CID)
                                                        account1.send(request_amount,select_account)
                                                        break
                                                    else:
                                                        print('BSB or Account Number has incorrect length.Check again!')

                                                    break
                                                except ValueError:
                                                    print('Values entered are invalid. Try again!')

                                            break
                                        else: # the selected account is ssaving account
                                            CID = IDinput
                                            account1=SavingAccount(CID)
                                            account1.send(request_amount,select_account)

                                    else:
                                        print('selection is not in the list. Please try again!')
                                except ValueError:
                                    answer_to = input('Do you want to quit?(Y/N):')
                                    if answer_to == 'Y'or answer_to =='y':
                                        break
                        else:
                            print('No account available to send money')
                            break
                    else:
                        print("See you again!")
                        break

            else: # Password is not found in customer.txt file
                print("Please try again!Pass is incorrect")
        else: # ID provided is not found in customer.txt file
            print("You have not registed with KatBank. Please register first!")
    def __str__(self):
        return " ID:{} \n Name:{} \n Age:{} \n Gender:{}\n Password:{}\n NationalID:{}\n ".format(self.ID,self.Age,self.Gender,self.Pass,self.NationalID)

# main code:
while True:
    # prompt user a list of options to choose from
    prompt1 = input("WELLCOME TO KATBANK!! PLEASE SELECT OPTIONS:""\n""1. Register""\n""2. Sign In""\n""3. Quit Program""\n")
    if prompt1 == str(1): # register a new account
        dict = {}
        while True:
            try:
                FName = str(input("First Name: "))
                LName = str(input("Last Name:"))
                NationalID = int(input('Your national identity number(9 digit):'))
                Age = int(input("Age: "))
                Gender = str(input("Gender(M/F): "))
                Pass = input("Password: ")
                FName = FName.split()[0] # take the first name if first name input has space in between
                LName = LName.split()[-1] # take the last name if last name input has space in between
                Name = FName +'-'+LName # name to be recorded on customer.txt
                if Gender in ['M','m','F','f']:
                    customer1 = Customer(Name,Age,Gender,Pass,NationalID)
                    customer1.register_customer()
                else:
                    print('mistake made at entering value for Gender')

                break
            except ValueError:
                print('Value entered is invalid.Please try again')

    elif prompt1 == str(2): # sign in by entering ID and password
        IDinput = input("ID: ")
        passinput = input("Password: ")
        dict2={}
        dict3={}
        count = 1
        ID = IDinput
        Name = ""
        Age = ""
        Gender = ""
        Pass = 0
        NationalID =0
        customer1=Customer(Name,Age,Gender,Pass,NationalID)
        customer1.sign_in(IDinput,passinput)

    else:
        break

