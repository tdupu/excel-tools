import re
import numpy as np

def is_subdictionary(A,B):
    return set(A.items()).issubset(B.items())


def match_key(list_of_dicts, my_key, my_value):
    """
    my_key needs to be a string
    my_value is anything
    """
    possibles =[]
    for dict0 in list_of_dicts:
        if dict0[my_key] == my_value:
            possibles.append(dict0)
    return possibles
    
def kill_repeats(mylist):
    newlist = []
    for x in mylist:
        if newlist.count(x)=0:
            newlist.append(x)
    return newlist
    
    
def make_inclusive_search_key(words):
    """
    >>> words = ['apple','banana','c']
    >>> key=make_inclusive_search_key(words)
    "^(apple|banana|c)"
    >>> re.search(key,"copper")
    True
    
    we could have also used "starts with"
    """
    search_key = "("
    n = len(words)
    for i in range(n-1):
        search_key = search_key + words[i]+ "|"
    search_key = "^"+search_key+words[n-1]+")"
    return search_key

def copyd(oldd):
    """
    A function that copies dictionaries without making them point to the same place in memory.
    """
    newd = {}
    for k in oldd.keys():
        newd[k] = oldd[k]
    return newd

def dicts_by_key(keys,X):
    """
    INPUT:
    --X a list of dictionaries X all with the same key values
    --keys, a subset of keys of the dictionaries
    OUTPUT: [vals,dictX]
    --vals, all the possible values of [x[k] for k in keys] and x in X
    --dictX a dictionary of lists, where
        dictX[v] = [all dictionaries of where [x[k] for k in keys] = v]
    """
    dictX = {}
    vals = []
    for x in X:
        p = [x[k] for k in keys]
        
        if vals.count(p)==0:
            vals.append(p)
        
        if dictX[p]==None:
            dictX[p] = []
            dictX[p].append(x)
        else:
            dictX[p].append(x)V
    return vals,dictX

"""
This function isn't used here but I want to use it in Zulip for
1) pairing people into random streams during class
2) "speeddating" when we need to talk about problems
3) tournament of ideas.

I'm going pair people at random and then throw them in a chat room for 10 minutes and then cancel.
"""

def chunk(mylist,n):
    """
    len(chunk(range(21),6)) == 21//6
    True
    """
    m = len(mylist)
    r = m % n
    a=m//n
    if a==0:
        return [mylist]
    if r==0 and a>0:
        mylist = list(np.random.permutation(mylist))
        return [mylist[n*i:n*(i+1)] for i in range(a)]
    else:
        remainders = mylist[0:r]
        remainders = np.random.permutation(remainders)
        newlist = mylist
        teams = chunk(mylist[r:],n)
        m = len(teams)
        for i in range(r):
            j = i % m
            teams[j].append(remainders[i])
            return teams
