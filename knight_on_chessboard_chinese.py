# -*- coding: utf8 -*-
import turtle as t
import time

width=9
height=10
board=[]
rule=[[2,-1],[1,-2],[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1]]
for i in range(height):
    temp=[]
    for i in range(width):
        temp.append(0)
    board.append(temp)

trace=[]


def inputxy():
    initx=input('input x of the init point')
    inity=input('input y of the init point')
    while True:
        if (initx in range(width))&(inity in range(height)):
            initp=(initx,inity)
            return initp
        else:
            print ("error")
            initx=input('input x of the init point')
            inity=input('input y of the init point')

def dinit_c():
    t.Turtle().screen.delay(0)
    t.pensize(1)
    t.hideturtle()
    t.setup(450,450)
    t.pu()

    for i in range(10):
        t.pu()
        t.goto(-170,170-i*40)
        t.pd()
        t.goto(150,170-i*40)
    t.pu()

    for i in range(9):
        t.pu()
        t.goto(-170+i*40,170)
        if i in range(1,8):
            t.pd()
            t.goto(-170+i*40,10)
            t.pu()
            t.goto(-170+i*40,-30)
        t.pd()
        t.goto(-170+i*40,-190)
    t.pu()

    t.goto(-50,170)
    t.pd()
    t.goto(30,90)
    t.pu()
    t.goto(-50,90)
    t.pd()
    t.goto(30,170)
    t.pu()
    t.goto(-50,-110)
    t.pd()
    t.goto(30,-190)
    t.pu()
    t.goto(-50,-190)
    t.pd()
    t.goto(30,-110)
    t.pu()

    t.hideturtle()

def dinit_w():
    t.Turtle().screen.delay(0)
    t.pensize(1)
    t.hideturtle()
    t.setup(440,440)
    t.pu()

    for i in range(9):
        t.pu()
        t.goto(-190,190-i*40)
        t.pd()
        t.goto(130,190-i*40)
    t.pu()

    for i in range(9):
        t.pu()
        t.goto(-190+i*40,190)
        t.pd()
        t.goto(-190+i*40,-130)
    t.pu()

    t.hideturtle()

    
def write(x,y,p):
    t.pu()
    t.goto(-180+40*x,160-40*y)
    t.pd()
    t.write(p,font=('Arial',16))
    t.pu()     

def jump(x,y,c):
    xnew=x+rule[c][0]
    ynew=y+rule[c][1]
    if ((xnew in range(width))&(ynew in range(height))):
        if (board[ynew][xnew]==0):
            return True
        else:
            return False
    else:
        return False

def tour(x,y,z):
    board[y][x]=z
    c=0
    flag=0
    xx=x
    yy=y
    trace.append((x,y))
    if (z==width*height):
        return True
    while(c<8):
        flag=0
        flag=jump(xx,yy,c)
        if (flag!=0):
            xn=xx+rule[c][0]
            yn=yy+rule[c][1]
            temp=tour(xn,yn,z+1)
            if (z<width*height-5):
                print z c
            if (temp==0):
                c=c+1
            else:
                return True
        else:
            c=c+1
    
    if (c==8):
        board[y][x]=0
        trace.pop()
        return False
    

def main():
    ii=inputxy()
    start=time.clock()
    k=tour(ii[0],ii[1],0)
    #k=tour(0,1,1)
    end=time.clock()
    print str(end-start)
    if(k==0):
        print ('no result')
    else:
        pass
    
        dinit_c()
        #dinit_w()
        for i in trace:
            write(i[0],i[1],trace.index(i))
            pass
        t.done()
    
    print trace
    print board

if __name__ == "__main__":
    main()
