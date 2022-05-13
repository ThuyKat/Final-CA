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
         # extract information from customer.txt into a dict
        dict = {}
        dict_string = ""
        dict['ID'] = []
        dict['Name'] = []
        dict['Age'] = []
        dict['Gender']=[]
        dict['Password']=[]
        with open('customer.txt', 'r') as customer_file:
            for line in customer_file:
                dict_string += line
            dict_list = dict_string.split('\n')
            dict_list.remove('')
            # print(dict_list)
            for el in dict_list:
                list_el = el.split()
                dict['ID'].append(list_el[0])
                dict['Name'].append(list_el[1])
                dict['Age'].append(list_el[2])
                dict['Gender'].append(list_el[3])
                dict['Password'].append(list_el[4])
        # find account name in dict
        self.AccountName = dict['Name'][int(ID)-1]
        # Define transactionID & AccountNo
        try:
            with open('Account.txt', 'r') as account_file:
                self.TID = len(account_file.readlines()) + 1
                self.AccountNo = str(self.TID) + str(random.randint(10**7,10**8-1))
        except FileNotFoundError:
            self.TID = 1
            self.AccountNo = str(self.TID) + str(random.randint(10**7,10**8-1))

    def view_account(self):

        dict2_string = ""
        dict2['ACID'] = []
        dict2['CID'] = []
        dict2['Name'] = []
        dict2['Type'] = []
        dict2['BSB']=[]
        dict2['AccountNo']=[]
        dict2['Balance']=[]
        with open('Account.txt', 'r') as account_file:
            for line in account_file:
                dict2_string += line
            dict2_list = dict2_string.split('\n')
            dict2_list.remove('')
            # print(dict_list)
            for el in dict2_list:
                list2_el = el.split()
                dict2['ACID'].append(list2_el[0])
                dict2['CID'].append(list2_el[1])
                dict2['Name'].append(list2_el[2])
                dict2['Type'].append(list2_el[3])
                dict2['BSB'].append(list2_el[4])
                dict2['AccountNo'].append(list2_el[5])
                dict2['Balance'].append(list2_el[6])
        count = 1
        dict3['Type'] = []
        dict3['BSB'] = []
        dict3['AccountNo'] =[]
        dict3['Balance']=[]
        dict3['OrderNo']=[]
        dict3['ACID']=[]

        for index,CID in enumerate(dict2['CID']):
            if CID == self.CID:
                dict3['Type'].append(dict2['Type'][index])
                dict3['BSB'].append(dict2['BSB'][index])
                dict3['AccountNo'].append(dict2['AccountNo'][index])
                dict3['Balance'].append(dict2['Balance'][index])
                dict3['OrderNo'].append(count)
                dict3['ACID'].append(dict2['ACID'][index])
                print(count,' Type:',dict2['Type'][index],' BSB:',dict2['BSB'][index],' Account number:',dict2['AccountNo'][index],' Balance:',dict2['Balance'][index],'\n')
                count+=1
        return dict2, dict3

    def withdraw_transaction_update(self,request_amount,select_account):
    # only withdraw within daily limit $100 (balance +withdraw amount <=100) for checking account if balance = 0
    # saving account: only withdraw or transfer once per month
    # transaction.txt: TID,date, CID,type,BSB,AccountNo,amount,balance
        with open('transaction.txt','a+') as transaction_file:
            TID = len(transaction_file.readlines()) + 1
            withdraw_amount = request_amount
            CID = ID
            type = "withdraw"
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
        print("Withdraw successfully!")

    def __str__(self):
        return " TID:{} \n CID:{} \n AccountName:{} \n BSB:{}\n AccountNo:{}\n Balance:{}\n".format(self.TID,self.CID,self.AccountName,self.BSB,self.AccountNo,self.Balance)

class SavingAccount(Bank):
    def __init__(self,CID):
        Bank.__init__(self,CID)
        self.Type = 'SA'

    def create_account(self):
        Bank.create_account(self)
        with open('Account.txt', 'a+') as account_file:
            print(self.TID,self.CID,self.AccountName,self.Type,self.BSB,self.AccountNo,self.Balance,file=account_file)

    def withdraw(self,request_amount,select_account):
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
                        dict4_list.remove('This is transaction history')
                    countloop = 0
                    for el in dict4_list:
                        list4_el = el.split()
                        countloop +=1
                        if list4_el[1] == dict3['ACID'][select_account -1] and  list4_el[4] =='withdraw' and  int(list4_el[2].split('-')[1]) == date.today().month and int(list4_el[2].split('-')[0])==date.today().year:
                                print('Request is declined.Withdrawal limit of the month has been reached ')
                                break
                        else:
                            if countloop == len(dict4_list):
                                Bank.withdraw_transaction_update(self,request_amount,select_account)
                                break

    def __str__(self):
        return " TID:{} \n CID:{} \n AccountName:{} \n BSB:{}\n AccountNo:{}\n Balance:{}\n Type:{}\n".format(self.TID,self.CID,self.AccountName,self.BSB,self.AccountNo,self.Balance,self.Type)

class CheckingAccount(Bank):
    def __init__(self,CID):
        Bank.__init__(self,CID)
        self.Type = 'CA'

    def create_account(self):
        Bank.create_account(self)
        with open('Account.txt', 'a+') as account_file:
            print(self.TID,self.CID,self.AccountName,self.Type,self.BSB,self.AccountNo,self.Balance,file=account_file)

    def withdraw(self,request_amount,select_account):

        if  request_amount - int(dict3['Balance'][select_account -1]) >100:
            print('Request is declined.Credit limit has been reached, please top up to avoid fees')
        else:
            Bank.withdraw_transaction_update(self,request_amount,select_account)

    def __str__(self):
        return " TID:{} \n CID:{} \n AccountName:{} \n BSB:{}\n AccountNo:{}\n Balance:{}\n Type:{}\n".format(self.TID,self.CID,self.AccountName,self.BSB,self.AccountNo,self.Balance,self.Type)

class Customer(object):
    def __init__(self,Name="",Age=0,Gender="",Pass=""):
        self.Name = Name
        self.Age = Age
        self.Gender = Gender
        self.Pass = Pass
        self.ID = 0
    def register_customer(self):
        try:
            with open('customer.txt', 'r') as customer_file:
                self.ID = len(customer_file.readlines()) + 1
        except FileNotFoundError:

            self.ID = 1
        with open('customer.txt', 'a+') as customer_file:
            print(self.ID,self.Name,self.Age,self.Gender,self.Pass,file=customer_file)

    def sign_in(self,IDinput,passinput):
        dict = {}
        dict_string = ""
        dict['ID'] = []
        dict['Name'] = []
        dict['Age'] = []
        dict['Gender']=[]
        dict['Password']=[]
        with open('customer.txt', 'r') as customer_file:
            for line in customer_file:
                dict_string += line
            dict_list = dict_string.split('\n')
            dict_list.remove('')
            # print(dict_list)
            for el in dict_list:
                list_el = el.split()
                dict['ID'].append(list_el[0])
                dict['Name'].append(list_el[1])
                dict['Age'].append(list_el[2])
                dict['Gender'].append(list_el[3])
                dict['Password'].append(list_el[4])
            # print(dict)
        if IDinput in dict['ID']:
            if passinput == dict["Password"][int(IDinput)-1]:
                print("Wellcome "+dict["Name"][int(IDinput)-1]+". Login successful!")
                while True:
                    prompt2 = input("PLEASE SELECT OPTIONS:""\n""1.Open a new account""\n""2.View your account""\n""3.Make a deposit""\n""4.Withdraw""\n""5.Transfer""\n""6.Quit""\n")
                    if prompt2 == str(1):
                        if int(dict["Age"][int(IDinput)-1]) > 18:
                            while True:
                                prompt3 = input("PLEASE CHOOSE TYPE OF ACCOUNT:""\n""1.Checking Account""\n""2.Savings Account""\n""3.Quit""\n")
                                if prompt3 == str(1):
                                    while True:
                                        prompt4 = input("Checking account has daily credit limit and overdraft fees of $5 each transaction, interest rate = 0. Happy to procceed?(Y/N):")
                                        if prompt4 == "N":
                                            print("Returning to the main screen")
                                            break
                                        elif prompt4 =="Y":
                                            # print("create checking account. Function?")
                                            CID = IDinput
                                            customer1 = CheckingAccount(CID)
                                            customer1.create_account()
                                            print("Your checking account is successfully created!")
                                            break
                                        else:
                                            continue

                                elif prompt3 == str(2):
                                    while True:
                                        prompt5 = input("Savings account pays 4% interest annually and you are only allowed to withdraw or transfer once per month. Happy to procceed?(Y/N):")
                                        if prompt5 == "Y":
                                            # print("create saving account. Function?")
                                            CID = IDinput
                                            customer1 = SavingAccount(CID)
                                            customer1.create_account()
                                            print("Your savings account is successfully created!")
                                            break
                                        elif prompt5 == "N":
                                            print("Returning to the main screen")
                                            break
                                        else:
                                            print("Please enter again")
                                            continue


                                else:
                                    break

                        elif int(dict["Age"][int(IDinput)-1]) in range (14,19):
                            while True:
                                prompt6= input("Since you are over 14 year old and under 18 year old, you can only open Savings Account. Happy to procceed? (Y/N):")
                                if prompt6 == "Y":
                                    while True:
                                        prompt5 = input("Savings account pays 4% interest annually and you are only allowed to withdraw or transfer once per month. Happy to procceed?(Y/N):")

                                        if prompt5 == "Y":
                                            # print("create saving account. Function?")
                                            CID = IDinput
                                            account1 = SavingAccount(CID)
                                            account1.create_account()
                                            print("Your savings account is successfully created!")
                                            break


                                        elif prompt5 == "N":
                                            print("returning to the main screen")
                                            break
                                        else:
                                            print('value entered is not valid.Please try again')
                                    break

                                elif prompt6 =="N":
                                    break
                                else:
                                    print('value entered is not valid.Please try again')
                        else:
                            print("You need to be over 14 year old to open a bank account under your name.Please contact CATBANK for more information. ")
                    elif prompt2 == str(2): # view bank account
                        CID = IDinput
                        account1 = Bank(CID)
                        account1.view_account()
                    elif prompt2 == str(3):
                        print("Function for Deposit goes here!")
                        # Bank.deposit()
                    elif prompt2 == str(4): # withdraw
                        CID=IDinput
                        account1=Bank(CID)
                        account1.view_account()
                        while True:
                            select_account = int(input('please select which account you want to withdraw:'))
                            if int(select_account) in dict3['OrderNo']:
                                request_amount = int(input ('how much you want to withdraw  :'))
                                if dict3['Type'][select_account-1]=='CA':
                                    CID = IDinput
                                    account1=CheckingAccount(CID)
                                    account1.withdraw(request_amount,select_account)
                                    break
                                else:
                                    CID = IDinput
                                    account1=SavingAccount(CID)
                                    account1.withdraw(request_amount,select_account)
                                    break
                            else:
                                print('selection is not in the list. Please try again!')
                    elif prompt2 == str(5):
                        print("Function for Transfer goes here!")
                        #Bank.transfer()
                    else:
                        print("See you again!")
                        break

            else:
                print("Please try again!Pass is incorrect")
        else:
            print("user id is not exist")

# main code:
while True:
    # prompt user a list of options to choose from
    prompt1 = input("WELLCOME TO KATBANK!! PLEASE SELECT OPTIONS:""\n""1. Register""\n""2. Sign In""\n""3. Quit Program""\n")
    if prompt1 == str(1):
        Name = input("Name: ")
        Age = int(input("Age: "))
        Gender = input("Gender: ")
        Pass = input("Password: ")
        customer1 = Customer(Name,Age,Gender,Pass)
        customer1.register_customer()

    elif prompt1 == str(2):
        IDinput = input("ID: ")
        passinput = input("Password: ")
        dict2={}
        dict3={}
        ID = IDinput
        customer1=Customer()
        customer1.sign_in(IDinput,passinput)

    else:
        break

