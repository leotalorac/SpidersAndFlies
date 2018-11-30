from graphics import *
import spider as sp
import fly as fl
import random as random
import time
import matplotlib.pyplot as plt
height = 600
wight = 1000
def main():
    # setup
    series = list()
    s =0
    spy =list()
    fli = list()
    nspiders = 80
    nflies = 170
    #import the points
    flyform = open("./forms/fly.form",'r')
    flypoints = flyform.readlines()
    spiderform = open("./forms/spider.form","r")
    spiderspoints = spiderform.readlines()
    #define world
    
    spiders = list()
    flies = list()
    #put init
    for i in range(nspiders):
        spiders.append(sp.spider(random.randint(0,wight),random.randint(0,height)))
    for i in range(nflies):
        flies.append(fl.fly(random.randint(0,wight),random.randint(0,height)))
    while(True):
        series.append(s)
        s+=1
        spy.append(len(spiders))
        fli.append(len(flies))
        # clear(win)
        # drawspiders(spiders,win,spiderspoints)    
        # drawflies(flies,win,flypoints)
        moveflies(flies)
        spidereat(spiders,flies)
        reproducespiders(spiders)
        reproduceflies(flies)
        print("Flies population:" + str(len(flies)))
        print("Spiders population: " + str(len(spiders)))
        if(len(flies) ==0 or len(spiders) == 0 or len(flies) >=30000):
            if len(flies) <=0:
                for i in range(nflies):
                        flies.append(fl.fly(random.randint(0,wight),random.randint(0,height)))
            elif len(spiders) <=0:
                for i in range(nspiders):
                        spiders.append(sp.spider(random.randint(0,wight),random.randint(0,height)))
            else:
                break   
        # time.sleep(.01)
    win = GraphWin("Spider and Flyes",wight,height)
    series.append(s)
    s+=1
    spy.append(len(spiders))
    fli.append(len(flies))
    print(spy)
    print(fli)
    # plt.subplot(211)
#     plot
    plt.plot(series,fli,label="Flies")
    plt.plot(series,spy,label="Spiders")
    plt.legend(bbox_to_anchor=(.8,1),loc=2,borderaxespad=0 )
    plt.show()
    # draw final
    clear(win)
    drawflies(flies,win,flypoints)
    drawspiders(spiders,win,spiderspoints)    
    win.getMouse()
    win.close()
def clear(window):
    for i in window.items[:]:
        i.undraw()
    window.update()
def drawspiders(elements,window,points):
    for i in elements:
        i.simpledraw(window)
        # i.putspider(window,points)
def drawflies(elements,window,points):
    for i in elements:
        i.simpledraw(window)
def moveflies(elements):
    for i in elements:
        i.move(wight,height)
def spidereat(spiders, flies):
    for i in spiders:
        i.eat(flies)
def reproducespiders(spiders):
    for i in spiders:
        i.reproduce(spiders,i)
def reproduceflies(flies):
    for i in flies:
        i.reproduce(flies,i)
main()