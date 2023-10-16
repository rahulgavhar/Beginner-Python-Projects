import PyPDF2
from PyPDF2 import PdfReader, PdfWriter
import os
from typing import Union, Literal, List
from pathlib import Path

#finding the pdf file in the directory
directory="Pdf Operation/Input"
filenames=os.listdir(directory)
f_count=0
run="no"
print("PDF files found in the 'Pdf Operation/Input' Folder:\n",filenames,"\n(files except .pdf will be ignored)\n")
print("Enter the operation for image\n1. Merge PDFs\n2. Add Password\n3. Remove Password\n4. Add WaterMark\n5. Reduce Size")
while True:
    try:
        input_operation=input("\nEnter the operation number: ")
        if input_operation=="1" or input_operation=="2" or input_operation=="3" or input_operation=="4" or input_operation=="5":
            pass
        else:
            raise Exception("Invalid Input")
        
        filenames_list=[]
        if len(filenames)>0:
            for file_name in filenames:
                if not file_name.endswith(".pdf"):
                    continue
                if file_name.endswith(".pdf"):
                    filename=file_name
                    filenames_list.append(filename)
                    f_count=len(filenames_list)
            if f_count>1 and input_operation=="1":
                run="yes"
            elif f_count>1 and input_operation!="1":
                raise Exception("More than 1 pdf files are not accepted")
            elif f_count==1 and input_operation=="1":
                raise Exception("1 pdf file is not accepted for Merging PDFs")
            elif f_count==1 and input_operation!="1":
                run="yes"
            break
        else:
            raise Exception("No PDF file found in the 'Pdf Operation/Input' Folder")
                    
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
    
    if input_operation=="1":
        merger=PyPDF2.PdfWriter()
        for filename in filenames_list:
            merger.append(f"Pdf Operation/Input/{filename}")
        output_file_name=input("Enter the output file name(excluding '.pdf'): ")
        merger.write(f"Pdf Operation/Output/{output_file_name}.pdf")
        print("PDFs merged successfully (location: Pdf Operation/Output)")
        confidential=input("Do you want to add a password to the merged File? (yes/no): ")
        if confidential=="yes":
            reader=PdfReader(f"Pdf Operation/Output/{output_file_name}.pdf")
            writer=PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            password=input("Enter the password: ")
            writer.encrypt(password)
            writer.write(f"Pdf Operation/Output/{output_file_name}.pdf")
        # Removing the image from the input directory to dustbin folder
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
        except:
            print("**File is already encrypted**")
        # Removing the image from the input directory to dustbin folder
        os.makedirs("Pdf Operation/Dustbin", exist_ok=True)
        for filename in filenames_list:
            os.rename(f"Pdf Operation/Input/{filename}", f"Pdf Operation/Dustbin/{filename}")
            
    elif input_operation=="3":
        while True:
            try:
                reader=PdfReader(f"Pdf Operation/Input/{filename}")
                writer=PdfWriter()
                if reader.is_encrypted:
                    reader.decrypt(input("\nEnter the password: "))
                for page in reader.pages:
                    writer.add_page(page)
                if file_name.endswith("_encrypted.pdf"):
                    filename=filename.split("_encrypted")[0]
                    writer.write(f"Pdf Operation/Output/{filename}.pdf")
                else:
                    writer.write(f"Pdf Operation/Output/{filename}")
                print("Password successfully Removed(location: Pdf Operation/Output)")
                break
            except Exception as e:
                print("Incorrect Password, ",e)
        # Removing the image from the input directory to dustbin folder
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
        # Removing the image from the input directory to dustbin folder
        os.makedirs("Pdf Operation/Dustbin", exist_ok=True)
        for filename in filenames_list:
            os.rename(f"Pdf Operation/Input/{filename}", f"Pdf Operation/Dustbin/{filename}")
            
    elif input_operation=="5":
        pass
else:
    print("No PDF file found in the 'Pdf Operation/Input' Folder")
