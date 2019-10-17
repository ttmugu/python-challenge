import os
import csv

total_voters =  0 
resultdic ={}

#funtion that will call below for write result
def write_to_file(text):
    output_file = os.path.join('Election Results.txt')
    with open(output_file, 'a',) as txtfile:
        txtfile.write(text)


csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, newline='') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        total_voters += 1
        if row[2] not in resultdic:
            resultdic[row[2]] = 1
        if row[2] in resultdic:
            resultdic[row[2]] += 1
# print in screen
#print(resultdic)
print("Election Results")
write_to_file("Election Results\n")
print("-------------------------")
write_to_file("-------------------------\n")
print(f"Total Voters: {total_voters}")
write_to_file(f"Total Voters: {total_voters}\n")
print("-------------------------")
write_to_file("-------------------------\n")

for key in resultdic.keys(): 
    value = resultdic[key]
    percent = round(100 * (resultdic[key]/total_voters), 3)
    print (f"{key}: {percent}% ({value})") 
    write_to_file(f"{key}: {percent}% ({value})\n")

print("-------------------------")
write_to_file("-------------------------\n")
key = max(resultdic, key = lambda k: resultdic[k])
print(f"Winner : {key}")
write_to_file(f"Winner : {key}\n")
print("-------------------------")
write_to_file("-------------------------\n")

