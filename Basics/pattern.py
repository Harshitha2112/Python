#right downward triangle

num=int(input("enter number of rows"))
for i in range(0,num): #for row
    for j in range(num-i):#for column
        print("*",end="")
    print() #for newline


   # or


n=5
for i in range(n):
    for j in range(i,n):
        print("#",end=" ")
    print()


#right triangle

num=int(input("enter number of rows"))
for i in range(0,num):  # for i in range(1,num+1):
    for j in range(1+i):#for i in range (1,1+i):
        print("*",end="")
    print()

#pyramid

num=int(input("enter number of rows"))
k=1
for i in range(1,num):         #i=1,
    for j in range(1,k+1):     #range is 1 to 2 and 2 is excluded so, it will print only 1 time
        print("*",end=" ")     #\once this statement is executed it will go to nxt statement coz the range of repeatation is only one tym
    k=k+2                      # the range of repeatation is only one tym, k value is incremented to 3
    print()                    #newline



  #  or

    n = 5
    for i in range(n):
        for j in range(n - i):   #decreasing space
            print(end="  ")
        for j in range(i):       # increasing star
            print("x", end=" ")  # no spacing is requierd
        for j in range(i + 1):   # increasing star
            print("x", end=" ")
        print()



#pyramid even

num=int(input("enter the number of rows"))
k=1
for i in range(0,num):
    for j in range(0,k+1):
        print("*",end=" ")
    k=k+2
    print()


#pyramid natural number

    num = int(input("enter the number of rows"))
    for i in range(0, num):
        for j in range(0, num - i - 1):
            print(end=" ")
        for j in range(0, i + 1):
            print("*", end=" ")
        print()


      #  or


        n = 5
        for i in range(n):
            for j in range(n - i):
                print(end=" ")
            for j in range(i + 1):
                print("*", end=" ")
            print()


#hill pattern

num=int(input("enter the number of rows"))
for i in range(num,0,-1):    # 0 is excluded ,range is 4 ,3 ,2 ,1
    for j in range(0,num-i): # starting 4-4=0 space
        print(end=" ")
    for j in range(0,i):     #starting range is 0,1,2,3. so it print's 4 stars
        print("*",end=" ")
    print()


    #or


n=5
for i in range(n):
    for j in range(i+1):
        print(end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()



#left downward triangle

n=5
for i in range(n):
    for j in range(i):
        print(end=" ")
    for j in range(n-i):
        print("x",end="")
    print()



    #or

    n = 5
    for i in range(n):
        for j in range(i + 1):
            print(end=" ")
        for j in range(n - i):
            print("*", end=" ")
        print()


# invert hill pattern

n=5
for i in range(n):
    for j in range(i+1):
        print(end="  ")
    for j in range(i,n-1):
        print("x",end=" ")
    for j in range(i,n):
        print("x",end=" ")
    print()


      #or

    n = 5
    for i in range(n):
        for j in range(i + 1):
            print(end=" ")
        for j in range(n - i):
            print("*", end=" ")
        print()

#diamond

n = 5
for i in range(n-1):
    for j in range(n - i):  # decreasing space
        print(end="  ")
    for j in range(i):  # increasing star
        print("x", end=" ")  # no spacing is requierd
    for j in range(i + 1):  # increasing star
        print("x", end=" ")
    print()

for i in range(n):
    for j in range(i+1):
        print(end="  ")
    for j in range(i,n-1):
        print("x",end=" ")
    for j in range(n-i):
        print("x",end=" ")
    print()



#pattern 1


    n = 5
    p = 1
    for i in range(n):                   #1
        for j in range(i + 1):           #2 2
            print(p, end=" ")#i+1 for p  #3 3 3
        p += 1                           #4 4 4 4
        print()                          #5 5 5 5 5

#pattern 2

n=5
p=5
for i in range(n):             #5
    for j in range(i+1):       #4 4
        print(p,end=" ")       #3 3 3
    p-=1                       #2 2 2 2
    print()                    #1 1 1 1 1


# pattern 3

n=5                         #0
for i in range(n):          #1 1
    for j in range(i+1):    #2 2 2
        print(i,end=" ")    #3 3 3 3
    print()                 #4 4 4 4 4


 #pattern 4

n=5
p=1
for i in range(n):            #11111
    for j in range(i):        # 2222
        print(end=" ")        #  333
    for j in range(n-i):      #   44
        print(p,end="")       #    5
    p+=1
    print()



    #or

#pattern 5

n=5
p=5
for i in range(n):            #     5
    for j in range(n-i):      #    4 4
        print(end=" ")        #   3 3 3
    for j in range(i+1):      #  2 2 2 2
        print(p,end=" ")      # 1 1 1 1 1
    p-=1
    print()


    #or

#pattern 6

    n = 5
    p = 1
    for i in range(n):
        for j in range(n - i):     #     1
            print(end=" ")         #    2 2
        for j in range(i + 1):     #   3 3 3
            print(p, end=" ")      #  4 4 4 4
        p+= 1                      # 5 5 5 5 5
        print()


    #or


n=5
p=1
for i in range(n):
    for j in range(i+1):       # 1 1 1 1 1
        print(end=" ")         #  2 2 2 2
    for j in range(n-i):       #   3 3 3
        print(p,end=" ")       #    4 4
    p+=1                       #     5
    print()


    #or

    n = 5
    p = 5
    for i in range(n):
        for j in range(i + 1):     #5 5 5 5 5
            print(end=" ")         # 4 4 4 4
        for j in range(n - i):     #  3 3 3
            print(p, end=" ")      #   2 2
        p-= 1                      #    1
        print()

    n = 5
    for i in range(n):
        for j in range(i + 1):
            print(end="  ")
        for j in range(i, n - 1):
            print("x", end=" ")
        for j in range(i, n):
            print("x", end=" ")
        print()

