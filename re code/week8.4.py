def get_input():
    global s
    print("Function: get_input()")
    s = input("Enter 7 numbers separated by comma: ")
    print("Original string:",s)
    s = list(s)
def selection_sort():
    print("Function: selection_sort()")
    for y in range(0,len(s)-1):
        min = y 
        for x in range(y+1,len(s)):
            if s[x]<s[min]:
                min = x
        if min!=y:
            z = s[y]
            s[y] = s[min]
            s[min] = z
        print("After Round %d:"%(y+1),s)
    print("Sorted List:",s)
get_input()
selection_sort()