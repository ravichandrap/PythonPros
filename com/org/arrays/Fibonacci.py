'''
Created on Nov 27, 2018

@author: penumr
'''

# Memoized
def fibMemoized(n, lookup):
    
    if n ==0 or n == 1:
        lookup[n] = n;
    
    if lookup[n] is None:
        lookup[n] = fibMemoized(n-1, lookup) + fibMemoized(n-2, lookup);
    
    return lookup[n];

def fibTabulated(n):
    f = [0]*(n+1)
    f[1] = 1;
    
    for i in xrange(2, n+1):
        f[i] = f[i-1]+f[i-2];
    
    return f[n];
def main():
    
    n=10;
    
    lookup = [None]*(101);
    print "Fibonacci Memoized Number is: ", fibMemoized(n, lookup);
    print "Fibonacci Tabulated Number is: ", fibTabulated(n);

if __name__ == "__main__":
    main()