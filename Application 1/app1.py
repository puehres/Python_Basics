import json

def get_def(word):
    with open(r"C:\Users\fpuhringer\github\Python_Course\Application 1\data.json") as json_file:
        dict = json.load(json_file)
        print(dict.get(word))

word = input("Please enter the word you are looking for:\n")
get_def(word)
