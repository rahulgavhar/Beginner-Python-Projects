#Requirements: Python 3.6.5 or higher, OpenCV 4.5.1 or higher
#Folders: Resize Image > Input, Output, Dustbin

import cv2
import os

directory="Resize Image/Input"
filenames=os.listdir(directory)

try:
    for file_name in filenames:
        if file_name.endswith(".jpg") or file_name.endswith(".png"):
            filename=file_name
            break
        else:
            raise Exception("No image file found in the 'Resize Image/Input' Folder")
    else:
        raise Exception("No image file found in the 'Resize Image/Input' Folder")

    src = cv2.imread(f"Resize Image/Input/{filename}", cv2.IMREAD_UNCHANGED)

    scale_percent = int(input("Enter the \'%\' by which you want to scale your image: "))
    
    new_width = int(src.shape[1] * scale_percent / 100)
    new_height = int(src.shape[0] * scale_percent / 100)
    dim = (new_width, new_height)
    output = cv2.resize(src, dim)
    cv2.imwrite(f"Resize Image/Output/{filename.split('.')[0]}_resized.jpg", output)
    cv2.waitKey(0)
    
    # Removing the image from the input directory to dustbin folder
    os.makedirs("Resize Image/Dustbin", exist_ok=True)
    os.rename(f"Resize Image/Input/{filename}", f"Resize Image/Dustbin/{filename}")
    print("Image resized successfully (location: Resize Image/Output)")
except Exception as e:
    print("Error: ",e)