import sqlite3
import datetime

class SongLibrary():
    
    def __init__(self):
        pass

    def __len__(self):
        self.cur.execute("SELECT * FROM SongLibrary")
        allSongs = self.cur.fetchall()
        return len(allSongs)
        

    def connectDatabase(self):
        self.con = sqlite3.connect("database.db")
        self.cur = self.con.cursor()

    def createTable(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS SongLibrary(Name TEXT,Albume TEXT,Singer TEXT,Duration INT)")
        self.con.commit()

    def showSongs(self):
        self.cur.execute("SELECT * FROM SongLibrary")
        allSongs = self.cur.fetchall()
        for song in allSongs:
            print("*****************************")
            print("Name: {}\nAlbume: {}\nSinger: {}\nDuration: {}secs".format(song[0],song[1],song[2],song[3]))
            print("*****************************\n")

    def addSong(self,song):
        self.cur.execute("INSERT INTO SongLibrary VALUES(?,?,?,?)",(song.name,song.albume,song.singer,song.duration))
        self.con.commit()
        print(f"{song.name} is sucessfully added to the library.")

    def deleteSong(self,name):
        choice = input("Are You Sure? (y/n)")
        while True:
            if choice.lower() == "y":
                self.cur.execute("DELETE FROM SongLibrary WHERE Name = ?",(name,))
                print(f"{name} deleted.")
                self.con.commit()
                break
            elif choice.lower() == "n":
                print("Cancelled.")
                break
            else:
                print("Please enter y or n.")
    
    def totalDuration(self):
        self.cur.execute("SELECT Duration FROM SongLibrary")
        durations = self.cur.fetchall()
        total = sum([i[0] for i in durations])
        total_all = datetime.timedelta(seconds=total)
        print(f"Total duration is {total} seconds.({total_all})")

    def songStartsWith(self,letter : str):
        letter = letter.upper()
        self.cur.execute(f"SELECT * FROM SongLibrary WHERE Name LIKE '{letter}%'")
        songs = self.cur.fetchall()
        print(f"SONGS THAT STARTS WITH {letter}")
        if len(songs) == 0:
            print(f"No song found starts with letter {letter}")
        else:
            for song in songs:
                print("*****************************")
                print("Name: {}\nAlbume: {}\nSinger: {}\nDuration: {}secs".format(song[0],song[1],song[2],song[3]))
                print("*****************************\n")

    def topFiveSongByDuration(self):
        self.cur.execute("SELECT * FROM SongLibrary ORDER BY Duration DESC LIMIT 5")
        songs = self.cur.fetchall()
        for song in songs:
            print("*****************************")
            print("Name: {}\nAlbume: {}\nSinger: {}\nDuration: {}secs".format(song[0],song[1],song[2],song[3]))
            print("*****************************\n")