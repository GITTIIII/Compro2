n = input("Enter numbers saparated by space: ")
n = n.split(" ")
if len(n)==len(set(n)):
    print("All numbers are different.")
else:
    print("Some numbers are repeated!!!")