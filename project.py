import sys
def qual():
    n1=1
    print("1 B.Tech")
    print("2 M.tech")
    print("3 Phd")
    n=int(input())
    if (n==3):
        print(" How mny Phds you have")
        n1=int(input())
    return (n)*5*n1
def clg():
    print("1.central government colleges (IIT/NIT)")
    print("2. State Universites")
    print("3.Private Deemed Universities")
    print("4.Government colleges")
    print("5 private colleges")
    n=int(input())
    return (6-n)*3
def exper():
    n=int(input())
    return n
def publish():
    n=int(input())
    return n*2
def proj():
    n=int(input())
    return n*3
def sub():
    n=int(input())
    return n*5
def awards():
    n1=0
    n2=0
    n3=0
    print("How many awards you got in each category")
    n1=int(input("Clg level"))
    n2=int(input("State Level"))
    n3=int(input("National Level"))
    return n1*1 + n2*2 + n3*3
def cert():
    n=int(input())
    return n
def tsess():
    n=int(input())
    return n*2
print("Welcome to the Expert System for finding Best Teacher")
n=int(input("Enter how many teacher you want to check"))
c=0
s=0
oname="abcd"
for  x in range(0,n):
    s=0
    name=input("Enter Teacher's name: ")
    print("Enter qualification: ")
    s=s+qual()
    print("Enter Which Type of college: ")
    s=s+clg()
    print("please Enter how many Years of experience: ")
    s=s+exper()
    print("Enter how many reasearch papers have you published: ")
    s=s+publish()
    print("Enter how many Projects you are involved in: ")
    s=s+proj()
    print("How many subjects you can teach: ")
    s=s+sub()
    s=s+awards()
    print("How many Certifications you have: ")
    s=s+cert()
    print("Enter how many training sessions you have attended: ")
    s=s+tsess()
    if(s>c):
        c=s
        oname=name
        oname
    print(s)
print()
print()
print("!-----------------------------------------------------------------!")
print("The best teacher is")
print(oname)
print("!-----------------------------------------------------------------!")
