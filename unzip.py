import zipfile  
  
zip = zipfile.ZipFile(r'Python\Python.zip')  
zip.extractall(r'\Python\output') 
