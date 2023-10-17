import PyPDF2
from PyPDF2 import PdfReader, PdfWriter
import os
from typing import Union, Literal, List
from pathlib import Path
from pdf2image import convert_from_path
from PIL import Image

#finding the pdf file in the directory
directory="Pdf Operation/Input"
filenames=os.listdir(directory)
filtered_files = [file for file in filenames if (file.endswith(".pdf") or file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"))]
f_count=0
run="no"

if len(filtered_files)==0:
    print("No valid PDF/image file found in the 'Pdf Operation/Input' Folder")
else:
    print("PDF/image files found in the 'Pdf Operation/Input' Folder:\n",filtered_files,"\n")
    print("Enter the operation number\n1. Merge PDFs\n2. Add Password\n3. Remove Password\n4. Add WaterMark\n5. Reduce Size\n6. PDF to Image\n7. Image to PDF\n")
    while True:
        try:
            input_operation=input("\nEnter the operation number: ")
            if input_operation=="1" or input_operation=="2" or input_operation=="3" or input_operation=="4" or input_operation=="5" or input_operation=="6":
                xx=".pdf"
            elif input_operation=="7":
                while True:
                    check_img_files=[]
                    for file_name in filenames:
                        if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
                            check_img_files.append(file_name)
                    if len(check_img_files)==0:
                        xx=".xyz"
                        break
                    try:
                        xx=input("\nEnter the image file extension\n(eg- .jpg, .jpeg, .png): ")
                        if xx==".jpg" or xx==".jpeg" or xx==".png":
                            break
                        else:
                            raise Exception("Invalid Extension")
                    except Exception as e:
                        print("Error: ",e)
            else:
                raise Exception("Invalid Input")
            
            filenames_list=[]
            if len(filenames)>0:
                for file_name in filenames:
                    if not file_name.endswith(xx):
                        continue
                    if file_name.endswith(xx):
                        filename=file_name
                        filenames_list.append(filename)
                        f_count=len(filenames_list)
                if f_count>1 and input_operation=="1":
                    run="yes"
                elif f_count>1 and input_operation=="7":
                    run="yes"
                elif f_count>1:
                    raise Exception("More than 1 files are not accepted")
                elif f_count==1 and input_operation=="1":
                    raise Exception("Single PDF file is not accepted for Merging PDFs")
                elif f_count==1:
                    run="yes"
                break
            else:
                raise Exception("No valid PDF/image file found in the 'Pdf Operation/Input' Folder for your required operation")
                        
        except Exception as e:
            print("Error: ",e)

    if run=="yes":
        if input_operation=="1":
            print("Merging PDFs: ",filenames_list)
        elif input_operation=="2":
            print("Adding Password on: ",filename)
        elif input_operation=="3":
            print("Removing Password from: ",filename)
        elif input_operation=="4":
            print("Adding Watermark on: ",filename)
        elif input_operation=="5":
            print("Reducing Size of: ",filename)
        elif input_operation=="6":
            print("Converting PDF to Image: ",filename)
        elif input_operation=="7":
            print("Converting Images to PDF: ",filenames_list)
        
        if input_operation=="1":
            try:
                merger=PyPDF2.PdfWriter()
                for filename in filenames_list:
                    merger.append(f"Pdf Operation/Input/{filename}")
                output_file_name=input("Enter the output file name(excluding '.pdf'): ")
                merger.write(f"Pdf Operation/Output/{output_file_name}.pdf")
                print("PDFs merged successfully (location: Pdf Operation/Output)")
                status="success"
                confidential=input("Do you want to add a password to the merged File? (yes/no): ")
                if confidential=="yes":
                    reader=PdfReader(f"Pdf Operation/Output/{output_file_name}.pdf")
                    writer=PdfWriter()
                    for page in reader.pages:
                        writer.add_page(page)
                    password=input("Enter the password: ")
                    writer.encrypt(password)
                    writer.write(f"Pdf Operation/Output/{output_file_name}.pdf")
                    print("Password successfully Added(location: Pdf Operation/Output)")
            except:
                print("PDFs Merging Failed")
                status="failed"
            if status=="success":
                # Removing the pdf from the input directory to dustbin folder
                os.makedirs("Pdf Operation/Dustbin", exist_ok=True)
                for filename in filenames_list:
                    os.rename(f"Pdf Operation/Input/{filename}", f"Pdf Operation/Dustbin/{filename}")
            
        elif input_operation=="2":
            try:
                reader=PdfReader(f"Pdf Operation/Input/{filename}")
                writer=PdfWriter()
                for page in reader.pages:
                    writer.add_page(page)
                password=input("Enter the password: ")
                writer.encrypt(password)
                filename=filename.split(".")[0]
                writer.write(f"Pdf Operation/Output/{filename}_encrypted.pdf")
                print("Password successfully Added(location: Pdf Operation/Output)")
                status="success"
            except:
                print("**File is already encrypted**")
                status="failed"
            if status=="success":
                # Removing the pdf from the input directory to dustbin folder
                os.makedirs("Pdf Operation/Dustbin", exist_ok=True)
                for filename in filenames_list:
                    os.rename(f"Pdf Operation/Input/{filename}", f"Pdf Operation/Dustbin/{filename}")
                
        elif input_operation=="3":
            while True:
                try:
                    reader=PdfReader(f"Pdf Operation/Input/{filename}")
                    writer=PdfWriter()
                    if reader.is_encrypted:
                        reader.decrypt(input("\nEnter the existing password to decrypt: "))
                    for page in reader.pages:
                        writer.add_page(page)
                    if file_name.endswith("_encrypted.pdf"):
                        filename=filename.split("_encrypted")[0]
                        writer.write(f"Pdf Operation/Output/{filename}.pdf")
                    else:
                        writer.write(f"Pdf Operation/Output/{filename}")
                    print("Password successfully Removed(location: Pdf Operation/Output)")
                    status="success"
                    break
                except Exception as e:
                    print("Incorrect Password, ",e)
                    status="failed"
            if status=="success":
                # Removing the pdf from the input directory to dustbin folder
                os.makedirs("Pdf Operation/Dustbin", exist_ok=True)
                for filename in filenames_list:
                    os.rename(f"Pdf Operation/Input/{filename}", f"Pdf Operation/Dustbin/{filename}")
                
                
        elif input_operation=="4":
            def watermark(
                content_pdf: Path,
                stamp_pdf: Path,
                pdf_result: Path,
                page_indices: Union[Literal["ALL"], List[int]] = "ALL",
            ):
                    reader = PdfReader(content_pdf)
                    if page_indices == "ALL":
                        page_indices = list(range(0, len(reader.pages)))
                    writer = PdfWriter()
                    for index in page_indices:
                        content_page = reader.pages[index]
                        mediabox = content_page.mediabox

                        # You need to load it again, as the last time it was overwritten
                        reader_stamp = PdfReader(stamp_pdf)
                        image_page = reader_stamp.pages[0]

                        image_page.merge_page(content_page)
                        image_page.mediabox = mediabox
                        writer.add_page(image_page)
                    writer.write(pdf_result)
            stamp_pdf=input("Enter the Watermark pdf file name: ")
            stamp_pdf=f"Pdf Operation/Input/{stamp_pdf}"
            # Removing the pdf from the input directory to dustbin folder
            os.makedirs("Pdf Operation/Dustbin", exist_ok=True)
            for filename in filenames_list:
                os.rename(f"Pdf Operation/Input/{filename}", f"Pdf Operation/Dustbin/{filename}")
                
        elif input_operation=="5":
            pass
        elif input_operation=="6":
            try:
                images=convert_from_path(f"Pdf Operation/Input/{filename}",500,poppler_path=r'C:\Program Files\poppler-23.08.0\Library\bin')
                for i in range(len(images)):
                    images[i].save(f"Pdf Operation/Output/{filename.split('.')[0]}_{i+1}.jpg", 'JPEG')
                print("PDF converted to image successfully (location: Pdf Operation/Output)")
                status="success"
            except:
                print("Image Conversion Failed")
                status="failed"
            if status=="success":
                # Removing the pdf from the input directory to dustbin folder
                os.makedirs("Pdf Operation/Dustbin", exist_ok=True)
                for filename in filenames_list:
                    os.rename(f"Pdf Operation/Input/{filename}", f"Pdf Operation/Dustbin/{filename}")
        elif input_operation=="7":
            try:
                use_lesspdfs=[]
                def convert_to_pdf(filenames_list):
                    for filename in filenames_list:
                        image = Image.open(f"Pdf Operation/Input/{filename}")
                        img = image.convert("RGB")
                        new_pdf = f"{filename.split('.')[0]}.pdf"
                        img.save(f"Pdf Operation/Input/{new_pdf}", "PDF", resolution=100.0)
                        global use_lesspdfs
                        use_lesspdfs.append(new_pdf)
                convert_to_pdf(filenames_list)
                
                # Merging the pdfs
                merger=PyPDF2.PdfWriter()
                for file in use_lesspdfs:
                    merger.append(f"Pdf Operation/Input/{file}")
                new_merged_pdf=input("Enter the output PDF file name (excluding '.pdf'): ")
                merger.write(f"Pdf Operation/Output/{new_merged_pdf}.pdf")
                    
                print(f"Image converted to {new_merged_pdf}.pdf successfully (location: Pdf Operation/Output)")
                status="success"
            except:
                print("PDF Conversion Failed.")
                status="failed"
            if status=="success":
                # Removing the pdf from the input directory to dustbin folder
                os.makedirs("Pdf Operation/Dustbin", exist_ok=True)
                for f in use_lesspdfs:
                    os.remove(f"Pdf Operation/Input/{f}")
                for filename in filenames_list:
                    os.rename(f"Pdf Operation/Input/{filename}", f"Pdf Operation/Dustbin/{filename}")
                
    else:
        print("No valid PDF/image file found in the 'Pdf Operation/Input' Folder for your required operation")
