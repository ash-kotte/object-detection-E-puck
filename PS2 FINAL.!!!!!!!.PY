from controller import Robot, DistanceSensor, Motor, Camera, CameraRecognitionObject
import cv2
import numpy as np
#import math
# time in [ms] of a simulation step
TIME_STEP = 64

MAX_SPEED = 6.28

# create the Robot instance.
robot = Robot()

# initialize devices
prox_sensor=[]
for i in range(8):
  name='ps'+str(i)
  prox_sensor.append(robot.getDevice(name))
  prox_sensor[i].enable(TIME_STEP)


camera=robot.getDevice('camera')
camera.enable(TIME_STEP)
       
leftMotor = robot.getDevice('left wheel motor')
rightMotor = robot.getDevice('right wheel motor')
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

"""def MASK(IMAGE,LOWER,UPPER):
    
    img = cv2.cvtColor(IMAGE, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(img,LOWER,UPPER )
    res=cv2.bitwise_and(img,img, mask=mask)
    # Find the largest segmented contour (red ball) and it's center
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    #largest_contour = max(contours, key=cv2.contourArea)
    #largest_contour_center = cv2.moments(largest_contour)
    #center_x = int(largest_contour_center['m10'] / largest_contour_center['m00'])
    cv2.imshow('segment', res)
    cv2.waitKey(1)
    if(len(contours)>=1):
        contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)

        if(cv2.contourArea(contours[0])>500): 
            M= cv2.moments(contours[0])
  
            if(M['m00']!=0):
                cx = int(M['m10']/M['m00'])
                cy = int(M[ 'm01']/M[ 'm00'])
    cv2.imshow('img',IMAGE)
    cv2.imshow('mask',mask)
    cv2.imshow('result',res)

def blue(Image):
  lower_blue = np.array([94,80,2])
  upper_blue = np.array([126,255,255])
  return MASK(Image,lower_blue,upper_blue)

def red(Image):
  lower_red = np.array([161, 155, 84])
  upper_red = np.array([179, 255, 255])
  return  MASK(Image,lower_red,upper_red)

def green(Image):
    lower_green = np.array([25, 52, 72])
    upper_green = np.array([102, 255, 255])
    return MASK(Image,lower_green,upper_green)
#def purple(Image):"""
    
def get_image_from_camera():
  
    img = camera.getImageArray()
    img = np.asarray(img, dtype=np.uint8)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    return cv2.flip(img, 1)
leftMotor.setVelocity(0.0)
rightMotor.setVelocity(0.0)


        

    #GREEEEN
c=0
while robot.step(TIME_STEP) != -1:
    print(c)
    IMAGE = get_image_from_camera()
    
    if prox_sensor[7].getValue()>80 or prox_sensor[0].getValue()>80 or prox_sensor[1].getValue()>80 or prox_sensor[6].getValue()>80:
      
       leftMotor.setVelocity(MAX_SPEED)
       rightMotor.setVelocity(MAX_SPEED/10)
    if prox_sensor[7].getValue()<80 or prox_sensor[0].getValue()<80 or prox_sensor[1].getValue()<80 or prox_sensor[6].getValue()<80:
          leftMotor.setVelocity(MAX_SPEED)
          rightMotor.setVelocity(-MAX_SPEED)    
       #leftMotor.setVelocity(MAX_SPEED)
       #rightMotor.setVelocity(MAX_SPEED)
    else :
       if prox_sensor[5].getValue()>80:
         leftMotor.setVelocity(MAX_SPEED)
         rightMotor.setVelocity(MAX_SPEED)
       if prox_sensor[2].getValue()>80:
         leftMotor.setVelocity(MAX_SPEED)
         rightMotor.setVelocity(MAX_SPEED)
      
    img = cv2.cvtColor(IMAGE, cv2.COLOR_RGB2HSV)
    if c==0:
    #------------------------------------------------------------------------------------------------------
        print("green")
        leftMotor.setVelocity(MAX_SPEED)
        rightMotor.setVelocity(-MAX_SPEED)
        lower_green = np.array([25, 52, 72])
        upper_green = np.array([102, 255, 255])
        mask = cv2.inRange(img,lower_green,upper_green )
        res=cv2.bitwise_and(img,img, mask=mask)
        # Find the largest segmented contour (red ball) and it's center
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        #largest_contour = max(contours, key=cv2.contourArea)
        #largest_contour_center = cv2.moments(largest_contour)
        #center_x = int(largest_contour_center['m10'] / largest_contour_center['m00'])
        
        
       
            
        if(len(contours)>=1):
            contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    
            if(cv2.contourArea(contours[0])>500): 
                M= cv2.moments(contours[0])
      
                if(M['m00']!=0):
                    cx = int(M['m10']/M['m00'])
                    cy = int(M[ 'm01']/M[ 'm00'])
                           

        if np.count_nonzero(res)>0:
          print ("block detected1")
          leftMotor.setVelocity(0.0)
          rightMotor.setVelocity(0.0)
          leftMotor.setVelocity(MAX_SPEED)
          rightMotor.setVelocity(MAX_SPEED)
          if prox_sensor[7] .getValue()> 80 or prox_sensor[0].getValue() > 80 or prox_sensor[1].getValue()>80 or prox_sensor[6].getValue()>80 :
           
            c=1
            print(c)
            for i in range(30):
                robot.step(TIME_STEP)
                leftMotor.setVelocity(-MAX_SPEED)
                rightMotor.setVelocity(-MAX_SPEED)
                leftMotor.setVelocity(-MAX_SPEED)
                rightMotor.setVelocity(MAX_SPEED)
                leftMotor.setVelocity(MAX_SPEED)
                rightMotor.setVelocity(MAX_SPEED)
            leftMotor.setVelocity(0)
            rightMotor.setVelocity(0)
            """ #for i in range(5):
            leftMotor.setVelocity(MAX_SPEED)
            rightMotor.setVelocity(-MAX_SPEED) 
            n=10
            leftMotor.setVelocity(MAX_SPEED/10)
            rightMotor.setvelocity(10)"""
            """for b in range(10):
                leftMotor.setVelocity(MAX_SPEED)
                rightMotor.setVelocity(MAX_SPEED)""
              else:  
             leftMotor.setVelocity(MAX_SPEED)
             rightMotor.setVelocity(-MAX_SPEED)"""
        

      
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------            
    elif c==1:
        leftMotor.setVelocity(MAX_SPEED)
        rightMotor.setVelocity(-MAX_SPEED)
        print("blue")
        """if prox_sensor[7].getValue()<80 or prox_sensor[0].getValue()<80 or prox_sensor[1].getValue()<80 or prox_sensor[6].getValue()<80:
          leftMotor.setVelocity(0.0)
          rightMotor.setVelocity(0.0)"""
        """leftMotor.setVelocity(MAX_SPEED)
          rightMotor.setVelocity(-MAX_SPEED)
          leftMotor.setVelocity(MAX_SPEED)
          rightMotor.setVelocity(MAX_SPEED)
          leftMotor.setVelocity(MAX_SPEED)
          rightMotor.setVelocity(MAX_SPEED)
          leftMotor.setVelocity(MAX_SPEED)
          rightMotor.setVelocity(-MAX_SPEED)"""
        
        """for i in range(5):
            leftMotor.setVelocity(MAX_SPEED)
            rightMotor.setVelocity(-MAX_SPEED) 
        for b in range(10):
           leftMotor.setVelocity(MAX_SPEED)
           rightMotor.setVelocity(MAX_SPEED)"""
       
        lower_blue=np.array([116,109,56])
        upper_blue=np.array([122,225,119])

        mask = cv2.inRange(img,lower_blue,upper_blue )
        res=cv2.bitwise_and(img,img, mask=mask)
        # Find the largest segmented contour (red ball) and it's center
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        #largest_contour = max(contours, key=cv2.contourArea)
        #largest_contour_center = cv2.moments(largest_contour)
        #center_x = int(largest_contour_center['m10'] / largest_contour_center['m00'])
        print("____________")
       
            
        if(len(contours)>=1):
            contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    
            if(cv2.contourArea(contours[0])>500): 
                M= cv2.moments(contours[0])
      
                if(M['m00']!=0):
                    cx = int(M['m10']/M['m00'])
                    cy = int(M[ 'm01']/M[ 'm00'])
                          
        print("aaaaaaaaaaaaaaaaaaaaaaa")
        if np.count_nonzero(res)>0:
          print ("block detected2")
          leftMotor.setVelocity(0.0)
          rightMotor.setVelocity(0.0 )
          leftMotor.setVelocity(MAX_SPEED)
          rightMotor.setVelocity(MAX_SPEED)
        if  prox_sensor[7] .getValue()> 80 or prox_sensor[0].getValue() > 80 or prox_sensor[1].getValue()>80 or prox_sensor[6].getValue()>80 :
            c=2
            
            leftMotor.setVelocity(0.0)
            rightMotor.setVelocity(0.0)
            for i in range(30):
                robot.step(TIME_STEP)
                leftMotor.setVelocity(-MAX_SPEED)
                rightMotor.setVelocity(-MAX_SPEED)
                leftMotor.setVelocity(-MAX_SPEED)
                rightMotor.setVelocity(MAX_SPEED)
                leftMotor.setVelocity(MAX_SPEED)
                rightMotor.setVelocity(MAX_SPEED)
                
            
            leftMotor.setVelocity(0)
            rightMotor.setVelocity(0)
        print("bbbbbbbbbbbbbbbbbbbbbbb")
 
    """ else:  
           leftMotor.setVelocity(MAX_SPEED)
          rightMotor.setVelocity(-MAX_SPEED)"""
          
    if c==2:
        leftMotor.setVelocity(MAX_SPEED)
        rightMotor.setVelocity(-MAX_SPEED)
        print("purple")
        """if prox_sensor[7].getValue()<80 or prox_sensor[0].getValue()<80 or prox_sensor[1].getValue()<80 or prox_sensor[6].getValue()<80:
          leftMotor.setVelocity(0.0)
          rightMotor.setVelocity(0.0)"""
        """leftMotor.setVelocity(MAX_SPEED)
          rightMotor.setVelocity(-MAX_SPEED)
          leftMotor.setVelocity(MAX_SPEED)
          rightMotor.setVelocity(MAX_SPEED)
          leftMotor.setVelocity(MAX_SPEED)
          rightMotor.setVelocity(MAX_SPEED)
          leftMotor.setVelocity(MAX_SPEED)
          rightMotor.setVelocity(-MAX_SPEED)"""
        
        """for i in range(5):
            leftMotor.setVelocity(MAX_SPEED)
            rightMotor.setVelocity(-MAX_SPEED) 
        for b in range(10):
           leftMotor.setVelocity(MAX_SPEED)
           rightMotor.setVelocity(MAX_SPEED)"""
       
        lower_blue=np.array([125,137,49])
        upper_blue=np.array([151,209,215])

        mask = cv2.inRange(img,lower_blue,upper_blue )
        res=cv2.bitwise_and(img,img, mask=mask)
        # Find the largest segmented contour (red ball) and it's center
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        #largest_contour = max(contours, key=cv2.contourArea)
        #largest_contour_center = cv2.moments(largest_contour)
        #center_x = int(largest_contour_center['m10'] / largest_contour_center['m00'])
        print("____________")
       
            
        if(len(contours)>=1):
            contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    
            if(cv2.contourArea(contours[0])>500): 
                M= cv2.moments(contours[0])
      
                if(M['m00']!=0):
                    cx = int(M['m10']/M['m00'])
                    cy = int(M[ 'm01']/M[ 'm00'])
                          
        print("aaaaaaaaaaaaaaaaaaaaaaa")
        if np.count_nonzero(res)>0:
          print ("block detected3")
          leftMotor.setVelocity(0.0)
          rightMotor.setVelocity(0.0 )
          leftMotor.setVelocity(MAX_SPEED)
          rightMotor.setVelocity(MAX_SPEED)
        if  prox_sensor[7] .getValue()> 80 or prox_sensor[0].getValue() > 80 or prox_sensor[1].getValue()>80 or prox_sensor[6].getValue()>80 :
            c=3
            
            leftMotor.setVelocity(0.0)
            rightMotor.setVelocity(0.0)
            for i in range(30):
                robot.step(TIME_STEP)
                leftMotor.setVelocity(-MAX_SPEED)
                rightMotor.setVelocity(-MAX_SPEED)
                leftMotor.setVelocity(-MAX_SPEED)
                rightMotor.setVelocity(MAX_SPEED)
                leftMotor.setVelocity(MAX_SPEED)
                rightMotor.setVelocity(MAX_SPEED)
                
            
            leftMotor.setVelocity(0)
            rightMotor.setVelocity(0)
        print("bbbbbbbbbbbbbbbbbbbbbbb")
        
    elif c==3:
        leftMotor.setVelocity(MAX_SPEED)
        rightMotor.setVelocity(-MAX_SPEED)
        print("red")
        """if prox_sensor[7].getValue()<80 or prox_sensor[0].getValue()<80 or prox_sensor[1].getValue()<80 or prox_sensor[6].getValue()<80:
          leftMotor.setVelocity(0.0)
          rightMotor.setVelocity(0.0)"""
        """leftMotor.setVelocity(MAX_SPEED)
          rightMotor.setVelocity(-MAX_SPEED)
          leftMotor.setVelocity(MAX_SPEED)
          rightMotor.setVelocity(MAX_SPEED)
          leftMotor.setVelocity(MAX_SPEED)
          rightMotor.setVelocity(MAX_SPEED)
          leftMotor.setVelocity(MAX_SPEED)
          rightMotor.setVelocity(-MAX_SPEED)"""
        
        """for i in range(5):
            leftMotor.setVelocity(MAX_SPEED)
            rightMotor.setVelocity(-MAX_SPEED) 
        for b in range(10):
           leftMotor.setVelocity(MAX_SPEED)
           rightMotor.setVelocity(MAX_SPEED)"""
       
        lower_blue=np.array([161,39,0])
        upper_blue=np.array([179,255,255])

        mask = cv2.inRange(img,lower_blue,upper_blue )
        res=cv2.bitwise_and(img,img, mask=mask)
        # Find the largest segmented contour (red ball) and it's center
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        #largest_contour = max(contours, key=cv2.contourArea)
        #largest_contour_center = cv2.moments(largest_contour)
        #center_x = int(largest_contour_center['m10'] / largest_contour_center['m00'])
        print("____________")
       
            
        if(len(contours)>=1):
            contours = sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    
            if(cv2.contourArea(contours[0])>500): 
                M= cv2.moments(contours[0])
      
                if(M['m00']!=0):
                    cx = int(M['m10']/M['m00'])
                    cy = int(M[ 'm01']/M[ 'm00'])
                          
        print("aaaaaaaaaaaaaaaaaaaaaaa")
        if np.count_nonzero(res)>0:
          print ("block detected4")
          leftMotor.setVelocity(0.0)
          rightMotor.setVelocity(0.0 )
          leftMotor.setVelocity(MAX_SPEED)
          rightMotor.setVelocity(MAX_SPEED)
        if  prox_sensor[7] .getValue()> 80 or prox_sensor[0].getValue() > 80 or prox_sensor[1].getValue()>80 or prox_sensor[6].getValue()>80 :
            
            
            leftMotor.setVelocity(0.0)
            rightMotor.setVelocity(0.0)
            for i in range(30):
                robot.step(TIME_STEP)
                leftMotor.setVelocity(-MAX_SPEED)
                rightMotor.setVelocity(-MAX_SPEED)
                leftMotor.setVelocity(-MAX_SPEED)
                rightMotor.setVelocity(MAX_SPEED)
                leftMotor.setVelocity(MAX_SPEED)
                rightMotor.setVelocity(MAX_SPEED)
                
            
            leftMotor.setVelocity(0)
            rightMotor.setVelocity(0)
        print("bbbbbbbbbbbbbbbbbbbbbbb")
        
    cv2.imshow('img',IMAGE)
    cv2.imshow('mask',mask)
    cv2.imshow('result',res)
    cv2.imshow('segment', res)
    cv2.waitKey(1)
    
    
         
    pass
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------                   

        


cv2.waitKey(0)
cv2.destroyAllWindows(0)

  