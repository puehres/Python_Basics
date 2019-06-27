import json
from difflib import get_close_matches

with open(r"C:\Users\fpuhringer\github\Python_Course\Application 1\data.json") as json_file:
    dict = json.load(json_file)

def get_def(word):
    word = word.lower()
    get_close_matches(word,dict.keys(),1)[0]
    if word in dict:
        return(dict.get(word))
    elif word.capitalize() in dict:
        return(dict.get(word.capitalize()))
    elif word.upper() in dict:
        return(dict.get(word.upper()))
    elif len(get_close_matches(word,dict.keys())) >  0:
        choice = input("Did you mean %s instead? Enter Y if yes, or N if no:\n" % get_close_matches(word,dict.keys())[0])
        if choice == "Y":
            return dict[get_close_matches(word,dict.keys())[0]]
        elif choice == 'N':
            return "The word doesn't exit. Please double check it."
        else:
            return("We didn't understand your query.")
    else:
        return "The word doesn't exist. Please double check it."

word = input("Please enter the word you are looking for:\n")

output = get_def(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
