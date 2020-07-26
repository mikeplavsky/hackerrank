from itertools import dropwhile
from functools import reduce

def log(x):
    print(x)

def is_vowel(c):
    return c in "AEIOU"

def first(s,pred):

    idx = -1

    for i in range(len(s)):
        if pred(s[i]):
            idx = i
            break

    return idx

def all_subs(s,ss_set,pred):

    idx = first(s,pred)

    if idx == -1:
        return -1

    ss = ''
    
    for c in s[idx:]:

        ss += c
        ss_set.add(ss)

    return idx

def count_all(s,pred):

    org = s
    ss = set()

    while True:

        i = all_subs(s,ss,pred)
        if i == -1:
            break
            
        s = s[i+1:]

    def count(s,x):

        res = 0

        while True:

            idx = s.find(x)
            res = res if idx == -1 else res + 1

            if idx == -1:
                return res

            s = s[idx+1:]
            if not s:
                return res

    def counter(a,x):

        res = count(org, x)
        log(f"{x}: {res}")
        return a + res

    res = reduce(
        counter, 
        ss, 0)

    log( ss )    
    log (res)

    return res

def minion_game(string):

    s = count_all(string,lambda x: not is_vowel(x))
    k = count_all(string,is_vowel)

    if s > k: 
        print(f"Stuart {s}")

    elif s == k:
        print("Draw")

    else:
        print(f"Kevin {k}")


if __name__ == '__main__':

    s = input()
    minion_game(s)

