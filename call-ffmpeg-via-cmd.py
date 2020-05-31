import os
import subprocess

# change the current directory to specified directory which contains ffmpeg.exe
# raw string is used, otherwise need to becareful escape characters '\'
os.chdir(r'C:\Matthew\0-Software\ffmpeg-4.2.1\bin')

# call cmd and to run ffmpeg
subprocess.call(['ffmpeg', '-i', 'input.mp4', 'output.avi'])

# more input parameter for ffmpeg
# download video file
subprocess.call(['ffmpeg', '-i', 'FileLink', '-c', 'copy', '-bsf:a', 'aac_adtstoasc', 'FileName'])


# ------
# loop for a series of files
for each in range(0, 100, 1): # loop from 0 to 99, incremental = 1
    # generate file link and file name for a series of file, prevent new file over write the old one
    tempFileLink = <fileLinkPart1> + str(each) + <fileLinkPart2>
    tempFileName = <fileName> + str(each) + <fileType>

    # print to console for checking
    print('ffmpeg', '-i', tempFileLink, tempFileName)

    # call cmd and to run ffmpeg
    subprocess.call(['ffmpeg', '-i', tempFileLink, tempFileName])
# ------
