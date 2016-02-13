combined = open("combined2015.csv","a")

# first file with header
for line in open("201501-citibike-tripdata.csv"):
    combined.write(line)

# rest of the file ignore header
for i in range(2,13):
    f = open("2015"  + str("%02d" %(i)) + "-citibike-tripdata.csv")
    f.next()
    for line in f:
        combined.write(line)
    f.close()
combined.close()

