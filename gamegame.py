#Fangjiao Xu
#15-112 Final project
import random

class game:
    def __init__(self):
        self.score=0
        self.ellist=[]
        self.listnum=[]
        self.count=0
        #gernerate a list
        for i in range(8):
            listrow=[]
            for j in range(8):
                n=random.randint(1,6)
                listrow.append(n)
            #print listrow
            self.listnum.append(listrow)
        self.checkmatch()
        '''for i in self.listnum:
            print i
        # x is row, y is col
        for num in range(10):
            xy=raw_input("xy")
            self.makemove(int(xy[0]),int(xy[1]),int(xy[2]),int(xy[3]))
            for i in self.listnum:
                print i'''
       
    #check match before the game starts           
    def checkmatch(self):
        count=0
        eliminatelist=[]
        #check match on the row
        for i in range(0,8):
            for j in range(0,6):
                if self.listnum[i][j]==self.listnum[i][j+1] and self.listnum[i][j+2]==self.listnum[i][j+1]:
                    #if there is a match，change the number
                    self.listnum[i][j+1]=random.randint(1,6)
                    count=count+1
        #check match on the col
        for i in range(0,8):
            for j in range(0,6):
                if self.listnum[j][i]==self.listnum[j+1][i] and self.listnum[j+2][i]==self.listnum[j+1][i]:
                    self.listnum[j+1][i]=random.randint(1,6)
                    count=count+1
        if count!=0:
            #check again
            self.checkmatch()

    def changepos(self,x1,y1,x2,y2):
        temp=self.listnum[x1][y1]
        self.listnum[x1][y1]=self.listnum[x2][y2]
        self.listnum[x2][y2]=temp

    def countmatch(self,x1,y1,x2,y2):
        self.count=self.rowmatch(x1,y1)+self.rowmatch(x2,y2)+self.colmatch(x1,y1)+self.colmatch(x2,y2)
   
    def makemove(self,x1,y1,x2,y2):
        if (x1==x2 and abs(y1-y2)==1) or (y1==y2 and abs(x1-x2)==1):
            self.remove()
            self.drop()
            '''self.countmatch()
            count=self.count
            #if the change does not make a match， change the number back
            if count==0:
                temp=self.listnum[x1][y1]
                self.listnum[x1][y1]=self.listnum[x2][y2]
                self.listnum[x2][y2]=temp'''
            '''elif count!=0:
                #get the score
                self.score=self.score+count*10
                #change the matched candies into 0
                self.remove()
                #generate new numbers
                self.drop()'''
            
    def drop(self):
        #from the last row
        for i in range(7,-1,-1):
            for j in range(0,8):
                k=i
                num=-1
                #if the current place is 0
                if self.listnum[k][j]==0:
                    #find the num above it and the num cannot be 0
                    for k in range(i,-1,-1):
                        if self.listnum[k][j]!=0 and k>num:
                            num=k
                    #switch the num in current place and the place found
                    if num!=-1:
                        self.listnum[i][j]=self.listnum[num][j]
                        self.listnum[num][j]=0
        #find all the places where the number is 0 and give it a new number                       
        for i in range(0,8):
            for j in range(0,8):
                if self.listnum[i][j]==0:
                    self.listnum[i][j]=random.randint(1,6)
        self.checkmatch()                              
                    
    def remove(self):
        #change the number in the list into 0
        #print "list",self.ellist
        for i in self.ellist:
            x=i/8
            y=i%8
            self.listnum[x][y]=0
        self.ellist=[]
        
    def rowmatch(self,x,y):
        count=0
        if y==0:
            #three match
            if self.listnum[x][y]==self.listnum[x][y+1] and self.listnum[x][y+1]==self.listnum[x][y+2]:
                count=3
                n=8*x+y
                #add the place in the list
                self.ellist.append(n)
                self.ellist.append(n+1)
                self.ellist.append(n+2)
        elif y==1:
            #four and three match
            if self.listnum[x][y]==self.listnum[x][y+1] and self.listnum[x][y+1]==self.listnum[x][y+2] and self.listnum[x][y-1]==self.listnum[x][y]:
                count=4
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+1)
                self.ellist.append(n+2)
                self.ellist.append(n-1)
            elif self.listnum[x][y]==self.listnum[x][y+1] and self.listnum[x][y+1]==self.listnum[x][y+2]:
                count=3
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+1)
                self.ellist.append(n+2)
            elif self.listnum[x][y]==self.listnum[x][y+1] and self.listnum[x][y]==self.listnum[x][y-1]:
                count=3
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+1)
                self.ellist.append(n-1)
        elif y==6:
            if self.listnum[x][y]==self.listnum[x][y+1] and self.listnum[x][y]==self.listnum[x][y-1] and self.listnum[x][y-1]==self.listnum[x][y-2]:
                count=4
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+1)
                self.ellist.append(n-1)
                self.ellist.append(n-2)
            elif self.listnum[x][y]==self.listnum[x][y+1] and self.listnum[x][y]==self.listnum[x][y-1]:
                count=3
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+1)
                self.ellist.append(n-1)
            elif self.listnum[x][y]==self.listnum[x][y-1] and self.listnum[x][y]==self.listnum[x][y-2]:
                count=3
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n-2)
                self.ellist.append(n-1)
        elif y==7:
            if self.listnum[x][y]==self.listnum[x][y-1] and self.listnum[x][y-1]==self.listnum[x][y-2]:
                count=3
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n-2)
                self.ellist.append(n-1)
        else:
            if self.listnum[x][y]==self.listnum[x][y+1] and self.listnum[x][y+1]==self.listnum[x][y+2] and self.listnum[x][y]==self.listnum[x][y-1] and self.listnum[x][y-1]==self.listnum[x][y-2]:
                count=5
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+1)
                self.ellist.append(n+2)
                self.ellist.append(n-1)
                self.ellist.append(n-2)
            elif self.listnum[x][y]==self.listnum[x][y+1] and self.listnum[x][y+1]==self.listnum[x][y+2] and self.listnum[x][y]==self.listnum[x][y-1]:
                count=4
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+1)
                self.ellist.append(n+2)
                self.ellist.append(n-1)
            elif self.listnum[x][y]==self.listnum[x][y+1] and self.listnum[x][y]==self.listnum[x][y-1] and self.listnum[x][y-1]==self.listnum[x][y-2]:
                count=4
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+1)
                self.ellist.append(n-2)
                self.ellist.append(n-1)
            elif self.listnum[x][y]==self.listnum[x][y+1] and self.listnum[x][y]==self.listnum[x][y-1]:
                count=3
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+1)
                self.ellist.append(n-1)
            elif self.listnum[x][y]==self.listnum[x][y+1] and self.listnum[x][y]==self.listnum[x][y+2]:
                count=3
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+1)
                self.ellist.append(n+2)
            elif self.listnum[x][y]==self.listnum[x][y-1] and self.listnum[x][y]==self.listnum[x][y-2]:
                count=3
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n-1)
                self.ellist.append(n-2)
        return count
        
    def colmatch(self,x,y):
        count=0
        if x==0:
            if self.listnum[x][y]==self.listnum[x+1][y] and self.listnum[x][y]==self.listnum[x+2][y]:
                count=3
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+8)
                self.ellist.append(n+16)
        elif x==1:
            if self.listnum[x][y]==self.listnum[x+1][y] and self.listnum[x][y]==self.listnum[x+2][y] and self.listnum[x][y]==self.listnum[x-1][y]:
                count=4
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+8)
                self.ellist.append(n+16)
                self.ellist.append(n-8)
            elif self.listnum[x][y]==self.listnum[x+1][y] and self.listnum[x][y]==self.listnum[x+2][y]:
                count=3
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+8)
                self.ellist.append(n+16)
            elif self.listnum[x][y]==self.listnum[x+1][y] and self.listnum[x][y]==self.listnum[x-1][y]:
                count=3
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+8)
                self.ellist.append(n-8)
        elif x==6:
            if self.listnum[x][y]==self.listnum[x+1][y] and self.listnum[x][y]==self.listnum[x-1][y] and self.listnum[x][y]==self.listnum[x-2][y]:
                count=4
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+8)
                self.ellist.append(n-16)
                self.ellist.append(n-8)
            elif self.listnum[x][y]==self.listnum[x-1][y] and self.listnum[x][y]==self.listnum[x-2][y]:
                count=3
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n-8)
                self.ellist.append(n-16)
            elif self.listnum[x][y]==self.listnum[x+1][y] and self.listnum[x][y]==self.listnum[x-1][y]:
                count=3
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+8)
                self.ellist.append(n-8)
        elif x==7:
            if self.listnum[x][y]==self.listnum[x-1][y] and self.listnum[x][y]==self.listnum[x-2][y]:
                count=3
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n-8)
                self.ellist.append(n-16)
        else:
            if self.listnum[x][y]==self.listnum[x+1][y] and self.listnum[x][y]==self.listnum[x-1][y] and self.listnum[x][y]==self.listnum[x-2][y] and self.listnum[x][y]==self.listnum[x+2][y]:
                count=5
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+8)
                self.ellist.append(n-16)
                self.ellist.append(n-8)
                self.ellist.append(n+16)
            elif self.listnum[x][y]==self.listnum[x+1][y] and self.listnum[x][y]==self.listnum[x-1][y] and self.listnum[x][y]==self.listnum[x-2][y]:
                count=4
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+8)
                self.ellist.append(n-16)
                self.ellist.append(n-8)
            elif self.listnum[x][y]==self.listnum[x+1][y] and self.listnum[x][y]==self.listnum[x+2][y] and self.listnum[x][y]==self.listnum[x-1][y]:
                count=4
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+8)
                self.ellist.append(n+16)
                self.ellist.append(n-8)
            elif self.listnum[x][y]==self.listnum[x-1][y] and self.listnum[x][y]==self.listnum[x-2][y]:
                count=3
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n-8)
                self.ellist.append(n-16)
            elif self.listnum[x][y]==self.listnum[x+1][y] and self.listnum[x][y]==self.listnum[x-1][y]:
                count=3
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+8)
                self.ellist.append(n-8)
            elif self.listnum[x][y]==self.listnum[x+1][y] and self.listnum[x][y]==self.listnum[x+2][y]:
                count=3
                n=8*x+y
                self.ellist.append(n)
                self.ellist.append(n+8)
                self.ellist.append(n+16)
        return count
game()
