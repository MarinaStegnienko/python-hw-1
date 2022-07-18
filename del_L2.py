def oddOrEven(num):
    
    x=num%2
    if x==1:
       print('число', num, 'непарне')
    else:
       print('число',num,'парне')
        
num=int(input("Введіть число"))
oddOrEven(num)