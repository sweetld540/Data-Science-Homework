import os
import csv

budget_data_path = os.path.join("..", "..", "GTATL201811DATA3", "03-Python", "Homework",
    "Instructions", "PyPoll", "Resources", "election_data.csv")

with open(budget_data_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
  

    voterID = []
    counties = []
    candidates = []
    

    for row in csvreader:
        voterID.append(int(row[0]))
        counties.append(row[1])
        candidates.append(row[2])
    

    Khan = 0
    Correy = 0
    Li = 0
    OTooley = 0

    for candidate in candidates:
        if candidate == "Khan":
            Khan = Khan + 1
            
        elif candidate == "Correy":
            Correy = Correy + 1
            
        elif candidate == "Li":
            Li = Li + 1
            
        elif candidate == "O'Tooley":
            OTooley = OTooley + 1
    

possibleWinners = {"Khan": Khan,"Correy": Correy,"Li":Li,"O'Tooley" : OTooley}
totalVotesCast = len(voterID)
khanPercentage = '{0:.0%}'.format(Khan/totalVotesCast)
correyPercentage = '{0:.0%}'.format(Correy/totalVotesCast)
liPercentage = '{0:.0%}'.format(Li/totalVotesCast)
oTooleyPercentage = '{0:.0%}'.format(OTooley/totalVotesCast)

print("Election Results")
print("-----------------------------------")
print(f"Total votes cast: {totalVotesCast}")
print("-----------------------------------")
print(f"Khan: {khanPercentage} {(Khan)}")
print(f"Correy: {correyPercentage} {(Correy)}")
print(f"Li: {liPercentage} {(Li)}")
print(f"O'Tooley: {oTooleyPercentage} {(OTooley)}")
print("-----------------------------------")
print(f"Winner: {(max(possibleWinners.keys(),key=(lambda k: possibleWinners[k])))}")

#save summary to txt
save_file = "election_data_output"
filepath = os.path.join(".", save_file)
with open(filepath,'w') as text:
   
    text.write("Election Results" + "\n")
    text.write("----------------------------------------" + "\n")
    text.write(f"Total votes cast: {totalVotesCast}" + "\n")
    text.write("----------------------------------------" + "\n")
    text.write(f"Khan: {khanPercentage} {(Khan)}" + "\n")
    text.write(f"Correy: {correyPercentage} {(Correy)}" + "\n")
    text.write(f"Li: {liPercentage} {(Li)}" + "\n")
    text.write(f"O'Tooley: {oTooleyPercentage} {(OTooley)}" + "\n")
    text.write("-----------------------------------------"  +  "\n")
    text.write(f"Winner: {(max(possibleWinners.keys(),key=(lambda k: possibleWinners[k])))}" + "\n")