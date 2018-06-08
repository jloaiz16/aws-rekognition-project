# PROYECTO Final - AWSRekognitionProject  <h1>
# Tópicos especiales en telemática <h2>

## Miembros del equipo:
* Juan David Loaiza Botero
* Juan Camilo Gomez Ruiz
* Jorge Iván Ortiz Serna

## Problema elegido
Se dese construir un proyecto en el cual se puedan utilizar AWS Rekognition para identificar personas y relacionarlas en un tiempo y lugar, esto con la finalidad de evitar que los candidatos a ingresar a una empresa utilicen suplantadores para hacer trampa y pasar ya sean exámenes teóricos, prácticos o entrevistas. De esta forma, podemos ofrecer un producto que las empresas puedan usar para identificar si las personas que están evaluando para ingresar no usen suplantación en alguno de los procesos. El producto dirá el lugar en el que estuvo, cuanto tiempo estuvo y que porcentaje de acertividad tiene para identificar cada persona, por medio del procesamiento de vídeo de las cámaras de seguridad. Así, se evitarán fraudes y se podrá hacer una mejor elección de personal

## Herramientas usadas

* __AWS Rekognition:__ API de AWS que facilita la incorporación del análisis de imágenes y videos a sus aplicaciones. Usted tan solo debe suministrar una imagen o video a la API de Rekognition y el servicio identificará objetos, personas, texto, escenas y actividades, además de detectar contenido inapropiado.

* __AWS S3:__ Servicio de AWS para el almacenamiento en la nube, además de ofrecer la capacidad para recopilar, almacenar y analizar datos de manera simple, segura y a gran escala.

* __Open CV:__ Es una librería software open-source de visión artificial y machine learning. OpenCV provee una infraestructura para aplicaciones de visión artificial. Se usa en aplicaciones como la detección de intrusos en vídeos, monitorización de equipamientos, ayuda a navegación de robots, inspeccionar etiquetas en productos, etc.

## Configuración de ambiente

__Insatalar Python__

* $ sudo add-apt-repository ppa:deadsnakes/ppa
* $ sudo apt-get update
* $ sudo apt-get install python3.6

__Instalar Pip__

* $ sudo apt-get update && sudo apt-get -y upgrade
* $ sudo apt-get install python-pip
* $ pip -v

__Descargar e instalar cliente de AWS__

* $ sudo pip install awsebcli

__Descargar e instalar boto3__

* $ sudo pip install boto3

__Configurar llaves de acceso__

Se debe crear una la carpeta `./aws` en el direcotrio __home__, dentro de la carpeta se debe crear un archivo llamado `credentials` sin extensión. Dentro copiar el sigueinte codigo:

```java
  [default]
  aws_access_key_id = YOUR_ACCESS_KEY_ID
  aws_secret_access_key = YOUR_SECRET_ACCESS_KEY
```
 
 __Instalar OpenCV__
 * $ sudo apt-get install libopencv-dev python-opencv

 ## Correr el programa
 * $ python2.7 main_process_videorekognition.py
  
 ## URL's de referencia

 * Open CV Tutorial: https://docs.opencv.org/3.1.0/d7/d8b/tutorial_py_face_detection.html
 * AWS Rekognition Tutorial: https://docs.aws.amazon.com/rekognition/latest/dg/API_Video.html
