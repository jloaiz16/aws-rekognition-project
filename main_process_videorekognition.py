import rekognition_video
import streamvideo

pointer = True

if __name__ == '__main__' :

	print("PROCESSING VIDEO SYSTEM v2.0")
	print("Face recognition ...")
	print("Escriba 1: Procesamiento video almacenado")
	print("Escriba 2: Procesamiento video en vivo")

	option = input()

	if option == 1 :

		file_vd = raw_input("Ingrese nombre de video a procesar con su extension: ")
		while pointer :
			print("Escriba 1: Obtener detalles del video")
			print("Escriba 2: Verificar si se encuentra persona especifica")

			option = input()

			if option == 1 :
				print("sd")
				#rekognition_video.getvideodetails()
			elif option == 2 :
				file_im = raw_input("Ingrese nombre de imagen de persona a verificar: ")
				im_name = raw_input("Ingrese nombre de la persona")
				rekognition_video.build_reckognition(file_vd, im_name)
				#rekognition_video.verifyperson()
			else :
				print("Opcion incorrecta")


			print("Escriba True: continuar | Escriba False: parar")
			pointer = bool(input())
		    #rekognition_video.build_reckognition(file_vd)
	elif option == 2 :
		streamvideo.getvideorekognition()
	else :
		print("Opcion incorrecta")