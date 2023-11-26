import os
import moviepy.editor as mp

files = os.listdir()
current_path = os.getcwd()
new_path =  os.path.join(current_path,'converted_videos')


for file in files:
    try:
        f, extension = file.split('.')
        if extension == 'mp4':           
            clip = mp.VideoFileClip(file)
            clip_resized = clip.resize(height=480) # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
            clip_resized.write_videofile("converted_videos/{0}".format(file))
    except Exception as e:
        pass

print('TODOS LOS VIDEOS HAN SIDO CONVERTIDOS CON ÉXITO!')