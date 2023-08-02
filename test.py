import shutil
import os

for file in os.listdir("2023-05"):
    source = f"2023-05\\{file}"
    file=list(file)
    file.pop(file.index('.',4))
    file[file.index('.')]="#"
    dest = f"2023-05-{''.join(file)}"
    #print(source,dest)
    shutil.copy(source, dest)
#print("File copied successfully.")