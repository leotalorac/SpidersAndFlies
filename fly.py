from graphics import *
import random as random
class fly:
    def __init__(self,posx,posy):
        self.x = posx
        self.y = posy
        self.live = 2
    def putfly(self,window,flypoints):
        c = True
        for i in flypoints:
            xs,ys = map(int,i.split())
            if(xs == -1 and ys == -1):
                c = False
            else:
                pt = Point(self.x+xs,self.y+ys)
                if(c):
                    pt.setOutline('blue')
                else:
                    pt.setOutline("black")
                pt.draw(window)
    def simpledraw(self,window):
        pt = Point(self.x,self.y)
        pt.setOutline("blue")
        pt.draw(window)
    def move(self,w,h):
        xp = random.randint(-40,40)
        yp = random.randint(-40,40)
        self.x = (self.x+xp)%w
        self.y = (self.y+yp)%h
        self.live -=1
    def reproduce(self,flies,me):
        if self.live <=0:
            numsons = random.randint(2,10)
            for i in range(numsons):
                sx = self.x + random.randint(5,15)
                sy = self.y + random.randint(5,15)
                temf = fly(sx,sy)
                flies.append(temf)
            flies.remove(me)