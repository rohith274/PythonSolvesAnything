def printnum(n):
    for i in range(n):
        print(i) # this is O(n)
def printnums(n):
    for i in range(n):
        for j in range(n):
            print(i,j) # this is O(n*n)
# After O(n*n) or O(n^2) we call everything like O(n^3) as 
# O(n^2)
printnum(10)
printnums(10)