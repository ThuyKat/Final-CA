# when a user gives us a set of keywords, find the documents in this collection  match their search terms.
#  read in the documents from the file and number each document starting with 1
# use a dictionary to look up search terms  appear in each document.
# Each entry in your dictionary should have a word as the key
# and the word’s value as the set of document numbers that this word appears in
# to look up a keyword in the dictionary and immediately get all the documents that it appears in
# your program has read the file
# prompt the user to do one of three things:
# 1)search for documents that match the search words input by the user,
#     If the user chooses to search, your program should prompt for a
#     string of search words and find documents that contain all those keywords.
#     It will then print out the document number of all the relevant documents.
#      If no documents in the collection your program should print a message no relevant documents were found.
# 2) display a document,
#     your program should prompt for a document number
#     and print out the entire document that corresponds to that number
# or 3) quit the program.
#     Your program should continue to prompt until the user chooses to quit.
#
# 1. You will likely need to store two types of data in two different data structures.
    # In one,you will have a dictionary that stores single words as the key with the value as the
    # set of documents (numbers) that the word appears in.
    # In the other data structure, you will store the actual text of the documents,
    # so that you can display it for the user when they ask.use a list or a dictionary
# 2. search queries should not be case sensitive
# 3 use string.punctuation to remove punctuation from the start and end of a word as well
    # "stock," appears in the document, this should be counted as an instance of the
    # word "stock" (without the comma).
 # 4. Don’t forget to convert strings to numbers (and vice versa) where appropriate
import string
def list_of_doc():
#function to create a list of document from the text, each document is separated by the <NEW DOCUMENT> line
    line_string = ""
    for line in file:
        line_string += line.strip(string.punctuation)+" "
        # remove punctuation at start and end of the line
        # adding space at the end of each line before adding it to the string
        # to avoid words at beginning of line and end of line being sticked together

    doc_list = line_string.split("NEW DOCUMENT>")

    doc_list.remove("")

    dictionary(doc_list)
    return(doc_list)
def dictionary(doc_list):
# creat a dictionary which has key is the word, and value is the set of document numbers of documents contain that word.
    for index,doc in enumerate(doc_list):
        doc = doc.lower().strip()
        doc = doc.strip(string.punctuation).split(" ") # remove punctuation and split each document in to a list of words

        for word in doc:
            word = word.strip()
            word = word.strip(string.punctuation)# remove punctuation and space at both ends of each word
            if word in dic.keys(): # if word is found in dictionary, add the document number to the value set
                dic[word].add(index+1)
            else:
                dic[word] = {index+1} # if word is not found in dictionary, add that word into dictionary
                                      # the value is the current document number
                                      # document number = index of that document in the list + 1
    return(dic)

def search(words):
    # break the searched words into a list of words
    single_word_list = words.split(" ")
    list_set = [] # create a new list to store value sets of searched words found in dictionary

    for s_word in single_word_list:
        s_word = s_word.lower().strip()
        s_word = s_word.strip(string.punctuation)  # remove punctuation and space at both sides of each word

    # check if each searched word exist in the dictionary.
    # If yes, add the value found in dictionary to the store list
        if s_word in dic.keys():
            list_set.append(dic[s_word])


    if len(list_set) == len(single_word_list): # check if all searched words are found in dictionary.
     # if yes,find the list of document that contains all searched words using intersection operation
     #    while True:
     #        if len(list_set) >1:
     #            result =list_set[0] & (list_set[1]) # find the intersection of two first set
     #            list_set[0] = result                # assign result to the first element of the list of set
     #            list_set.remove(list_set[1])        # remove the second element
     #            # the loop will continue until len(list_set) =1
     #        else:
     #            break

        return set.intersection(*list_set)


        # return(list_set[0]) # the list of sets of document number after intersection operation now only has one element

    else: # if any searched word is not found in dictionary, no document is found
        return("no relevant document is found")

# main code:
while True:
    # prompt user a list of options to choose
     prompt = input("what would you like to do?""\n""1. Search for documents""\n""2. Read Document""\n""3. Quit Program""\n")
     file = open("../../week 7/doc1.txt", "r")
     dic = {}
     read_doc = list_of_doc()

    #option 1: search all documents contain words that are searched for
     if prompt == str(1):
        words = input("Enter search words: ")
        print(search(words))
    #option2:print document of selected number
     elif prompt == str(2):
        try:
            doc_number = int(input("Enter document number: "))
            if doc_number in range(1,len(read_doc)-1): # avoid user entering negative document numbers
                print("DOCUMENT NO.",doc_number,"_" * 55)
                print(read_doc[doc_number-1])
                print("_" * 70)
            else:
                print("document number",doc_number," is not exist")
        # message printed when user enter an input other than an integer
        except ValueError:
            print("please enter a valid document number")
    #option3: quit program
     elif prompt == str(3):
         break



