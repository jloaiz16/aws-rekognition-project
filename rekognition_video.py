import boto3
import json
import pickle
import io
import os
import operator
import opencv_utils

from multiprocessing.dummy import Pool as ThreadPool
from threading import Lock

name = "unknown"
rekognition = boto3.client('rekognition', 'us-east-1')

persons = {}
d_index = {} # Elementos del video
label_counts = {}
lock = Lock()

# Obtener elementos del video y procesamiento de rostros
def get_labels(params):
    f, image = params

    try:
        #Generamos una imagen del video y se la pasamos a AWS
        resp = rekognition.detect_labels(Image={'Bytes': image.getvalue()})
        #Obtenemos los elementos que extraiga de la imagen
        labels = resp['Labels']

        dt = {}
        for v in labels:
            l = v['Name'].lower()
            c = v['Confidence']

            #Identificar persona
            if l == "person":
                print("Detected person")
                continue

            #Confirmamos buen porcentaje de acertividad
            if c < 60:
                continue

            dt[l] = c

            #Frecuencia de elementos en el video
            try:
                label_counts[l]
            except KeyError:
                label_counts[l] = 0
            label_counts[l] += 1
        #Mostramos elementos encontrados
        print(label_counts)

        #Procesamos los rostros encontrados en el video
        response = rekognition.detect_faces(Image={'Bytes': image.getvalue()}, Attributes=['ALL'])
        print(len(response))

        for face in response.get('FaceDetails'):


            w = face.get('BoundingBox').get('Width')
            h = face.get('BoundingBox').get('Height')
            l = face.get('BoundingBox').get('Left')
            t = face.get('BoundingBox').get('Top')

            print(face)
            #x1 = image.size[0]*l
            #y1 = image.size[1]*t

            #x2 = x1+image.size[0]*w
            #y2 = y1+image.size[1]*h

            print(face.get('Emotions')[0].get('Type'))

            #a = int(x2-x1)
            #b = int(y2-y1)

        lock.acquire()
        d_index[f] = dt
        lock.release()
    except Exception, e:
        print e

# Obtener elementos del video y procesamiento de rostros
def get_description(params):
    f, image = params
    cont = 0
    try:
        #Generamos una imagen del video y se la pasamos a AWS
        resp = rekognition.detect_labels(Image={'Bytes': image.getvalue()})
        #Obtenemos los elementos que extraiga de la imagen
        labels = resp['Labels']

        dt = {}
        for v in labels:
            l = v['Name'].lower()
            c = v['Confidence']

            #Identificar persona
            if l == "person":
                cont = cont + 1
                continue

            #Confirmamos buen porcentaje de acertividad
            if c < 60:
                continue

            dt[l] = c

            #Frecuencia de elementos en el video
            try:
                label_counts[l]
            except KeyError:
                label_counts[l] = 0
            label_counts[l] += 1
        #Mostramos elementos encontrados
        #print(label_counts)

        print("PERSONAS EN EL VIDEO: ")
        print(cont)

        claves = label_counts.keys()

        print("SE IDENTIFICAN LOS SIGUIENTES OBJETOS")
        print(claves)

        #Procesamos los rostros encontrados en el video
        response = rekognition.detect_faces(Image={'Bytes': image.getvalue()}, Attributes=['ALL'])
        print(len(response))

        for face in response.get('FaceDetails'):


            w = face.get('BoundingBox').get('Width')
            h = face.get('BoundingBox').get('Height')
            l = face.get('BoundingBox').get('Left')
            t = face.get('BoundingBox').get('Top')

            #print(face)
            #x1 = image.size[0]*l
            #y1 = image.size[1]*t

            #x2 = x1+image.size[0]*w
            #y2 = y1+image.size[1]*h

            print(face.get('Emotions')[0].get('Type'))

            #a = int(x2-x1)
            #b = int(y2-y1)

        lock.acquire()
        d_index[f] = dt
        lock.release()
    except Exception, e:
        print e


#if __name__ == '__main__' :

def build_reckognition(video_file, name):
    frames = []
    for f_no, img in opencv_utils.get_frames_every_x_sec(video_file, secs=1, fmt="PIL"):
        b_img = io.BytesIO()
        img.save(b_img, format='PNG')
        frames.append([f_no, b_img])

    N_THREADS = 25
    pool = ThreadPool(N_THREADS)
    results = pool.map(get_labels, frames)
    pool.close()
    pool.join()
    #print "done"

    #Corremos el video con identificacion de los rostros
    opencv_utils.write_labels(name, video_file, d_index)

def getvideodetails(video_file):
    frames = []
    for f_no, img in opencv_utils.get_frames_every_x_sec(video_file, secs=1, fmt="PIL"):
        b_img = io.BytesIO()
        img.save(b_img, format='PNG')
        frames.append([f_no, b_img])

    N_THREADS = 25
    pool = ThreadPool(N_THREADS)
    results = pool.map(get_description, frames)
    pool.close()
    pool.join()
    #print "done"

def setnameperson(im_name):
    name = im_name
