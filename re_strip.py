import re


def strp(string, target=' '):
    '''eiminates repeated charectores surrounding a word, usage: strip(string,
    targeted charecters0)'''
    cut = re.compile(f'^({target})*')
    word = cut.sub('', string)
    cut = re.compile(f'({target})*$')
    word = cut.sub('', word)
    return word
