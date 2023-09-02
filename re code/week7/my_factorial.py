class Fac:
    def loop(n):
        fac = 1
        for x in range(n,0,-1):
            if x>1:
                print("%d*"%x,end="")
            else:
                print("%d"%x,end="")
            fac *= x
        return(fac)
    def recursive(n):
        if n==1:
            print("%d"%n,end="")
            return(1)
        else:
            print("%d*"%n,end="")
        return(n*Fac.recursive(n-1))