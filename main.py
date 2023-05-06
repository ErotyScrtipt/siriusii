from stop_words import get_stop_words
stop = get_stop_words('english')
def filter(word: str) -> str:
    wordcor = ''
    if word[-1].isalpha():
        wordcor = word.lower()
    else:
        wordcor = word[:-1].lower()    
    return wordcor

def check(s):
    data = open('data.txt', 'r').read().split('\n')
    dct = {}
    for line in data:
        for word in line.split()[:-1]:
            wordcor = filter(word)
            if wordcor not in stop:
                if wordcor not in dct:
                    dct[wordcor] = [0, 0]
                if line.split()[-1] == '1':
                    dct[wordcor][1] += 1
                dct[wordcor][0] += 1
    if s == '': 
        inp = open('input.txt', 'r').read().split('\n')
    else:
        inp = [s]
    for line in inp:
        cor = 1
        incor = 1
        for word in line.split():
            wordcor = filter(word)
            if (wordcor in dct and (dct[wordcor][1] != dct[wordcor][0] and dct[wordcor][1])):
                cor *= dct[wordcor][1] / dct[wordcor][0]
                incor *= (dct[wordcor][0] - dct[wordcor][1]) / dct[wordcor][0] 
        return " ".join([line, str(int(cor >= incor)), str(cor), str(incor)])
