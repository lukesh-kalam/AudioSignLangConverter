import os
import shutil

signImagePath = r"C:\\Project\\sampleCode\\hdSigns\\"
newPath = r"C:\\Project\\sampleCode\\solution\\"

data = input("Enter the data :- ")
for i in range(len(data)) :
    
    if data[i]==" " :
        copyPath=signImagePath+'space.jpg'
        copyPath1=newPath+'space.jpg'
        #print(copyPath,copyPath1)
        shutil.copy(copyPath,copyPath1)
    
    else:
        
        # Copying the file from original location to other location
        copyPath = signImagePath+data[i]+'.jpg'
        copyPath1 = newPath+data[i]+'.jpg'
        #print(copyPath,copyPath1)
        shutil.copy(copyPath,copyPath1)
    
    # Renaming the file 
    #print(data[i])
    newName = newPath+'100'+str(i)+'.jpg'
    shutil.move(copyPath1,newName)
    
print("All the required images are moved to required folder and renamed them accordingly")
    
