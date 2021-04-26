# Import libraries
import urllib.request, os, time

# Globals
# Use time library to pull timestamp of downloaded file
timestr = time.strftime("%Y-%m-%d")

# Funtion to access URL and download file
def pullURL():
    # Medical Checkin request URL
    url = 'https://www.cmgcheckin.com/login/exportall.php'
    # Make request to URL and download file to path and file name specified  
    r = urllib.request.urlretrieve(url, './MDC/DataFiles/' + timestr + '.csv')

# Function to rename .csv file downloaded with timestamp
# def fileRename():
#     # Rename file to include timestamp in its name
#     os.rename('./MDC/DataFiles/export.csv','./MDC/DataFiles/' + timestr + '.csv')

# Function to log script execution
def Logger():
    # Open changelog.txt and append new row
    f = open('./MDC/changelog.txt', 'a')
    # Assign temp variable to timezone portion of timestamp
    temp = time.strftime("%Z")
    # Log temp value
    # print(temp)
    # Assign variable to empty string to be updated later
    timezone = ''
    # Conditional to set timezone string to 'EDT'
    if temp == 'Eastern Daylight Time':
        timezone = 'EDT'
    # Conditional to set timezone string to 'EST'
    elif temp == 'Eastern Standard Time':
        timezone = 'EST'
    else:
        timezone
    # Write script execution confirmation to changelog file with timestamp
    f.write("Downloaded on: " + time.strftime("%Y-%m-%d %H:%M:%S " + timezone + "\n"))
    # Close file when completed
    f.close()

# Function to append data to master file
def appendToMaster():
    # Open daily file in read-mode
    file = open('./MDC/DataFiles/' + timestr + '.csv', 'r')
    # Open master file in append-mode
    master = open('./MDC/master.csv', 'a+')
    
    with file as f:
        next(f)
        for line in f:
            # Append to master starting with second data row (excluding headers)
            master.write(file.read())
    # Return cursor to top line
    master.seek(0)
    # Close both files
    file.close()
    master.close()

# Call all functions
pullURL()
# fileRename() -- Unused function
Logger()
appendToMaster()
