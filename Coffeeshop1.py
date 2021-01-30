'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import cv2
import numpy as np
import pandas as pd
import argparse


img = cv2.imread(&#39;colorpic.jpg&#39;)

clicked=False
r=g=b=xpos=ypos=0
index=[&quot;color&quot;,&quot;color_name&quot;,&quot;hex&quot;,&quot;R&quot;,&quot;G&quot;,&quot;B&quot;]
csv=pd.read_csv(&#39;colors.csv&#39;,names=index, header=None)
ing color
def getColorName(R,G,B):
    minimum=10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,&quot;R&quot;])) + abs(G- int(csv.loc[i,&quot;G&quot;]))+ abs(B-
 int(csv.loc[i,&quot;B&quot;]))
        if(d&lt;=minimum):
            minimum = d
            cname = csv.loc[i,&quot;color_name&quot;]
    return cname
def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked=True
        xpos=x
        ypos=y
        b,g,r=img[y,x]
        b=int(b)
        g=int(g)
        r=int(r)
    
cv2.namedWindow(&#39;image&#39;)
cv2.setMouseCallback(&#39;image&#39;,draw_function)