import os
import csv

budget_data_path = os.path.join("..", "..", "GTATL201811DATA3", "03-Python", "Homework",
    "Instructions", "PyBank", "Resources", "budget_data.csv")

with open(budget_data_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
 

#Variables For First Loop
    #list of total months data was recorded
    listOfMonths = []
    #list containing all of the monthly  P & L statements
    monthlyPAL = []
#Variable For Second Loop
    #change month over month for increase or decrease in revenue
    palChange = []
      

    for row in csvreader:
        
        listOfMonths.append(row[0])
        monthlyPAL.append(int(row[1]))
        
    for x in range(1,len(monthlyPAL)):

        palChange.append(int(monthlyPAL[x] - monthlyPAL[x-1]))
            
#find the max value of monthly changes
largestIncreaseRevenue = max(palChange)
#find the min value in monthly changes
largestDecreaseRevenue = min(palChange) 
#find the max increase month
LargestMonthIndex = palChange.index(largestIncreaseRevenue)
largestIncreaseMonth = listOfMonths[LargestMonthIndex+1]
#find the min increase month
WorstMonthIndex = palChange.index(largestDecreaseRevenue)
largestDecreaseMonth = listOfMonths[WorstMonthIndex+1]
#average change Month over month
averagePAL = round((sum(palChange))/(len(listOfMonths)-1),2)
#total sum of all P & L Statements
monthlyPALSum = sum(monthlyPAL)
#total amount of months data was collected
listOfMonthsSum = len(listOfMonths)

print("Financial Analysis")
print("------------------")
print(f"Total Months: {listOfMonthsSum}")
print(f"Total ${monthlyPALSum}")
print(f"Average change: {averagePAL}")
print(f"Greatest increase in profits: {largestIncreaseMonth} (${largestIncreaseRevenue})")
print(f"Greatest decrease in profits: {largestDecreaseMonth} (${largestDecreaseRevenue})")


# save summary to txt
save_file = "budget_data_output"
filepath = os.path.join(".", save_file)
with open(filepath,'w') as text:
   

    text.write("Financial Analysis" + "\n")
    text.write("----------------------------------------" + "\n")
    text.write(f"Total Months: {listOfMonthsSum}" + "\n")
    text.write(f"Total Revenue: ${monthlyPALSum}" + "\n")
    text.write(f"Average Revenue Change: ${averagePAL}" + "\n")
    text.write(f"Greatest Increase in Revenue: {largestIncreaseMonth} (${largestIncreaseRevenue})" + "\n")
    text.write(f"Greatest Decrease in Revenue: {largestDecreaseMonth} (${largestDecreaseRevenue})" + "\n")

    