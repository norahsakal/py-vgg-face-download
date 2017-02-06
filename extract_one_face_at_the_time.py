import os
import urllib
import csv 
import sys

# The custom delimiter is whitespace 
with open("files/Surnamne_Lastname.txt", "rb") as f:
	reader = csv.reader(f, delimiter=' ')

	# Enumerate to give unique image name and urlretrieve images from the file
	for i, row in enumerate(reader):
		print row[1]

		# Try/except to avoid interruption during looping
		try:
			urllib.urlretrieve(row[1], "images/" + str(i) + ".jpg")
		except Exception as e:
			print e



 








