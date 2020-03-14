import json
from difflib import get_close_matches

data = json.load(open('data/data.json'))


def getmatch(q, d):
    return get_close_matches(q, d.keys())


def fetch(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(getmatch(word, data)) > 0:
        c = input('Did you mean %s instead? Enter 1 if yes and 2 if no : ' %
                  getmatch(word, data)[0])
        if(c == '1'):
            return data[getmatch(word, data)[0]]
        elif (c == '2'):
            return 'Word not in dictionary. Please Try another word'
        else:
            return 'We didn\'t understand your entry'
    else:
        return 'Word not in dictionary. Please Try another word'


print('Press # to exit from dictionary')

while True:
    query = input('Enter Query: ')
    if(query == '#'):
        print('Exited from Dictionary')
        break
    else:
        output = fetch(query)
        if type(output) == list:
            for index, value in enumerate(output):
                print(f'{index}. %s' % value)
        else:
            print(output)
        continue
