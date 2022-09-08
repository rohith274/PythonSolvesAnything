# O(log n) is very powerful and always try to achieve this for better time complexity
# Maximum Sorting algorithms are of O(nlogn)
# We drop constants in case big O

def print_items(a, b):
    for i in range(a):
        print(i)       # this runs for a times so O(a)
    for j in range(b):
        print(j)       # this runs for b times so O(b)
        # total time complexity is O(a+b)


print_items(3, 4)
