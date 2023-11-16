# lista
string= []
i= 0
small_string= []
big_string=[]
medium_string= []
while i <10:
    x= input ("algo")
    s = len (x)
    if s < 5: 
        small_string.append(x)
    if s==5:
        medium_string.append(x)
    else:
        big_string.append(x)
        i+=1
print(small_string,big_string)


    


    



    

     
    


