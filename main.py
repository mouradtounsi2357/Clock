import pygame, math, sys
from datetime import datetime

# initiation pygame --------------------------$
pygame.init()
width,height=200,200
display=pygame.display.set_mode((width,height))
pygame.display.set_caption("watch")
clock=pygame.time.Clock()
fps=60

# classes -------------------------------------$
class Time_ac():
    def __init__(self):
        self.hr=0
        self.mn=0
        self.sc=0
    
    def update(self):
        time = datetime.now()
        self.hr=time.hour
        self.mn=time.minute
        self.sc=time.second
        
class Show_time():
    def __init__(self):
        self.pos=(int(width/2),int(height/2))
        self.color1=(0xfc,0x21,0xeb)
        self.color2=(0x8a,0x21,0xfc)
        self.color3=(0x21,0xd3,0xfc)
        self.size1=60
        self.size2=50
        self.size3=30
    
    def draw(self):
        pygame.draw.line(display,self.color1,self.pos,(self.pos[0]+int(self.size1*math.cos((-PI/2)+2*PI*(tm.sc/60))),self.pos[1]+int(self.size1*math.sin((-PI/2)+2*PI*(tm.sc/60)))),2)
        pygame.draw.line(display,self.color2,self.pos,(self.pos[0]+int(self.size2*math.cos((-PI/2)+2*PI*(tm.mn/60))),self.pos[1]+int(self.size2*math.sin((-PI/2)+2*PI*(tm.mn/60)))),2)
        pygame.draw.line(display,self.color3,self.pos,(self.pos[0]+int(self.size3*math.cos((-PI/2)+2*PI*(tm.hr/12))),self.pos[1]+int(self.size3*math.sin((-PI/2)+2*PI*(tm.hr/12)))),2)

        k=25
        k1=20
        k2=15
        rect=pygame.Rect(stm.pos[0]-stm.size1-k,stm.pos[1]-stm.size1-k,2*stm.size1+2*k,2*stm.size1+2*k)
        pygame.draw.arc(display, self.color1,rect, -((2*PI)*tm.sc/60)%(2*PI)+PI/2+0.00001, PI/2, 3)

        rect=pygame.Rect(stm.pos[0]-stm.size1-k1,stm.pos[1]-stm.size1-k1,2*stm.size1+2*k1,2*stm.size1+2*k1)
        pygame.draw.arc(display, self.color2,rect, -((2*PI)*tm.mn/60)%(2*PI)+PI/2+0.00001, PI/2, 3)
        
        rect=pygame.Rect(stm.pos[0]-stm.size1-k2,stm.pos[1]-stm.size1-k2,2*stm.size1+2*k2,2*stm.size1+2*k2)
        pygame.draw.arc(display, self.color3,rect, -((2*PI)*tm.hr/12)%(2*PI)+PI/2+0.00001, PI/2, 3)
        
        

# setup --------------------------------------$
tm=Time_ac()
PI=math.pi
stm=Show_time()

# main loop ----------------------------------$
while 1:
    # logic ----------------------------------$
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tm.update()

    # draw -----------------------------------$
    display.fill((0,0,30))
    stm.draw()
    
    # update ---------------------------------$
    pygame.display.flip()
    clock.tick(fps)

