def get_input():
    global lst
    print("Function: get_input()")
    lst = input("Enter 7 numbers separated by comma: ")
    lst = lst.split(",")
    print("Data in list:",lst)
    
def bubble_sort():
    print("Function: bubble_sort()")
    for y in range(1,len(lst)):
        for x in range(0,len(lst)-1):
            if lst[x]>lst[x+1]:
                z = lst[x+1]
                lst[x+1] = lst[x]
                lst[x] = z
        print("After Round %d:"%y,lst)
    print("Sorted List:",lst)
get_input()
bubble_sort()