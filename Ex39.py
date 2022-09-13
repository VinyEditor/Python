a = 1
b = 1
f = a + b

for i in range (1 , 31, 1):
    print(f)
    b = a
    a = f
    f = a+b
      
#1, 1, 2, 3, 5, 8, 13, 21, ...