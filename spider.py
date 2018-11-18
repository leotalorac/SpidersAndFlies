from graphics import *
import random as random
import math 
class spider:
    def __init__(self,posx,posy):
        self.x = posx
        self.y = posy
        self.belly = 0
        self.live = 2
    def putspider(self,window,spiderspoints):        
        for i in spiderspoints:
            xs,ys = map(int,i.split())
            pt = Point(self.x+xs,self.y+ys)
            pt.setOutline("black")
            pt.draw(window)
        #eyes
        e1 = Point(self.x+7,self.y+8)
        e1.setOutline("yellow")
        e2 = Point(self.x+10,self.y+8)
        e2.setOutline("yellow")
        e1.draw(window)
        e2.draw(window)
    def eat(self,flies):
        a = 2
        for i in flies:
            d = math.sqrt(abs(self.x - i.x )) + math.sqrt(abs(self.y - i.y))
            if a == 0:
                break
            if(d <=20):
                self.x = i.x
                self.y = i.y
                flies.remove(i)
                self.belly+=1
                a-=1
                # break
        if(a == 2):
            self.live -=1
            # print(self.live)
    def reproduce(self,spiders, me):
        if self.live <=0:
            spiders.remove(me)
            # print("quit" + str(len(spiders)))
            return
        if self.belly >=4:
            numsons = random.randint(0,10)
            for i in range(numsons):
                sx = self.x + random.randint(0,20)
                sy = self.y + random.randint(0,20)
                tem = spider(sx,sy)
                spiders.append(tem)
            spiders.remove(me)