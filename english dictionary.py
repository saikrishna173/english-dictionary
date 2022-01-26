import json
from difflib import get_close_matches as match

#we are loading the data from the data file
data = json.load(open("data.json"))

#take word from user
word = input('Enter word: ')

#we are checking the data from the data base and returning to the user by using this function getmeaning and using w as parameter
def getMeaning(w):
    #changing to lower case
    w = w.lower()
    if w in data:
        return data[w]
    #now we are searching and returning data
    elif len(match(w,data.keys())) > 0:
        close_match = match(w,data.keys())[0]
        print("Did you mean %s instead? Enter Y if yes or N if no: " % close_match)
        choice = input()
        choice = choice.lower()
        if choice == 'y':
            return data[close_match]
        elif choice == 'n':
            return "The word doesn't exist. Please double check it."
        else:
            return "Sorry, We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

meaning = getMeaning(word)

if type(meaning) == list:
    for item in meaning:
        print(item)
else:
    print(meaning)