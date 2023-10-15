#Requirements: Python 3.6.5 or higher, OpenCV 4.5.1 or higher, pillow module
#Folders: Image Operation > Input, Output, Dustbin, imageresizer.py

import cv2
import os
from PIL import Image

#finding the image file in the directory
directory="Image Operation/Input"
filenames=os.listdir(directory)
try:
    for file_name in filenames:
        if file_name.endswith(".jpg") or file_name.endswith(".png"):
            filename=file_name
            run="yes"
            break
        else:
            raise Exception("No image file found in the 'Image Operation/Input' Folder")
    else:
        raise Exception("No image file found in the 'Image Operation/Input' Folder")
except Exception as e:
    run="no"
    print("Error: ",e)

if run=="yes":
    method=input("Enter the operation for image\n1. Change File Size\n2. Change Dimensions\nEnter 1 or 2: ")

    if method=="1":
        original_size = os.path.getsize(f"Image Operation/Input/{filename}")
        og_size_inmb=float(original_size/2**20)
        print(f"Original Size: {og_size_inmb} MB")
        qlt=int(input("Enter the new quality of the image (1-50)for compression, (50<)for expansion: "))
        image = Image.open(f"Image Operation/Input/{filename}")
        image.save(f"Image Operation/Output/{filename.split('.')[0]}_reduced.jpg", optimize=True, quality=qlt)
        compressed_size = os.path.getsize(f"Image Operation/Output/{filename.split('.')[0]}_reduced.jpg")
        cs_size_inmb=float(compressed_size/2**20)
        print(f"\nCompressed Size: {cs_size_inmb} MB\nCompression Percentage: {round((original_size-compressed_size)/original_size*100,2)}%")
        # Removing the image from the input directory to dustbin folder
        os.makedirs("Image Operation/Dustbin", exist_ok=True)
        os.rename(f"Image Operation/Input/{filename}", f"Image Operation/Dustbin/{filename}")
        print("Image reduced successfully (location: Image Operation/Output)")
    
    elif method=="2":
            src = cv2.imread(f"Image Operation/Input/{filename}", cv2.IMREAD_UNCHANGED)
            print(f'Original Dimensions (w*h): {src.shape[1]}x{src.shape[0]}')
            print("1. Dimensions to which you want to scale your image (width, height)\n2. The \'%\' to which you want to scale your image (dimensions)")
            dimorpercent=input("Enter 1 or 2: ")
            if dimorpercent=="1":
                while True:
                    try:
                        new_width=input("Enter the dimensions(width): ")
                        new_height=input("Enter the dimensions(height): ")
                        new_width = int(new_width)
                        new_height = int(new_height)
                        times_w=new_width/src.shape[1]
                        times_h=new_width/src.shape[0]
                        if times_w>100 or times_h>100:
                            raise Exception("The dimensions you entered are x100 greater than the original dimensions")
                        break
                    except Exception as e:
                        print(e)
                        continue
                    
            elif dimorpercent=="2":
                scale_percent = int(input("Enter the \'%\' to which you want to scale your image (dimensions): "))
                while True:
                    try:
                        if scale_percent<10000:
                            new_width = int(src.shape[1] * scale_percent / 100)
                            new_height = int(src.shape[0] * scale_percent / 100)
                        else:
                            raise Exception("The image cannot be scaled to more than 100 times or 10000% ")
                        break
                    except Exception as e:
                        print(e)
                        continue
            dim = (new_width, new_height)
            output = cv2.resize(src, dim)
            cv2.imwrite(f"Image Operation/Output/{filename.split('.')[0]}_resized.jpg", output)
            cv2.waitKey(0)
            
            # Removing the image from the input directory to dustbin folder
            os.makedirs("Image Operation/Dustbin", exist_ok=True)
            os.rename(f"Image Operation/Input/{filename}", f"Image Operation/Dustbin/{filename}")
            print("Image resized successfully (location: Image Operation/Output)")
