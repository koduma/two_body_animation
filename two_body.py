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
        ra =math.sqrt((x*x)+(y*y))
        ra3=ra*ra*ra
        k00=dt*vx
        k01=dt*vy
        k02=dt*(-x/ra3)
        k03=dt*(-y/ra3)
        x1 = x+(k00/2.0)
        y1 = y+(k01/2.0)
        vx1= vx+(k02/2.0)
        vy1= vy+(k03/2.0)
        rb = math.sqrt((x1*x1)+(y1*y1))
        rb3= rb*rb*rb
        k10=dt*vx1
        k11=dt*vy1
        k12=dt*(-x1/rb3)
        k13=dt*(-y1/rb3)
        x2 = x+(k10/2.0)
        y2 = y+(k11/2.0)
        vx2= vx+(k12/2.0)
        vy2= vy+(k13/2.0)
        rc = math.sqrt((x2*x2)+(y2*y2))
        rc3= rc*rc*rc
        k20=dt*vx2
        k21=dt*vy2
        k22=dt*(-x2/rc3)
        k23=dt*(-y2/rc3)
        x3 =x+k20
        y3 =y+k21
        vx3=vx+k22
        vy3=vy+k23
        rd = math.sqrt((x3*x3)+(y3*y3))
        rd3= rd*rd*rd
        k30=dt*vx3
        k31=dt*vy3
        k32=dt*(-x3/rd3)
        k33=dt*(-y3/rd3)
        x =x +(k00+(2.0*k10)+(2.0*k20)+k30)/6.0
        y =y +(k01+(2.0*k11)+(2.0*k21)+k31)/6.0
        vx=vx+(k02+(2.0*k12)+(2.0*k22)+k32)/6.0
        vy=vy+(k03+(2.0*k13)+(2.0*k23)+k33)/6.0            
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
