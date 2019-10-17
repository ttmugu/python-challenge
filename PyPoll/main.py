import os
import csv

resultdic ={
    "Total_Voters": 0 
}


csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for row in csvreader:
        resultdic["Total_Voters"] += 1
        if row[2] not in resultdic:
            resultdic[row[2]] = 1
        if row[2] in resultdic:
            resultdic[row[2]] += 1

print(resultdic)
print("Election Results")
print("-------------------------")
#print(f"{resultdec.keys().index(0)} : {resultdec.keys().index(0)[0]}")
# need to print result correct format 
for key, value in resultdic.items(): 
    print (key, value) 

print("-------------------------")
# need to print winner here
print("-------------------------")