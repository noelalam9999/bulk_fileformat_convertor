from PIL import Image
import os
files = os.listdir('D:\\small projs\\roadtrip\\image_files')
png = ".png"
i = 0
for file in files:
    i+=1
    j=str(i)
    png = "D:\\small projs\\roadtrip\\image_files\\"+j+".png"
    exact_dest = "D:\\small projs\\roadtrip\\image_files\\"+file
    with Image.open(exact_dest,mode='r') as im1:
        im1.save(png)