def AND(r,c):
    global x
    if r==1 and c==1:
      x=1
    else:
        x=0
def AND1(s,c):
    global y
    if s==1 and c==1:
      y=1
    else:
        y=0
    
def NOT(x,q):
    global q_1
    if x==0 and r==0:
        q_1=1
    else:
        q_1=0
def NOT1(q_1,y):
    global q_2
    if q_1==0 and y==0:
        q_2=1
    else:
        q_2=0
    

s=int(input("Enter the value of S(0 or 1): "))
r=int(input("Enter the value of R(0 or 1): "))
q=int(input("Enter the previous output Q(n)(0 or 1): "))
c=1
if s==1 &r==1:
    print("Invalid condition")
elif s==0 & r==0:
    print("Hold condition")
else:
 AND(r,c)
 AND1(s,c)
 NOT(x,q)
 NOT1(q_1,y)
 print("Q(n+1)=",q_1)


 if q_1==0:
    print("clock is Reset")
 elif q_1==1:
    print("Clock is Set")
