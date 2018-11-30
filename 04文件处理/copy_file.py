file_read = open("C:\\Users\\eryeer\\Desktop\\git\\pythonStudy\\.gitignore")
file_write = open("C:\\Users\\eryeer\\Desktop\\git\\pythonStudy\\README", "w")

# read = file_read.read()
# file_write.write(read)
while True:
    readline = file_read.readline()
    if not readline:
        break
    file_write.write(readline)
file_read.close()
file_write.close()
