from array import array


num = array('i',[4,6,8,5,9])
new = array(num.typecode,(a*a for a in num ))
i = 0
while i < len(new):
    print(new[i])
    i+=1
    
    
    
