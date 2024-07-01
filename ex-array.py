from array import array


num = array('i',[4,6,8,5,9])
new = array(num.typecode,(a*a for a in num ))
for i in new :
    print(i)
