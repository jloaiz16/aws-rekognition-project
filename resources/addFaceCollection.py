import boto3
if __name__ == "__main__":
 	bucket='camiloin'
 	collectionId='MyCollection'
 	fileName='images1.jpeg'

 	client=boto3.client('rekognition')
 	response=client.index_faces
 	response=client.index_faces(CollectionId=collectionId,
 								Image={'S3Object':{'Bucket':bucket,'Name':fileName}},
 										ExternalImageId=fileName,
 								DetectionAttributes=['ALL'])
 	print ('Faces in ' + fileName)
 	for faceRecord in response['FaceRecords']:
 		print (faceRecord['Face']['FaceId']) 