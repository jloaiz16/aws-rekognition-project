import boto3
import json
import cv2
import cv2 as cv
import os
from PIL import Image

rekognition = boto3.client('rekognition', 'us-east-1')

def get_frame_rate(video):
    # Find OpenCV version
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

    if int(major_ver)  < 3 :
        fps = video.get(cv2.cv.CV_CAP_PROP_FPS)
    else:
        fps = video.get(cv2.CAP_PROP_FPS)
    print "Fotogramas por segundo del video: {0}".format(fps)

    return fps

def get_all_frames(video, path_output_dir):
    vidcap = cv2.VideoCapture(video)
    count = 0
    while vidcap.isOpened():
        success, image = vidcap.read()
        if success:
            cv2_im = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            count += 1
        else:
            break
    cv2.destroyAllWindows()
    vidcap.release()

def get_frames_every_x_sec(video, secs=1, fmt='opencv'):
    print(cv2.__version__)
    vidcap = cv2.VideoCapture(video)
    fps = get_frame_rate(vidcap)
    inc = int(fps * secs)
    length = int(vidcap.get(cv2.CAP_PROP_FPS))
    count = 0
    while vidcap.isOpened() and count <= length:
        if count % inc == 0:
            success, image = vidcap.read()
            if success:
                cv2_im = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                if fmt == 'PIL':
                    im = Image.fromarray(cv2_im)
                else:
                    im = cv2_im
                yield count, im
            else:
                break
        count += 1
    cv2.destroyAllWindows()
    vidcap.release()

def write_labels(name, video, label_dict, secs=1):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(video)
    w=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH ))
    h=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT ))
    out = cv2.VideoWriter('output.mp4', -1, 20.0, (w,h))

    f_no = 0
    fps = get_frame_rate(cap)
    inc = int(fps * secs)

    f_nos = label_dict.keys()
    lbl = ''
    while(cap.isOpened()):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
                    #print("Entro a dibujar")
                    cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                    #verifypersonphoto(frame)
                    cv2.putText(frame,name,(x+w-85,y+h+20),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8,(255, 0, 0))
                    roi_gray = gray[y:y+h, x:x+w]
                    roi_color = frame[y:y+h, x:x+w]

        if ret==True:
            if f_no in f_nos:
                try:
                    lbls = label_dict[f_no]
                    lbl = ",".join(lbls.keys())
                except:
                    pass
            cv2.putText(frame,lbl,(25, 25),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8,(235, 242, 247))
        else:
            break

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        #inc
        f_no += 1

    cap.release()
    out.release()
    cv2.destroyAllWindows()
