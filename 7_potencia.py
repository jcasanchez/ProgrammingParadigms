class power:
   def pow(self, x, n):
        if x==0 or x==1 or n==1:
            return x 
        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.pow(x,-n)
        val = self.pow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

print(power().pow(2, -3));
print(power().pow(3, 5));
print(power().pow(100, 0));