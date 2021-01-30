'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
while(1):
    cv2.imshow(&quot;image&quot;,img)
    if (clicked):
   

        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-
1 fills entire rectangle 
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
        #Creating text string to display( Color name and RGB values )
        text = getColorName(r,g,b) + &#39; R=&#39;+ str(r) +&#39; G=&#39;+ str(g) +  &#39; B=&#39;+ st
r(b)
        
        #cv2.putText(img,text,start,font(0-
7),fontScale,color,thickness,lineType )
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        #For very light colours we will display text in black colour
        if(r+g+b&gt;=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
        clicked=False
    #Break the loop when user hits &#39;esc&#39; key    
    if cv2.waitKey(20) &amp; 0xFF ==27:
        break
   
cv2.destroyAllWindows()