from collections import deque

class Song:

    def __init__(self):
        self.title = ""
        self.artist = ""

    def prompt(self):
        self.title = input("Enter the title: ")
        self.artist = input("Enter the artist: ")
        
    def display(self):
        print("{} by {}".format(self.title, self.artist))
    
def main():
    playlist = deque()
    song = Song()
    sel_user = 0

    while sel_user != 4:
        print()
        print("Options:")
        print("1. Add a new song to the end of the playlist")
        print("2. Add a new song to the beginning of the playlist")
        print("3. Play the next song")
        print("4. Quit")
        print()
        sel_user = int(input("Enter selection: "))

        if sel_user == 1:
            song.prompt()
            playlist.append(song)

        elif sel_user == 2:
            song.prompt()
            playlist.appendleft(song)

        elif sel_user == 4:
            print("Good bye")

        else:
            if len(playlist) == 0:
                print("The playlist is currently empty.")
            elif len(playlist) > 1:
                song = playlist.popleft()
                print()
                print("Playing song:")
                song.display()

if __name__ == "__main__":
   main()
