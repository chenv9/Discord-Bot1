def check(dir, len): 
  
    for i in range(1 , len + 1):  
        password(dir, i, "", len) 
      

def password(dir, i, str, len): 
   
    if (i == 0):
        print(str) 
        return
      
    for j in range(0, len): 
  
        combin = str + dir[j] 
        password(dir, i - 1, combin, len) 
  
    return
  
dir = ['a', 'b', 'c', 'd', 'e', 'f','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ] 
len = 8 
check(dir, len) 
