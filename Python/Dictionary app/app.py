import json
import difflib
from difflib import get_close_matches

#load the data in a dictionary and store in data
data = json.load(open("data.json"))


def translate(word):
    word = word.lower()#to prevent upper and lower case problem
    if word in data:
       return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        #get_close_matches gives a list of words similar to the word
       print("Did you mean %s instead?" % get_close_matches(word,data.keys())[0])
       #%s-placeholder for string variable
       answer = input("Y or N:  ")
       if answer =="Y":
           return data[get_close_matches(word,data.keys())[0]]
           #the first element in the list of similar words is the most similar
           #words are compared to the list of keys in data.keys()
       else:
           return "Sorry your word does not really exist then try again"
    else:
        return "Nope"
    #two condition if the word is not exact-find first item of similar words
    #otherwise just say the word does not exist
word = input("Enter a word: ")
output = translate(word)
if(type(output) == list):#meanings are always given in the form of a list
    for item in output:
        print (item)
else:#if the word is not found
    print(output)
