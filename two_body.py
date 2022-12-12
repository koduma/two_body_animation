import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
 
def calc(tmax):
    x=1.0
    y=0.0
    vx=0.0
    vy=1.0
    dt=0.1
    print_x10=0
    print_x11=0
    print_x20=x
    print_x21=y
    
    for t in np.arange(0.0, tmax, dt):
        obj =math.sqrt((x*x)+(y*y))
        x =x +dt*vx
        y =y +dt*vy
        vx=vx+(dt*(-x/(obj*obj)))
        vy=vy+(dt*(-y/(obj*obj)))
        x_com0=(print_x10+print_x20)/2.0          
        x_com1=(print_x11+print_x21)/2.0
        print_x10=x_com0-(x/2.0)
        print_x11=x_com1-(y/2.0)
        print_x20=x_com0+(x/2.0)
        print_x21=x_com1+(y/2.0)
        
    return print_x10, print_x11, print_x20, print_x21
    
    
fig = plt.figure()
 
ims = []
 
for ttt in np.arange(0.0,100.0,0.1):
    aaa, bbb, ccc, ddd = calc(ttt)
    plt.xlim([-0.2,1.5])
    plt.ylim([-1.0,1.0])
    im2=plt.plot(aaa,bbb,ccc,ddd,marker='o',color="k",markersize=10)
    #plt.draw()
    #plt.pause(0.01)
    #plt.clf()
    ims.append(im2)

ani = animation.ArtistAnimation(fig, ims, interval=10)
plt.show()
