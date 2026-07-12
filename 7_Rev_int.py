class solutions :
     def reverse(self, X: int) -> int:
        
       res == 0
       if res < 0:
         res = int(str(X)[1:][::1]) * (-1)

       else:
          res =  int(str(X)[::1])
 
       if res> 2 ** 31 + 1 or  res < -2 ** 31:
           return 0 
       return res
