import csv

tleFile = open("tle.txt", "r")
csvFile = open("tle.csv", "w")

fieldnames = ['name', 'norad_id', 'epoch_year', 'epoch_day', 'inclination', 'right_asc',
              'eccentricity', 'arg_perigee', 'mean_anomoly', 'mean_motion']

writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
writer.writeheader()

# Get the first line
line = tleFile.readline()

while line:
        satName = line.strip()

        lineOne = tleFile.readline().strip()
        lineOne = lineOne.split()
        lineTwo = tleFile.readline().strip()
        lineTwo = lineTwo.split()

#        print lineOne
#        print lineTwo
        
        valueDict = {'name': satName,
                     'norad_id': lineTwo[1],
                     'epoch_year': lineOne[3][:2],
                     'epoch_day': lineOne[3][2:],
                     'inclination': lineTwo[2],
                     'right_asc': lineTwo[3],
                     'eccentricity': '0.' + lineTwo[4],
                     'arg_perigee': lineTwo[5],
                     'mean_anomoly': lineTwo[6],
                     'mean_motion': lineTwo[7]}
        
#        print valueDict
        writer.writerow(valueDict)
        

        line = tleFile.readline()
