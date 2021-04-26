# Import libraries
import urllib.request, os, time

# Funtion to access URL and download file
def pullURL():
    # Medical Checkin request URL
    url = 'https://www.example.com'
    # Make request to URL and download file to path and file name specified  
    r = urllib.request.urlretrieve(url, "./DataFiles/export.csv")

# Function to rename .csv file downloaded with timestamp
def fileRename():
    # Use time library to pull timestamp of downloaded file
    timestr = time.strftime("%Y-%m-%d")
    # Rename file to include timestamp in its name
    os.rename('./DataFiles/export.csv','./DataFiles/' + timestr + '.csv')

# Function to log script execution
def Logger():
    # Open changelog.txt and append new row
    f = open("./DataFiles/changelog.txt", "a")
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

# Call all functions
pullURL()
fileRename()
Logger()
