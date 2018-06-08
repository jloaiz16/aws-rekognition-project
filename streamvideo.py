import numpy as np
import cv2
import boto3

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
name = "Desconocido"
bucket = "camiloin"

def getvideorekognition():
    print("Ingrese 1: Si quiere verificar persona")
    option = input()

    if option == 1:
        file_im = raw_input("Ingrese nombre de imagen de persona a verificar: ")
        name = raw_input("Ingrese nombre de la persona")
        
        client=boto3.client('rekognition')

        cap = cv2.VideoCapture(0)
        while 1:
            ret, img = cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)


            #with open(img, 'rb') as image:
            #    response=client.compare_faces(SimilarityThreshold=70,
            #                                  SourceImage={'S3Object':{'Bucket':bucket,'Name':file_im}},
            #                                  TargetImage={'Bytes': image})
            #    print(response)
            


            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                cv2.putText(img,name,(x+w-85,y+h+20),cv2.FONT_HERSHEY_COMPLEX_SMALL,0.8,(255, 0, 0))
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]

            cv2.imshow('img',img)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

        cap.release()
        cv2.destroyAllWindows()
