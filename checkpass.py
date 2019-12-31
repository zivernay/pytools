import re


def check(passwd):
    '''takes a password and checks if it is secure based on lenth and charecter
     type
     usage: check(password)'''
    checks = {
        '[a-z]': 'small letters', '[A-Z]': 'capital letters', '[0-9]': 'digits'
         }
    pas = 0
    if len(passwd) > 8:
        for k, v in checks.items():
            check = re.compile(f'{k}+')
            if check.search(passwd) is None:
                print('password must include ' + v)
                break
            else:
                pas += 1
        if pas == 3:
            print('password secure!')
    else:
        print('password too short')
