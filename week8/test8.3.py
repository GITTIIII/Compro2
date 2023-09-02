def get_input():
    global lst
    print("Function: get_input()")
    n = input("Enter 7 numbers separated by comma: ")
    lst = n.split(",")
    print("Data in list:",lst)

def bubble_sort():
    print("")
    print("Function: bubble_sort()")
    for x in range(1,len(lst)):
        for y in range(0,len(lst)-1):
            if lst[y]>lst[y+1]:
                z = lst[y+1]
                lst[y+1] = lst[y]
                lst[y] = z
        print("After Round %d:"%x,lst)
    print("Sorted List:",lst)

get_input()
bubble_sort()