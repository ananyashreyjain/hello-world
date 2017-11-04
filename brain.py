import copy
n=input('enter no of times u want to play ') 
x1=[]
o1=[]
option=int(input("1-- for playing with computer \n2-- for playing with other player"))
for i in range(0,int(n)):
    class tictactoe():
        def __init__(obj):
            obj.a=[[' ',' ',' ' ],[' ',' ',' '],[' ',' ',' ']] 
            obj.string1="---------- --------- ----------"
            obj.c=0
            obj.x=0
            obj.o=0
        def getboard(obj):
            for i in range(0,3):
                print(obj.string1)
                print("|    "+obj.a[i][0]+"    |    "+obj.a[i][1]+"    |    "+obj.a[i][2]+"    |")
            print(obj.string1)
        def getevaluation(obj):
            if((obj.a[0][0]==obj.a[1][1])&(obj.a[0][0]==obj.a[2][2])&((obj.a[0][0]=='X')or(obj.a[0][0]=='O'))):
                print(obj.a[0][0]+" WINS")
                obj.c=obj.c+1
                if(obj.a[0][0]=='X'):
                    obj.x+=3
                else:
                    obj.o+=3
            if((obj.a[0][2]==obj.a[1][1])&(obj.a[0][2]==obj.a[2][0])&((obj.a[0][2]=='X')or(obj.a[0][2]=='O'))):   
                print(obj.a[0][2]+" WINS")
                obj.c=obj.c+1
                if(obj.a[0][2]=='X'):
                    obj.x+=3
                else:
                    obj.o+=3
            for i in range(0,3):
                if((obj.a[i][0]==obj.a[i][1])&(obj.a[i][0]==obj.a[i][2])&((obj.a[i][0]=='X')or(obj.a[i][0]=='O'))): 
                    print(obj.a[i][0]+" WINS")
                    obj.c=obj.c+1
                    if(obj.a[i][0]=='X'):
                        obj.x+=3
                    else:
                        obj.o+=3
            for j in range(0,3):
                if((obj.a[0][j]==obj.a[1][j])&(obj.a[0][j]==obj.a[2][j])&((obj.a[0][j]=='X')or(obj.a[0][j]=='O'))): 
                    print(obj.a[0][j]+" WINS")
                    obj.c=obj.c+1
                    if(obj.a[0][j]=='X'):
                        obj.x+=3
                    else:
                        obj.o+=3
        def getevaluation1(obj,c,d=0):
            c1=0
            d1=0
            if((c[0][0]==c[1][1])&(c[0][0]==c[2][2])&(c[0][0]=='X')):
                c1=c1+1
            if((c[0][2]==c[1][1])&(c[0][2]==c[2][0])&(c[0][2]=='X')):   
                c1=c1+1
            for i in range(0,3):
                if((c[i][0]==obj.a[i][1])&(c[i][0]==c[i][2])&(c[i][0]=='X')): 
                    c1=c1+1
            for j in range(0,3):
                if((c[0][j]==c[1][j])&(c[0][j]==c[2][j])&(c[0][j]=='X')): 
                    c1=c1+1
            if((c[0][0]==c[1][1])&(c[0][0]==c[2][2])&(c[0][0]=='O')):
                d1=d1+1
            if((c[0][2]==c[1][1])&(c[0][2]==c[2][0])&(c[0][2]=='O')):   
                d1=d1+1
            for i in range(0,3):
                if((c[i][0]==c[i][1])&(c[i][0]==c[i][2])&(c[i][0]=='O')): 
                    d1=d1+1
            for j in range(0,3):
                if((c[0][j]==c[1][j])&(c[0][j]==c[2][j])&(c[0][j]=='O')): 
                    d1=d1+1
            if(d==1and d1>0):
                return 1
            elif(c1>=1and d1==0):
                return 1
        def getinput(obj):
            print("first X chooses")
            for k in range(0,9):
                if(option==1 and k%2==0):
                    n1=obj.getbrain()
                else:
                    n1=input("enter position--")
                while(obj.check(n1,obj.a)==False):
                    n1=input("input empty position")
                n=int(n1)-1
                i=(int(n/3))
                j=(n%3)
                if(k%2==0):
                    obj.a[i][j]='X'
                else:
                    obj.a[i][j]='O'
                obj.getevaluation()
                obj.getboard()
                if(obj.c==1):
                    break
        def check(obj,b,z):
            n=int(b)-1
            i=(int(n/3))
            j=(n%3)
            if(z[i][j]=='X'or z[i][j]=='O'):
                return False
            else:
                return True
        def getbrain(obj):
            n=0
            k=0
            position=[]
            wins=[]
            for l in range(0,9):
                if(obj.check(l+1,obj.a)==True):
                    p=copy.deepcopy(obj.a)
                    x0=int(l/3)
                    y0=l%3
                    p[x0][y0]='O'
                    if(obj.getevaluation1(p,1)==1):
                        return(l+1)
                        k=1
            for i1 in range(0,9):
                c1=0
                c2=0
                c=[[' ',' ',' ' ],[' ',' ',' '],[' ',' ',' ']] 
                b=[[' ',' ',' ' ],[' ',' ',' '],[' ',' ',' ']] 
                b=copy.deepcopy(obj.a)
                if(obj.check((i1+1),(b))==False):
                    continue
                else:
                    position.append(i1+1)
                    x1=int((i1/3))
                    y1=(i1%3)
                    b[x1][y1]="X"
                    c=copy.deepcopy(b)
                    c1=0
                    for i2 in range(0,9):
                        x2=(int(i2/3))
                        y2=(i2%3)    
                        if(obj.check((i2+1),c)==False):
                            continue
                        else:
                            if(c1%2==0):
                                c[x2][y2]='O'
                            else:
                                c[x2][y2]='X'
                            c1+=1
                    for i3 in range(0,9):
                        x3=(int(i3/3))
                        y3=(i3%3)
                        for j3 in range(i3+1,9):
                                x4=(int(j3/3))
                                y4=(j3%3)
                                if((b[x4][y4]=='X'or b[x4][y4]=='O')or(b[x3][y3]=='X'or b[x3][y3]=='O')):
                                    continue
                                else:
                                    if( c[x3][y3]!=c[x4][y4]):
                                        temp=c[x3][y3]
                                        c[x3][y3]=c[x4][y4]
                                        c[x4][y4]=temp
                                        if(obj.getevaluation1(c)==1):
                                            n+=1
                                        
                                        c[x4][y4]=c[x3][y3]
                                        c[x3][y3]=temp
                    wins.append(n)
                    n=0
            if(k!=1):
                return(position[wins.index(max(wins))])        
                
    ob=tictactoe() 
    ob.getinput()	
    if(ob.c==0):
        print ("no one wins")
        ob.x+=1
        ob.o+=1
    x1.append(ob.x)
    o1.append(ob.o)
    print("score of X")
    print(x1)
    print("score of O")
    print(o1)   








