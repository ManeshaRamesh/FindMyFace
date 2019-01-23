import face_recognition
import os
import shutil 
import progressbar
from time import sleep
def main():
	try:
		
		#known images of people and their face encodongs
		print("\n\n")
		print("Initiating...")
		known_dir = "./known"
		counter = 0
		for file in os.listdir(known_dir):
			#ensures only one image has been added to the ./known directory
			if (counter != 0):
				print("You cannot add more than one pic in the ./known")
				print("Ensure that there is only one image in ./known")
				print("Terminating progam...")
				exit()
			image = face_recognition.load_image_file(known_dir+"/"+ file)
			face_encodings = face_recognition.face_encodings(image)[0]
			counter = counter+1

		# create a directory where the matched images will be copied to
		if (os.path.exists("./matched_images") == False):
			os.mkdir("matched_images")
		
		print("Directory created!") 
		print("Extracting face encodings and comparing images...")
		directory = "./unknown"

		#progress bar display
		maxvalue = len(os.listdir("./unknown"))
		bar = progressbar.ProgressBar(maxval=maxvalue, \
		    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])

		bar.start()
		#takes each image file in the unknown directory and compares face encodings
		i = 0
		for filename in os.listdir(directory):
			path = os.path.join(directory, filename)
			image_unknown = face_recognition.load_image_file(path)
			encodings_unknown = face_recognition.face_encodings(image_unknown)
			#if no face encodings are found, then get out of teh loop
			if len(encodings_unknown) == 0:
				# print("Cannot find face!")
				continue
			else: 
				face_encodings_unkown = face_recognition.face_encodings(image_unknown)[0]
				result = face_recognition.compare_faces([face_encodings], face_encodings_unkown)
				if(result == [True]):
					# copies the file into another directory
					shutil.copy(directory+"/"+filename, "./matched_images/")
			i = i +1
			bar.update(i)
			sleep(0.1)

		bar.finish()
		#terminating message
		print("Done!")
		print("Thank you! Bye!:)")

	except KeyboardInterrupt:
		# when program is interrupted
		print ("Program Terminated")
		print ("Bye :(")

main()