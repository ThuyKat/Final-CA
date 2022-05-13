with open('transaction.txt','r+') as transaction_file:
    dict4_string = ''
    for line in transaction_file:
        dict4_string += line
        dict4_list = dict4_string.split('\n')
        dict4_list.remove('')
        dict4_list.remove('This is transaction history')
    print(dict4_list)
