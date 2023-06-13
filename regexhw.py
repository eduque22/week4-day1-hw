import re
with open("namedup.txt") as f:
    data = f.readlines()

name_pattern = re.compile('([A-z][a-z]+[,]) ([A-z][a-z]+)')
tweet_patt = re.compile('\s\s*@[a-z]*')

def new_plan(data):
    for person in data:
        match1 = name_pattern.search(person)
        match2 = tweet_patt.search(person)
        if match2:
            print(match1.group(2), match1.group(1), match2[0])
            
        else:
            continue


new_plan(data)