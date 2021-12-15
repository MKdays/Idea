import os

app_path = os.getcwd()
target = "/Idea"

from glob import glob
file_list =  glob(app_path + target + "/**", recursive=True)

for i in file_list:
    if os.path.isfile(i):
        print(i)
    # a = os.path.getmtime(i)
    # print(a)


a = "https://raw.githubusercontent.com/MKdays/Idea/main"
