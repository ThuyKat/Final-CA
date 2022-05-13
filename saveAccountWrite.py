# function to create a new account with customer ID, BSB, account no, account name, transaction ID and save it to txt file
import random
def create_saving_account():
    # define customerID and BSB
    CustomerID = input("ID:")
    BSB = "123-456"
    Type = "SA"
    Balance = 0
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
    AccountName = dict['Name'][int(CustomerID)-1]
    # define transaction ID and account number
    try:
        with open('Account.txt', 'r') as account_file:
            TransactionID = len(account_file.readlines()) + 1
            AccountNo = str(TransactionID) + str(random.randint(10**7,10**8-1))
    except FileNotFoundError:
            TransactionID = 1
            AccountNo = str(TransactionID) + str(random.randint(10**7,10**8-1))
    # add to the account_file all information
    with open('Account.txt', 'a+') as account_file:
        print(TransactionID,CustomerID,AccountName,Type,BSB,AccountNo,Balance,file=account_file)
        print("the new Saving account has been added")
# execute funtion:
create_saving_account()

