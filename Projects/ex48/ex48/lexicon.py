direction = ('north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verbs = ('go', 'stop', 'kill', 'eat')
stop=('the', 'in','of','from', 'at', 'it ')
noun = ('door','bear', 'princess','cabinet')

def scan(sentence):
    results=[]
    analyze = sentence.split()
    print(analyze)
    for i in analyze:
        if i in direction:
            result = tuple(('direction',i))
        elif i in verbs:
            result = tuple(('verb',i))
        elif i in stop:
            result = tuple(('stop',i))
        elif i in noun:
            result = tuple(('noun',i))
        else:
            if convert_numbers(i) == None:
                result = tuple(('error', i))
            else:
                result = tuple(('number', convert_numbers(i)))
        results.append(result)

    return results


def convert_numbers(word):
    try:
        return int(word)
    except ValueError:
        return None
