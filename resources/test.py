import boto3
import json
from PIL import Image

if _name_ == "_main_":
    s3 = boto3.resource('s3')
    client = boto3.client('rekognition', 'us-east-1')
    fileName = 'video.mp4'
    bucketin = 'camiloin'
    bucketout = 'camiloout'   

    my_bucket = s3.Bucket(bucketin)

    response = client.start_face_search(
      Video={
          'S3Object': {
              'Bucket': bucketin,
              'Name': fileName
          }
      },
      ClientRequestToken= "LabelDetectionToken",
      FaceMatchThreshold=50,
      CollectionId= collectionId,
      NotificationChannel={
          'SNSTopicArn': "aws:rekognition:us-east-1:132922020722:collection/MyCollection",
          'RoleArn': "arn:aws:iam::132922020722:group/gteam"
      },
      JobTag="DetectingLabels"
  )
  print(response)