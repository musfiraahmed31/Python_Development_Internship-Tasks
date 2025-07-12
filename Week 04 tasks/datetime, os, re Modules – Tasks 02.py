import os
import re

FolderPath = input("Enter folder path: ")

if os.path.isdir(FolderPath):
    print("\nMatching .txt files that start with 'report':")

    for FileName in os.listdir(FolderPath):
        if FileName.endswith(".txt"):

            if re.match(r'^report.*\.txt$', FileName):
                print(FileName)
else:
    
    print("Folder not found. Please check the path.")
