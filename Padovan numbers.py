"""
The Padovan sequence is the sequence of integers defined by the initial values

P(0) = P(1) = P(2) = 1
and the recurrence relation

P(n) = P(n-2) + P(n-3)
The first few values of P(n) are:

1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, 21, 28, 37, 49, 65, 86, 114, 151, 200, 265, ...
"""





# Solve using memoization

def padovan(n):
    tab = [1,1,1]
    
    for i in range(3, n+1):
        tab.append(tab[i-3] + tab[i-2])
    return tab[n]
