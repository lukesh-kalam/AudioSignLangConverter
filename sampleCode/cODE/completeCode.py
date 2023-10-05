# Importing Required Modules
import os
import shutil
from os.path import isfile, join 
import cv2
import speech_recognition as sr


class SpechToSignVideo():
    def speechReg(self):
        r = sr.Recognizer()
        print("Please say something")
        with sr.Microphone() as source :
            audio_data = r.record(source,duration=5)
            print("Recognizing")
            text=r.recognize_google(audio_data)
            print(text)
            obj.imageMove(text)
            
    def imageMove(self,text):
        self.text = text
        signImagePath = r"C:\\Project\\sampleCode\\hdSigns\\"
        newPath = r"C:\\Project\\sampleCode\\solution\\"
        # data = input("Enter the data :- ")
        data = text
        for i in range(len(data)) :
            if data[i]==" " :
                copyPath=signImagePath+'space.jpg'
                copyPath1=newPath+'space.jpg'
                shutil.copy(copyPath,copyPath1)
            else:
                # Copying the file from original location to other location
                copyPath = signImagePath+data[i]+'.jpg'
                copyPath1 = newPath+data[i]+'.jpg'
                shutil.copy(copyPath,copyPath1)
            newName = newPath+'100'+str(i)+'.jpg'
            shutil.move(copyPath1,newName)
        print("All the required images are moved to required folder and renamed them accordingly")
        
        directory= 'C:\Project\sampleCode\solution'
        pathIn=directory+'/'
        pathOut=pathIn+'video_EX9.avi'
        fps=1
        time=1 # the duration of each picture in the video
        obj.convert_pictures_to_video(pathIn, pathOut, fps, time)
        
    def convert_pictures_to_video(self,pathIn, pathOut, fps, time):
        self.pathIn = pathIn
        self.pathOut = pathOut
        self.fps = fps
        self.time = time
        ''' this function converts images to video'''
        frame_array=[]
        files=[f for f in os.listdir(pathIn) if isfile(join(pathIn,f))]
        for i in range (len(files)):
            filename=pathIn+files[i]
            '''reading images'''
            img=cv2.imread(filename)
            # img=cv2.resize(img,(1400,1000))
            height, width, layers = img.shape
            size=(width,height)
            for k in range (time):
                frame_array.append(img)
        out=cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps,size)
        for i in range(len(frame_array)):
            out.write(frame_array[i])
        out.release()

    def cleanPath(self):
        print("Cleaning the path for exectuiton")
        path ='C:\\Project\\sampleCode\\solution'
        for file in os.listdir(path):
            os.remove(os.path.join(path, file))

obj = SpechToSignVideo()
obj.cleanPath()
obj.speechReg()
