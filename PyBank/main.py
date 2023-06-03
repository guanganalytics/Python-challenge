
import os
import csv

print("Fianancial analysis")
print("")
print("--------------------------------------------")

csvpath=r"C:\Users\henry\Desktop\Python-challenge\PyBank\Resources\budget_data.csv"
# The total number of months included in the dataset
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header=next(csvreader)
    firstrow=next(csvreader)
    number_of_months=1
    total_amount=int(firstrow[1])
    changelist=[]
    previousvalue=int(firstrow[1])
    maxnumber=firstrow[1]
    minnumber=firstrow[1]
    greatestincrease=0
    greatestdecrease=0
    maxdate=""
    mindate=""

    for row in csvreader:
#The total number of months included in the dataset
        number_of_months=number_of_months+1
# The net total amount of "Profit/Losses" over the entire period
        total_amount=total_amount+int(row[1])
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
        change=int(row[1])-previousvalue
        previousvalue=int(row[1])
        changelist.append(change)
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period   
        if int(change)>greatestincrease:
            greatestincrease=int(change)
            maxdate=row[0]
        if int(change)<greatestdecrease:
            greatestdecrease=int(change)
            mindate=row[0] 
    
# Formatting for averge change
    average=sum(changelist)/(number_of_months-1)
#Output all results run from the loop with skipping lines in between
    print("")
    print("Total Months: "+str(number_of_months))
    print("")
    print("Total: "+"$"+str(total_amount))
    print("")
    print("Average Change: "+"$"+(str(round(average,2))))
    print("")     
    print("Greatest Increase in Profits: "+ str(maxdate)+" "+"($"+str(greatestincrease)+")")
    print("")
    print("Greatest Decrease in Profits: "+str(mindate)+" "+"($"+str(greatestdecrease)+")")

rounded_average=str(round(average,2))
my_string=f"""Fianancial analysis

--------------------------------------------

Total Months: {number_of_months}
  
Total: ${total_amount}
   
Average Change: ${rounded_average}
 
Greatest Increase in Profits: {maxdate} {greatestincrease}
   
Greatest Decrease in Profits: {mindate} {greatestdecrease}"""

with open("PyBank.txt","w") as f:
    f.write(my_string)




