from datetime import date
def view_account():
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
        if CID == ID:
            dict3['Type'].append(dict2['Type'][index])
            dict3['BSB'].append(dict2['BSB'][index])
            dict3['AccountNo'].append(dict2['AccountNo'][index])
            dict3['Balance'].append(dict2['Balance'][index])
            dict3['OrderNo'].append(count)
            dict3['ACID'].append(dict2['ACID'][index])
            print(count,' Type:',dict2['Type'][index],' BSB:',dict2['BSB'][index],' Account number:',dict2['AccountNo'][index],' Balance:',dict2['Balance'][index],'\n')
            count+=1
    return dict2, dict3


def withdraw():
    # the withdrawal function starts here
    # only withdraw within daily limit $100 (balance +withdraw amount <=100) for checking account if balance = 0
    # saving account: only withdraw or transfer once per month
    # transaction.txt: TID,date, CID,type,BSB,AccountNo,amount,balance
    # pushing this comment as git hub test

    view_account()
    select_account = int(input('please select which account you want to withdraw:  '))
    if int(select_account) in dict3['OrderNo']:
        transaction_date = date.today()
        request_amount = int(input ('how much you want to withdraw  :'))

        if dict3['Type'][select_account-1]=='SA':

            # check the account balance

            if int(dict3['Balance'][select_account -1]) <request_amount:
                print('Not enough money in the account')
            # open transaction file and check for transaction history
            #when saving account has balance >=  the amount requested
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
                        print(list4_el)
                        print(list4_el[1])
                        print(dict3['ACID'][select_account -1])
                        print(list4_el[4])
                        print(int(list4_el[2].split('-')[1]))
                        print(date.today().month)
                        print(int(list4_el[2].split('-')[0]))
                        print(date.today().year)
                        countloop +=1
                        print(countloop)

                        if list4_el[1] == dict3['ACID'][select_account -1] and  list4_el[4] =='withdraw' and  int(list4_el[2].split('-')[1]) == date.today().month and int(list4_el[2].split('-')[0])==date.today().year:
                                print('Request is declined.Withdrawal limit of the month has been reached ')
                                break
                        else:
                            if countloop == len(dict4_list):
                                with open('transaction.txt','a+') as transaction_file:
                                    TID = len(transaction_file.readlines()) + 1
                                    withdraw_amount = request_amount
                                    CID = ID
                                    type = "withdraw"
                                    ACID = dict3['ACID'][select_account-1]
                                    BSB = dict3['BSB'][select_account-1]
                                    AccountNo = dict3['AccountNo'][select_account-1]
                                    Balance = int(dict3['Balance'][select_account-1]) - withdraw_amount

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
                                break


        else:
            if  request_amount - int(dict3['Balance'][select_account -1]) >100:
                print('Request is declined.Credit limit has been reached, please top up to avoid fees')
            else:
                with open('transaction.txt','a+') as transaction_file:
                    TID = len(transaction_file.readlines()) + 1
                    withdraw_amount = request_amount
                    CID = ID
                    type = "withdraw"
                    ACID = dict3['ACID'][select_account-1]
                    BSB = dict3['BSB'][select_account-1]
                    AccountNo = dict3['AccountNo'][select_account-1]
                    Balance = int(dict3['Balance'][select_account-1]) - withdraw_amount
                    CreationOrder = int(ACID)
                    print(TID,ACID,transaction_date,CID,type,BSB,AccountNo,withdraw_amount,Balance,file = transaction_file)

                    #update account.txt balance: update dict2 then rewrite dict2 on account.txt as the original order
                    #TID,CID,AccountName,Type,BSB,AccountNo,Balance
                    dict2['Balance'][CreationOrder -1] = Balance
                    n = 0
                    with open('Account.txt','w') as account_file:
                        while True:
                            if n in range (0,len(dict2['ACID'])):
                                print(dict2['ACID'][n],dict2['CID'][n],dict2['Name'][n],dict2['Type'][n],dict2['BSB'][n],dict2['AccountNo'][n],dict2['Balance'][n],file = account_file)
                                n+=1
                            else:
                                break
                    print("Withdraw successfully!")
    else:
        print('selection is not in the list. Please try again!')
        withdraw()

dict2={}
dict3={}
ID = input('ID:')
withdraw()





