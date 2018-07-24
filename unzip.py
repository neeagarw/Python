import zipfile  
  
zip = zipfile.ZipFile(r'https://github.com/neeagarw/Python.git')  
zip.extractall(r'https://github.com/neeagarw/Python.git') 
