import os
path ='C:\\Project\\sampleCode\\solution'
for file in os.listdir(path):
  os.remove(os.path.join(path, file))