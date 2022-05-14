# # register customer
def register_customer():
    with open('FINAL CA/customer.txt', 'r') as customer_file:

        ID = len(customer_file.readlines()) + 1
        Name = input("Name: ")
        Age = input("Age: ")
        Gender = input("Gender: ")
        Pass = input("Password: ")
        customer_file = open('FINAL CA/customer.txt', 'a')
        print(ID,Name,Age,Gender,Pass,file=customer_file)
        customer_file.close()



# turn the text file into a dictionary of customer details:
def customer_dict():
    dict_string = ""
    dict['ID'] = []
    dict['Name'] = []
    dict['Age'] = []
    dict['Gender']=[]
    dict['Password']=[]
    with open('FINAL CA/customer.txt', 'r') as customer_file:
        for line in customer_file:
            dict_string += line
        dict_list = dict_string.split('\n')
        dict_list.remove('')
        print(dict_list)
        for el in dict_list:
            list_el = el.split()
            dict['ID'].append(list_el[0])
            dict['Name'].append(list_el[1])
            dict['Age'].append(list_el[2])
            dict['Gender'].append(list_el[3])
            dict['Password'].append(list_el[4])
        print(dict)
# # customer log-in
# with open('customer.txt','r') as customer_file:
#     for index,line in enumerate(customer_file):
#         if index = int(log_in_ID) :
#             print("Log in successful, please continue")
#         else:


# main code
while True:
    # prompt user a list of options to choose
    prompt = input("WELLCOME TO KATBANK!! PLEASE SELECT OPTIONS:""\n""1. Register""\n""2. Sign In""\n""3. Quit Program""\n")
    if prompt == str(1):
        register_customer()
        continue
    if prompt == str(2):
        dict = {}
        customer_dict()
        #LOG-IN FUNCTION
        ID = input("ID: ")
        Password = input("Password: ")
        if ID in dict['ID']:
            if Password == dict["Password"][int(ID)-1]:
                print("Wellcome. Login successful!")
            else:
                print("Please try again!Pass is incorrect")
        else:
            print("user id is not exist")
    else:
        break




