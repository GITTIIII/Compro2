def get_input():
    global s
    print("Function: get_input()")
    s = input("Enter a string: ")
    print("Original string:",s)
    s = list(s)

def selection_sort():
    print("")
    print("Function: selection_sort()")
    for x in range(len(s)-1):
        min = x
        for y in range(x+1,len(s)):
            if s[y]<s[min]:
                min = y
        if min != x :
            z = s[x]
            s[x] = s[min]
            s[min] = z
        print("After Round %d:"%(x+1),s)
    print("Sorted List:",s)

get_input()
selection_sort()