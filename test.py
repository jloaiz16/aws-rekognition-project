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

   # maxResults=2
   # collectionId='MyCollection'
    #Create a collection
   # print('Creating collection:' + collectionId)
   # response=client.create_collection(CollectionId=collectionId)
   # print('Collection ARN: ' + response['CollectionArn'])
   # print('Status code: ' + str(response['StatusCode']))
   # print('Done...')


#response = client.start_face_search(
#    Video={
#        'S3Object': {
#            'Bucket': bucketin,
#            'Name': fileName
#        }
#    },
#    ClientRequestToken= "LabelDetectionToken",
#    FaceMatchThreshold=50,
#    CollectionId= collectionId,
#    NotificationChannel={
#        'SNSTopicArn': "aws:rekognition:us-east-1:132922020722:collection/MyCollection",
#        'RoleArn': "arn:aws:iam::132922020722:group/gteam"
#    },
#    JobTag="DetectingLabels"
#)

response = client.start_face_detection(
    Video={
        'S3Object': {
            'Bucket': bucketin,
            'Name': fileName,
        }
    },
    ClientRequestToken="LabelDetectionToken",
    #NotificationChannel={
    #    'SNSTopicArn': 'string',
    #    'RoleArn': 'string'
    #},
    FaceAttributes= "ALL",
    JobTag='string',
)

#Funciona
############################################
#response = client.start_label_detection(
#    Video={
#        'S3Object': {
#            'Bucket': bucketin,
#            'Name': fileName
#        }
#    },
#    ClientRequestToken="LabelDetectionToken",
#    MinConfidence=50,
    #NotificationChannel={
    #    'SNSTopicArn': 'string',
    #    'RoleArn': 'string'
    #},

#    JobTag='string'
#)
############################################

#response = client.get_label_detection(
#    JobId='string',
#    MaxResults=123,
#    NextToken='string',
#    SortBy='NAME'|'TIMESTAMP'
#)
print(response)