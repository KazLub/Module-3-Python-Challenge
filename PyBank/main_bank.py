#import os module
import os
#import csv module
import csv



# path to the file

#filepathcsv=os.path.join('Resources','budget_data.csv')

filepathcsv="C:\\Users\\kazek\\Desktop\\Zadanka domowe\\Module 3 Python\\Module 3 python Challenge\\Instructions\\PyBank\Resources\\budget_data.csv"

 # defining variables
rowcount=0
total=0   
total_months = 0
aged = 0

   
loss_in_profit = []
dates = []


 
with open(filepathcsv) as csvfile:
    csvreader= csv.reader(csvfile,delimiter=',')
    print(csvreader)

    csv_header = next(csvreader)
    print(f"csv header:{csv_header}")


 
    for row in csvreader:
        dates.append(row[0])
        loss_in_profit.append((int(row[1]))- aged)
       
        rowcount+=1
        total+=int(row[1])
        
        total_months = total_months + 1
        
        aged = int(row[1])

    del loss_in_profit[0]

    #finding the average change
    totalprofitloss = sum(loss_in_profit)
    averagechange = round((totalprofitloss / (total_months - 1)), 2)

    #max/min
    maximum_val = max(loss_in_profit)
    minimum_val = min(loss_in_profit)

    maxx = loss_in_profit.index(maximum_val) +1
    minn = loss_in_profit.index(minimum_val) +1

    #dates for max/min
    date_max = dates[maxx]
    date_min = dates[minn]

    #printing
    print("Financial Analysis")
    print("-----------------------")
    print("Total Months:" ,rowcount)
    print("Total: $",total)
    print("Average Change: $",averagechange)
    print("Greatest Increase in Profits:", date_max, "($",maximum_val,")")
    print("Greatest Decrease in Profits:", date_min, "($",minimum_val,")")

    analysis_text_file = os.path.join("C:\\Users\\kazek\\Desktop\\Zadanka domowe\\Module 3 Python\\Module 3 python Challenge\\Instructions\\PyBank\\analisys.txt")
with open(analysis_text_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write("Total Months:"  +str(rowcount))
    outfile.write("\n")
    outfile.write("Total:  $"+str(total))
    outfile.write("\n")
    outfile.write("Average Change:  $"+str(averagechange))
    outfile.write("\n")
    outfile.write("Greatest Increase in Profits:"+ str(date_max)+"( $"+str(maximum_val)+")")
    outfile.write("\n")
    outfile.write("Greatest Decrease in Losses:"+str(date_min)+"( $"+str(minimum_val)+")")