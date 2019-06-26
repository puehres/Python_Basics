import datetime, os, glob

def writer(files):
    now = datetime.datetime.now()
    with open(now.strftime("C:\\Users\\fpuhringer\\github\\Python_Basics\\%Y-%m-%d-%H-%M-%S-%f.txt"),"a") as file:
        for f in files:
            with open(f,"r") as content:
                file.write(content.read())

os.chdir("C:\\Users\\fpuhringer\\github\\Python_Basics\\Merging Text Files")
files = glob.glob("*.txt")

writer(files)
