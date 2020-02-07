import os
import sys
from collections import OrderedDict 

filename = input("type file input file name: ")

#read text file
with open(filename) as readFile:
    lines = [line.rstrip() for line in readFile]

outputLines = []
filesDictionary = OrderedDict() 
currentDepth = 0

#region <head>
#start head and scripts
outputLines.append("<head>")
#js
outputLines.append('<script type="text/javascript" async="" src="tree.js"></script>')
#css
outputLines.append('<link type="text/css" rel="stylesheet" href="tree.css">')
outputLines.append('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">')
outputLines.append('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.12.1/css/all.min.css">')
#close
outputLines.append("</head>")

#endregion

#start ul
outputLines.append("<body> \n <div class='col-12'> \n <ul id='my-dir'\n")

#remove the drive letter
startPath = lines[0][3:]
startPathArray = startPath.split('\\')
rootLocation = len(startPathArray) - 1
startPathName = startPathArray[rootLocation]
root = startPath[:-len(startPathName):]

#Build dictionary of the file structure
for line in lines:
    #remove which drive it is
    path = line[3:]
    pathArray = path.split('\\')
    fileLocation = len(pathArray) - 1
    file = pathArray[fileLocation]
    pathWithoutFile = path[:-len(file):]

    #add to dictionary
    if pathWithoutFile in filesDictionary:
        filesDictionary[pathWithoutFile].append(file)
    else:
        filesDictionary[pathWithoutFile] = [file]


def addFilesToOutput(key, folderArray):
    global filesDictionary
    pathArray = key.split('\\')
    fileLocation = len(pathArray) - 2
    folder = pathArray[fileLocation]
    outputLines.append('<li><span class="caret text-primary font-weight-bold"><i class="far fa-folder-open"></i> ' + folder  + '</span>\n <ul class="nested active">\n')
    for folderName in folderArray:
        path = key  + folderName + '\\'
        if path in filesDictionary:
            addFilesToOutput(path, filesDictionary[path])
        else:
            outputLines.append("<li>" + folderName + '</li>\n')
    outputLines.append("</ul>\n")
    outputLines.append("</li>\n")

#recursivly output the file structure
addFilesToOutput(root, filesDictionary[root])

#close UL
outputLines.append("</ul> \n </div> \n </body>")

#write new lines to tree.txt file
with open('tableOfContents.html', 'w') as writeFile:
    writeFile.writelines(outputLines)

#close 
readFile.close()
writeFile.close()
