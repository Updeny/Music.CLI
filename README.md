# Music.CLI
This project is to allow people to play their own music from the CLI (Command Line Interface)

##Motivation
Sometimes I just like having a screen full of terminal open, and this project will eventually add 
services that will let you stream music from them (Pandora, Spotify, SoundCloud, etc...).

##Installation
Make sure you have python3 installed, and the python module python-vlc from pip.

##Problems
If you do not use PulseAudio on linux, rename /usr/lib/vlc/plugins/audio_output/libpulse_plugin.so 
to libpulse_plugin.so.bak so vlc doesn't see it, and uses alsa instead
