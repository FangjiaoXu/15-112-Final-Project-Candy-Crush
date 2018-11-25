import pygame
import gamegame

imagered="red.png"
imageyellow="yellow.png"
imageorange="orange.png"
imagegreen="green.png"
imageblue="blue.png"
imagepurple="purple.png"


class gameboard:
    def __init__(self): 
        pygame.init()
        self.screen = pygame.display.set_mode((600, 500))
        self.game=gamegame.game()
        screen=self.screen
        white=[255, 255, 255]
        black=[0,0,0]
        screen.fill(white)
        pygame.display.set_caption('Candy Crush')
        self.images={1:pygame.image.load(imagered).convert_alpha(),
        2:pygame.image.load(imageyellow).convert_alpha(),
        3:pygame.image.load(imageorange).convert_alpha(),
        4:pygame.image.load(imagegreen).convert_alpha(),
        5:pygame.image.load(imageblue).convert_alpha(),
        6:pygame.image.load(imagepurple).convert_alpha()}
        self.drawlines()
        self.getboard()
        pygame.display.flip()
        poslist=[]
        time=pygame.time.get_ticks()
        seconds=(pygame.time.get_ticks()-time)/1000
        running = 1
        while seconds<120 and running:
            seconds=(pygame.time.get_ticks()-time)/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running=0
                if event.type==pygame.MOUSEBUTTONUP:
                    pos=pygame.mouse.get_pos()
                    #position[0] is row num
                    #position[1] is col num
                    position=self.getindex(pos[0],pos[1])
                    if position!=[]:
                        poslist.append(position[0])
                        poslist.append(position[1])
                    if len(poslist)==4:
                        x1=poslist[0]
                        y1=poslist[1]
                        x2=poslist[2]
                        y2=poslist[3]
                        if (x1==x2 and abs(y1-y2)==1) or (y1==y2 and abs(x1-x2)==1):
                            self.game.changepos(poslist[0],poslist[1],poslist[2],poslist[3])
                            self.updateboard(poslist[0],poslist[1],poslist[2],poslist[3])
                            self.game.countmatch(poslist[0],poslist[1],poslist[2],poslist[3])
                            if self.game.count==0:
                                self.game.changepos(poslist[0],poslist[1],poslist[2],poslist[3])
                                self.updateboard(poslist[0],poslist[1],poslist[2],poslist[3])
                            else: 
                                self.game.makemove(poslist[0],poslist[1],poslist[2],poslist[3])
                                self.getboard()
                        #print poslist
                        poslist=[]
    
                    #print position
                    #posrow=
                    #poscol=
     
        '''running = 1
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running=0'''
        pygame.quit()
        
    def updateboard(self,x1,y1,x2,y2):
        listnum=self.game.listnum
        screen=self.screen
        images=self.images
        ind1=listnum[x1][y1]
        pos1y=50*y1+51
        pos1x=50*x1+51
        screen.blit(images[ind1], (pos1y, pos1x))
        ind2=listnum[x2][y2]
        pos2y=50*y2+51
        pos2x=50*x2+51
        screen.blit(images[ind2], (pos2y, pos2x))
        pygame.display.update()
        
    def getindex(self,x,y):
        for i in range(0,8):
            for j in range(0,8):
                #ind=listnum[i][j]
                left=50*j+51
                up=50*i+51
                right=left+50
                down=up+50
                if left<x and right>x and up<y and down>y:
                    return [i,j]
        return []

    def getboard(self):
        listnum=self.game.listnum
        screen=self.screen
        images=self.images
        '''for i in listnum:
            print i'''
        for i in range(0,8):
            for j in range(0,8):
                ind=listnum[i][j]
                #x is row, y is col
                y=50*j+51
                x=50*i+51
                screen.blit(images[ind], (y, x))
        pygame.display.update()

    def drawlines(self):
        screen=self.screen
        black=[0,0,0]
        pygame.draw.line(screen,black,[50,50],[450,50],1)
        pygame.draw.line(screen,black,[50,100],[450,100],1)
        pygame.draw.line(screen,black,[50,150],[450,150],1)
        pygame.draw.line(screen,black,[50,200],[450,200],1)
        pygame.draw.line(screen,black,[50,250],[450,250],1)
        pygame.draw.line(screen,black,[50,300],[450,300],1)
        pygame.draw.line(screen,black,[50,350],[450,350],1)
        pygame.draw.line(screen,black,[50,400],[450,400],1)
        pygame.draw.line(screen,black,[50,450],[450,450],1)
        pygame.draw.line(screen,black,[50,50],[50,450],1)
        pygame.draw.line(screen,black,[100,50],[100,450],1)
        pygame.draw.line(screen,black,[150,50],[150,450],1)
        pygame.draw.line(screen,black,[200,50],[200,450],1)
        pygame.draw.line(screen,black,[250,50],[250,450],1)
        pygame.draw.line(screen,black,[300,50],[300,450],1)
        pygame.draw.line(screen,black,[350,50],[350,450],1)
        pygame.draw.line(screen,black,[400,50],[400,450],1)
        pygame.draw.line(screen,black,[450,50],[450,450],1)

gameboard()
              
