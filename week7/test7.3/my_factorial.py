class Fac:
    def loop(n):
        facloop = 1
        for x in range(n,0,-1):
            if x == 1:
                print("%d"%x)
            else:
                print("%d*"%x,end="")
            facloop *= x
        return(facloop)
    
    def recursive(n):
        if n==1:
            print("%d"%n)
            return(1)
        else:
            print("%d*"%n,end="")
        return(n*Fac.recursive(n-1))