import boto3
import os
import json
from PIL import Image

if __name__ == "__main__":
    s3 = boto3.resource('s3')
    client = boto3.client('rekognition', 'us-east-1')
    KEY = os.urandom(32)
    fileName = 'images1.jpeg'
    bucketin = 'camiloin'
    bucketout = 'camiloout'   

    my_bucket = s3.Bucket(bucketin)

    emoticons = {
        "HAPPY": 'emoji/happy.png',
        "ANGRY": 'emoji/angry.png',
        "SURPRISED": 'emoji/surprised.png',
        "SAD": 'emoji/sad.png',
        "CALM": 'emoji/calm.png',
        "DISGUSTED": 'emoji/disgusted.png',
        "CONFUSED": 'emoji/confused.png',
        "UNKNOWN": 'emoji/unknown.png'
    }

    response = client.detect_faces(
        Image={
            'S3Object': {
                'Bucket': bucketin,
                'Name': fileName
            }
        }, Attributes=['ALL']
    )

    source_img = s3.Object(bucketin, fileName).get()
    im = Image.open(source_img.get('Body'))

    for face in response.get('FaceDetails'):

        w = face.get('BoundingBox').get('Width')
        h = face.get('BoundingBox').get('Height')
        l = face.get('BoundingBox').get('Left')
        t = face.get('BoundingBox').get('Top')

        x1 = im.size[0]*l
        y1 = im.size[1]*t

        x2 = x1+im.size[0]*w
        y2 = y1+im.size[1]*h

        fimemo = face.get('Emotions')[0].get('Type')
        imemo = Image.open(emoticons.get(fimemo))

        a = int(x2-x1)
        b = int(y2-y1)
        imemo = imemo.resize((a, b))

        im.paste(imemo, (int(x1), int(y1)), imemo)
    im.save("images1-emo.jpeg", "JPEG")
    print("Uploading S3 object with SSE-C")
    s3 = boto3.client('s3')
    s3.put_object(Bucket=bucketout,
              Key=fileName,
              Body=b'foobar',
              SSECustomerKey=KEY,
              SSECustomerAlgorithm='AES256')
    print("Done")

im.show()