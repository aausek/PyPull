# PyPull

Developed by: **@aausek**

## Product Description

This simple script downloads a file via a specific URL then proceeds to timestamp it to reflect download date and log the script execution to *changelog.txt*. Daily file contents are then appended to master file.

## Completed Features

- File download & renaming
- Execution logging
- Appending contents to master

## Libraries used

-  urllib.request
-  os
-  time

## Running the script

On *Windows Powershell*, ensure you have the latest Python version installed then navigate to file directory and run the command: 

`
PS C:\Users\Folder> [~python.exe] .\pypull.py
`

On *Mac Terminal*, ensure you have the latest Python version installed then navigate to file directory and run the command:

`
$ python3 pypull.py
`
