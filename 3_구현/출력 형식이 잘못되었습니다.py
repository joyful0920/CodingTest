import sys
si = sys.stdin.readline

k = int(si())

for test in range(1, k + 1):
    s1 = si().strip()
    s2 = si().strip()

    s1 = s1.lower()
    s2 = s2.lower()
    s1 = s1.replace('(', ' ( ')
    s1 = s1.replace('[', ' ( ')
    s1 = s1.replace('{', ' ( ')
    s1 = s1.replace(')', ' ) ')
    s1 = s1.replace(']', ' ) ')
    s1 = s1.replace('}', ' ) ')
    s1 = s1.replace('.', ' . ')
    s1 = s1.replace(',', ' , ')
    s1 = s1.replace(':', ' : ')
    s1 = s1.replace(';', ' , ')
    s2 = s2.replace('(', ' ( ')
    s2 = s2.replace('[', ' ( ')
    s2 = s2.replace('{', ' ( ')
    s2 = s2.replace(')', ' ) ')
    s2 = s2.replace(']', ' ) ')
    s2 = s2.replace('}', ' ) ')
    s2 = s2.replace('.', ' . ')
    s2 = s2.replace(',', ' , ')
    s2 = s2.replace(':', ' : ')
    s2 = s2.replace(';', ' , ')

    s1 = ' '.join(s1.split())
    s2 = ' '.join(s2.split())

    if s1 != s2:
        print('Data Set ' + str(test) + ': not equal')
        print()
        continue
    
    print('Data Set ' + str(test) + ': equal')
    print()