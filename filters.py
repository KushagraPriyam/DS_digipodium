import cv2

path=r"C:\Users\kusha\OneDrive\Documents\video_sample.mp4"
video=cv2.VideoCapture(path)

while True:
    state,frame=video.read()
    if not state:
        break
    frame= cv2.resize(frame,(0,0),fx=0.5,fy=0.5)
    gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)    #convert color to
    rgb= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV_FULL)
    
    '''cv2.imshow('video',frame)
    cv2.imshow('video b/w',gray)    #running video with given filter
    cv2.imshow('video rgb',rgb)     # imshow names must be alsways unique
    cv2.imshow('video hsv',hsv)'''
    
    s1= cv2.hconcat([frame,cv2.merge([gray,gray,gray])])    #gray is padded to match size of frame
    s2= cv2.hconcat([rgb,hsv])  #horizontally concatinate rgb and hsv as s2
    f= cv2.vconcat([s1,s2])    #vertically concatinate s1 and s2 to make a complete window of 4 videos
    h,w,_= f.shape
    
    #adding text
    f=cv2.putText(f,'original', (50,100),
                  cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),5)
    f=cv2.putText(f,'grayscale', (w//2+50,100),
                  cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,255),5)
    f=cv2.putText(f,'RGB', (50,h//2+100),
                  cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0),5)
    f=cv2.putText(f,'HSV', (w//2+100,h//2+100),
                  cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,255),5)
    
    cv2.imshow('frame',f)
    
    if cv2.waitKey(10) == ord('q'):
        break
    