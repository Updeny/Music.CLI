import os
import time
import vlc

def main():	

	library = input("Please give me the full path to your libary")
	
	#Move to the library we were just given
	os.chdir(library)

	#Now we load all of the song files and list them to play
	for root, dirs, files in os.walk(library):
		print(files)
	
	song = input("Please give me the song file name you want to play")

	current_song = vlc.MediaPlayer(os.path.join(library, song))

        #We need to time.sleep because is_playing() is not updated fast enough, and will be considered false when we get to the while loop
	current_song.play()
	time.sleep(.1)
	print("song is " + str(current_song.is_playing()))

	#infinite loop
	while(current_song.is_playing()):
            pass

if(__name__ == "__main__"):
	main()
