def example2(n):
    for i in range(n):
        for j in range(n):
            print(i,j)          # till here O(n^2)
    for i in range(n):        # here O(n)
        print(i)

        # total number of operations = O(n^2 + n)
        # but we only consider the dominant so, final complexity is O(n^2)
example2(3)
