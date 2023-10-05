import speech_recognition as sr
import os, shutil

class DeafAudio :
    def speechReg(self) :
        r = sr.Recognizer()
        print("Please say something")
        with sr.Microphone() as source :
            audio_data = r.record(source,duration=5)
            print("Recognizing")
            text=r.recognize_google(audio_data)
            text = text.upper()
            print(text)
            obj.imageMovement(text)

    def imageMovement(self,data):
        self.datadata = data
        signImagePath = r"C:\\Project\\sampleCode\\SignImages\\"
        newPath = r"C:\\Project\\sampleCode\\solution\\"
        
        for i in range(len(data)) :
        
            if data[i]==" " :
                copyPath=signImagePath+'space.png'
                copyPath1=newPath+'space.png'
                #print(copyPath,copyPath1)
                shutil.copy(copyPath,copyPath1)
            
            else:
                # Copying the file from original location to other location
                copyPath = signImagePath+data[i]+'.png'
                copyPath1 = newPath+data[i]+'.png'
                #print(copyPath,copyPath1)
                shutil.copy(copyPath,copyPath1)
        
            # Renaming the file 
            #print(data[i])
            newName = newPath+'100'+str(i)+'.png'
            shutil.move(copyPath1,newName)
        
        #print("All the required images are moved to required folder and renamed them accordingly")

    
obj = DeafAudio()
obj.speechReg()