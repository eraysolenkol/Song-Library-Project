import Song        
import SongLibrary

library = SongLibrary.SongLibrary()
library.connectDatabase()
library.createTable()

while True:
    choice = int(input("""0. Exit
1. Show All Songs
2. Add A Song
3. Delete A Song
4. Show The Total Duration Of Songs
5. Show The Amount of Songs
6. Show The Songs That Starts With Any Letter
7. Show The Longest 5 Song In Descending Order\n"""))

    if choice == 0:
        print("Logged out.")
        break

    elif choice == 1:
        library.showSongs()
    
    elif choice == 2:
        name = input("Name: ")
        albume = input("Albume: ")
        singer = input("Singer: ")
        duration = int(input("Duration (secs): "))

        newSong = Song.Song(name,albume,singer,duration)
        library.addSong(newSong)
    
    elif choice == 3:
        name = input("Which song do you want to delete : ")
        library.deleteSong(name)

    elif choice == 4:
        library.totalDuration()

    elif choice == 5:
        print("There is",len(library),"songs in the library.")

    elif choice == 6:
        letter = input("Enter your letter to find the songs : ")
        library.songStartsWith(letter)

    elif choice == 7:
        library.topFiveSongByDuration()
    
library.cur.close()
library.con.close()