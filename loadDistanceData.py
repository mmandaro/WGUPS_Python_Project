import csv  # allow us to use the csv reader to read in the distance csv file

# define function that will open the csv file, make it a list and return the variable containing this list
# note the csv file has been edited to contain only the numeric data, with the address info being put in a separate file

def loaddistancedata():
    with open("WGUPS_Distance_File.csv", 'r') as distancedata_file:
        distancedata_csv = csv.reader(distancedata_file)
        distancedata = list(distancedata_csv)  # makes the distance data into a list
        distancedata[0][0] = '0'  # replaces /ueff0 with just 0, as intended

        return distancedata

