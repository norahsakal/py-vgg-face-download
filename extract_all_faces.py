import os
import urllib
import csv 
import sys

# Loop through each file in folder to read all the text files
for file in os.listdir("files"):
	if file.endswith(".txt"):
		print(file)

	# The custom delimiter is whitespace 
	with open(file, "rb") as f:
		reader = csv.reader(f, delimiter=' ')

		# Enumerate to give unique image name and urlretrieve images from the file
		for i, row in enumerate(reader):
			print row[1]

			# Try/except to avoid interruption during looping
			try:
				urllib.urlretrieve(row[1], "images/" + str(i) + ".jpg")
			except Exception as e:
				print e


 








