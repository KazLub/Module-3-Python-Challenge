#import modules
from ast import For
import os
import csv
import pandas as pd

# path to the file



filepathcsv="C:\\Users\\kazek\\Desktop\\Zadanka domowe\\Module 3 Python\\Module 3 python Challenge\\Instructions\\PyPoll\Resources\\election_data.csv"


rowcount=0
candidate1 = 0
candidate2 = 0
candidate3 = 0  
candidate = set()
uniquelist=[]
winner = 0 

with open(filepathcsv) as csvfile:
    csvreader= csv.reader(csvfile,delimiter=',')
    #print(csvreader)
    
    csv_header = next(csvreader)
    #print(f"csv header:{csv_header}")

#total votes
    for row in csvreader:
        rowcount+=1
#unique candidates        
        if row[2] not in uniquelist:
           uniquelist.append(row[2])
            
#total votes per canddidate            
with open(filepathcsv) as csvfile:
    csvreader= csv.reader(csvfile,delimiter=',')
    #print(csvreader)
    
    csv_header = next(csvreader)         
    for row in csvreader:
        candidate.add(row[2])
        if (row[2] == uniquelist[0]):
            candidate1 += 1
        elif (row[2] == uniquelist[1]):
            candidate2 += 1
        else:
            candidate3 += 1
            
#The winner of the election 
    vote_total = [ candidate1, candidate2, candidate3]
    winner_counts = max(vote_total)
    winner_name = ""
    
    if winner_counts == candidate1 :
        winner_name = uniquelist[0]

    elif winner_counts == candidate2 :
        winner_name = uniquelist[1]   

    elif winner_counts == candidate3 :
        winner_name = uniquelist[2]


    
            
#percentage        
    cand1_percent=candidate1/rowcount        
    cand2_percent=candidate2/rowcount
    cand3_percent=candidate3/rowcount

    
    print("Total Votes: ",rowcount)
    print("-----------------------")
    print(uniquelist[0]," ","{:.3%}".format(cand1_percent)," (",candidate1,")")
    print(uniquelist[1]," ","{:.3%}".format(cand2_percent)," (",candidate2,")")
    print(uniquelist[2]," ","{:.3%}".format(cand3_percent)," (",candidate3,")")
    print("Winner: " +  winner_name)

    output_path = os.path.join("C:\\Users\\kazek\\Desktop\\Zadanka domowe\\Module 3 Python\\Module 3 python Challenge\\Instructions\\PyPoll\\Results.txt")

with open(output_path, 'w') as file:

    file.write("Election Results")
    file.write("\n")
    file.write("---------------------")
    file.write("\n")
    
    file.write("Total Votes: "+str(rowcount))
    file.write("\n")
    
    file.write("---------------------")
    file.write("\n")
    file.write(str(uniquelist[0])+" "+"{:.3%}".format(cand1_percent)+" ("+str(candidate1)+")")
    file.write("\n")
    file.write(str(uniquelist[1])+" "+"{:.3%}".format(cand2_percent)+" ("+str(candidate2)+")")
    file.write("\n")
    file.write(str(uniquelist[2])+" "+"{:.3%}".format(cand3_percent)+" ("+str(candidate3)+")")
    file.write("\n")
    file.write("---------------------")
    file.write("\n")
    file.write("Winner: " +  str(winner_name))
    file.write("\n")
    file.write("---------------------")