from datetime import date
import random
class Bank(object):
    def __init__(self, TID =0 ,CID="" ,AccountName="" ,Type="" ,BSB="" ,AccountNo="" ,Balance=0):
        self.TID = TID
        self.CID = CID
        self.AccountName = AccountName
        self.Type = Type
        self.BSB = BSB
        self.AccountNo = AccountNo
        self.Balance = Balance
    def create_account(self):
        self.Type = "CA"
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
        self.AccountName = dict['Name'][int(CID)-1]
        # Define transactionID & AccountNo
        try:
            with open('Account.txt', 'r') as account_file:
                self.TID = len(account_file.readlines()) + 1
                self.AccountNo = str(self.TID) + str(random.randint(10**7,10**8-1))
        except FileNotFoundError:
            self.TID = 1
            self.AccountNo = str(self.TID) + str(random.randint(10**7,10**8-1))
        # add to the account_file all information
        with open('Account.txt', 'a+') as account_file:

            print(self.TID,self.CID,self.AccountName,self.Type,self.BSB,self.AccountNo,self.Balance,file=account_file)
            print("the new Checking account has been added")

    def view_account():
        dict_string = ""
        dict2['TID'] = []
        dict2['CID'] = []
        dict2['Name'] = []
        dict2['Type'] = []
        dict2['BSB']=[]
        dict2['AccountNo']=[]
        dict2['Balance']=[]
        with open('Account.txt', 'r') as account_file:
            for line in account_file:
                dict_string += line
            dict_list = dict_string.split('\n')
            dict_list.remove('')
            # print(dict_list)
            for el in dict_list:
                list_el = el.split()
                dict2['TID'].append(list_el[0])
                dict2['CID'].append(list_el[1])
                dict2['Name'].append(list_el[2])
                dict2['Type'].append(list_el[3])
                dict2['BSB'].append(list_el[4])
                dict2['AccountNo'].append(list_el[5])
                dict2['Balance'].append(list_el[6])
        count = 1
        dict3['Type'] = []
        dict3['BSB'] = []
        dict3['AccountNo'] =[]
        dict3['Balance']=[]
        dict3['OrderNo']=[]
        dict3['TID']=[]

        for index,CID in enumerate(dict2['CID']):
            if CID == ID:
                dict3['Type'].append(dict2['Type'][index])
                dict3['BSB'].append(dict2['BSB'][index])
                dict3['AccountNo'].append(dict2['AccountNo'][index])
                dict3['Balance'].append(dict2['Balance'][index])
                dict3['OrderNo'].append(count)
                dict3['TID'].append(dict2['TID'][index])
                print(count,' Type:',dict2['Type'][index],' BSB:',dict2['BSB'][index],' Account number:',dict2['AccountNo'][index],' Balance:',dict2['Balance'][index],'\n')
                count+=1
        return dict2, dict3


#MAIN CODE
#create account
# def create_account():
CID = input('ID:')
BSB = "123-456"
TID = 0
AccountName = ""
Type = ""
AccountNo = ""
Balance = 0
customer1 = Bank(TID,CID,AccountName,Type,BSB,AccountNo,Balance)
# customer1.create_account()
# view account
# def view():
dict2={}
dict3={}
ID = CID
Bank.view_account()
