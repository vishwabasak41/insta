import os
from glob import glob
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage



def upload_func(pic):
	UPLOAD_TO_WIN=ClarifaiApp()
	UPLOAD_TO_WIN.inputs.create_image_from_filename('/home/vishwarupa/Documents/insta_clone/SIGNUP/media_root/'+pic)

	# UPLOAD_TO_WIN.models.create()
	model = UPLOAD_TO_WIN.models.get('UPLOAD_TO_WIN')
	image = ClImage(filename="/home/vishwarupa/Documents/insta_clone/SIGNUP/media_root/"+pic)
	predicted_val= model.predict([image])
	print type(predicted_val)





	# UPLOAD_TO_WIN.inputs.create_image_from_filename('/home/vishwarupa/Documents/insta_clone/SIGNUP/media_root/'+pic, concepts=['man'])

# img_path="/home/vishwarupa/Documents/insta_clone/SIGNUP/media_root"


# def create_image_set(img_path, concepts):
#     images = []
#     for file_path in glob(os.path.join(img_path, '*.jpg')):
#         print(file_path)
#         img = ClImage(filename=file_path, concepts=concepts)
#         images.append(img)

#     return images

# create_image_set(img_path,['man'])
