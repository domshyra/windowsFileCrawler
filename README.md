# windowsFileCrawler
crawl a list of local files and put them into an collapsible list in html

# generate text file
on windows open cmd. navigate to the root folder you want to make the table of contents for. run `dir /s /b > FilePathTo\FileName.txt`. 
this will generate an output file of all the files and folders. 

Pipe the LS output for unix system. 

# to run
put file with the folder info (`C:\Users\Dominic Schira\FolderName` format) into the folder and then when propmted type full text file name and the extention. 

the folder list will be outputed to `tableOfContents.html` in the same folder.
