Input is a video recording recording.

Use VLC "Scene Filter" tool to extract frames in PNG format tips
https://www.reddit.com/r/VLC/comments/f6as7s/how_to_fix_scene_filter_if_it_isnt_working_for_you/

Example Python code using the Pillow library to average multiple PNG images into one PNG image.
https://stackoverflow.com/questions/17291455/how-to-get-an-average-picture-from-100-pictures-using-pil

Nested loop to make sequential average PNG files, based on images 1-6, 2-7, 3-8, etc.

ffmpeg combined the average PNG images into a video, mp4 or gif format
https://unix.stackexchange.com/questions/68770/converting-png-frames-to-video-at-1-fps

ffmpeg -r 4 -i Average%1d.png -pix_fmt yuv420p -r 4 ./output.gif
https://ffmpeg.org/download.html

ffmpeg -r 10 -i Average%05d.png -pix_fmt yuv420p -r 10 ../Shibuya_10.mp4
10 frames per second input, frame filename has zero-padded five-digit sequence

Online converter to resize GIF
https://ezgif.com/resize/ezgif-4-b54e4e68f2fc.gif

