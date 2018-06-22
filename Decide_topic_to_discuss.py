import random
#this is to randomly choose a topic 
#cause i find it tough to choose one
a = []
def add():
    top=input("please add a topic :- ")
    a.append(top)
def ans():
    an=random.choice(list(a))
    print(an)
    a.remove(an)

def rem():
    re=input("what would you like to remove")
    a.remove(re)

def dis():
    print(a)

def call(x):
    if(x=='1'):
        add()
    if(x=='2'):
        rem()
    if(x=='3'):
        dis()
    if(x=='4'):
        ans()        
ch = True    
while ch==True:
    
    print("""
    1: add topic
    2: remove topic
    3: display
    4: give a topic to discuss
    5:exit
    """)
    check = input()
    if check == '5':
        ch=False
        exit()

    else:
        call(check)        
        
    

    
