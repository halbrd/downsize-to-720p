import os
import subprocess

for file in os.listdir(os.getcwd()):
	if not file.endswith(".py"):
		subprocess.call(["ffmpeg", "-i", file, "-vf", "scale=1280:720", "720-" + file])
