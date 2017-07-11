# TO RUN: python3 Script_3_data_integration.py referenceFileName seedFileName > output.csv

import sys

# Lists to contain data from each respective input file
referenceFileList = []
seedFileList = []

# Lists to contain gene IDs
referenceGeneList = []
seedGeneList = []

# Result List
grownSeedFileList = []

# Processing reference file
with open(sys.argv[1], "r") as referenceFile:
	for line in referenceFile:
		referenceFileList.append(line.split(","))


# Processing seed file
with open(sys.argv[2], "r") as seedFile:
	for line in seedFile:
		seedFileList.append(line.split(","))

# Making refernce list of gene IDs
for line in referenceFileList:
	referenceGeneList.append(line[5])

# Making a seed list of gene IDs
for line in seedFileList:
	seedGeneList.append(line[0])

# Finding the indices of reference gene IDs in seed gene IDs
for gene in referenceGeneList:
	try:
		grownSeedFileList.append(seedFileList[seedGeneList.index(gene)])
	except ValueError:
		pass

for i in grownSeedFileList:
	for j  in i:
		print(j.strip("\n"), ",", end="")
	print("\n")




