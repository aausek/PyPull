# DEVELOPED BY ANA AUSEK - 2021-04-26

# Import libraries
import urllib.request, os, time

# Globals
# Use time library to pull timestamp of downloaded file
timestr = time.strftime("%Y-%m-%d")

path = './DataFiles/'

fileExtension = '.csv'

# Funtion to access URL and download file
def pullurl():
    # Medical Checkin request URL
    url = 'https://www.example.com'
    # Make request to URL and download file to path and file name specified
    r = urllib.request.urlretrieve(url, path + timestr + fileExtension)
    # Assign variable to newly generated file name
    filename = path + timestr + fileExtension
    # Call appendtomaster() 
    appendtomaster(filename)

# Function to rename .csv file downloaded with timestamp
# def fileRename():
#     # Rename file to include timestamp in its name
#     os.rename('./MDC/DataFiles/export.csv','./MDC/DataFiles/' + timestr + '.csv')

# Function to log script execution
def logger():
    # Open changelog.txt and append new row
    f = open('changelog.txt', 'a')
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
def appendtomaster(filename):
    # Open daily file in read-mode
    file = open(filename, 'r')
    # Open master file in append-mode
    master = open('master.csv', 'a+')

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

# Main function
def main():
    pullurl()
    logger()

# Call main()
main()
