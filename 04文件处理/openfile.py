file = open("C:\\Users\\eryeer\\Desktop\\git\\pythonStudy\\.gitignore", "r")
while True:
    readline = file.readline()
    if not readline:
        break
    print(readline)
file.close()
