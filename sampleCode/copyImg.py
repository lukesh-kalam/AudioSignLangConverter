import os
import shutil

signImagePath = r"C:\\Project\\sampleCode\\SignImages\\"
newPath = r"C:\\Project\\sampleCode\\solution\\"

data = input("Enter the data :- ")
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
    
print("All the required images are moved to required folder and renamed them accordingly")
    
