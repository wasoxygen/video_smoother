import os, numpy, PIL, time
from PIL import Image

#11:56 AM 9/12/2020

t1 = time.perf_counter()

#scene00001.png to scene01616.png
frames_in_dir = r"C:\Users\Steve\Videos\smooth\Shibuya_LlSPOnQw86A\frames_in" 
frames_out_dir = r"C:\Users\Steve\Videos\smooth\Shibuya_LlSPOnQw86A\frames_out"

#how many frames will be averaged into a new smoothed frame
rangelength = 24

# Access all PNG files in directory
allfiles=os.listdir(frames_in_dir)
imlist=[filename for filename in allfiles if  filename[-4:] in [".png",".PNG"]]
imlist.sort()

# Assuming all images are the same size, get dimensions of first image
w,h=Image.open(frames_in_dir + "\\" + imlist[0]).size
N=len(imlist)

print ("found " + str(len(imlist)) + " frames in " + frames_in_dir)

#there are 1616 source png images
#version one: combine in groups of 6, i.e. 1-6, 2-7, 3-8, ... 17-22
#             dumb way, repeat averaging for each set


# 1-10, 2-11, 3-12, 4-13 ...

for outerloop in range(0, len(imlist) - rangelength - 1):
#for outerloop in range(0, 4):

  # Create a numpy array of floats to store the average (assume RGB images)
  arr=numpy.zeros((h,w,3),numpy.float)

  #for innerloop in range(outerloop, outerloop + rangelength):  
  for innerloop in range(0, rangelength):  
    # Build up average pixel intensities, casting each image as an array of floats

    im = imlist[outerloop + innerloop]

    filename = frames_in_dir + "\\" + im
    print ("processing " + filename + " for out frame " + str(outerloop) + "|" + str(innerloop) + " " + "{:.2%}".format(outerloop / (len(imlist)-rangelength))) + " " + (time.perf_counter() - t1).round() + " sec"

    imarr=numpy.array(Image.open(frames_in_dir + "\\" + im),dtype=numpy.float)
    arr=arr+imarr/rangelength
  
    # Round values in array and cast as 8-bit integer
    arr=numpy.array(numpy.round(arr),dtype=numpy.uint8)
  
  # Generate, save and preview final image
  out=Image.fromarray(arr,mode="RGB")
  out.save(frames_out_dir + "\\Average" + str(outerloop).zfill(5) + ".png")

#out.show()
