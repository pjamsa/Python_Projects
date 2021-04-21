import sqlite3 

conn = sqlite3.connect('assignment.db') #creates my database in Sqlite3

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS TextFiles( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        FileName TEXT)")
    conn.commit() #commits changes made to DB 
conn.close()

conn = sqlite3.connect('assignment.db')

fileList = ('information,docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt','data.pdf', 'myPhoto.jpg') #All of my files
for files in fileList:
    if files.endswith(".txt"):
        print(files) # prints all files ending in .txt
        
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO TextFiles(FileName) VALUES(?)",(files,)) # brings all files ending with .txt into DB
        conn.commit()
conn.close()
                
    
