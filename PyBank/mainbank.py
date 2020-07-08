#import dependencies
import os
import csv

dates =[]
values = []
profit_lose = 0
average_delta= []
delta = 0



file_path = '../Resources/Budget_Data.csv'
#specifiy the file to write to
#Read the csv file budget_data.csv
Budget = os.path.join('Resources','Budget_Data.csv')
#append date and PL to the index
with open(Budget) as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')
	next(csvreader, None)
	for row in csvreader:
	#assign indexes for computation	
		date=row[0]
		value=int(row[1])
		dates.append(row[0])
		values.append(int(row[1]))
		datalength = len(values)
		sum = 0

	# calculate total PL as profit_lose with sum funtion.
	#max_profit using the max function and min_profit using min func.
	# For i statement to interate down data set
	for i in range(0, datalength):	

		profit_lose= profit_lose + int(values[i])
		max_profit=max(values)
		min_profit=min(values)
		months=len(values)
		#iterate through data
		sum = sum + (values[i + 1] - values[i]) 
		if i == datalength - 2:
			break
	#calculate the average of averages in value row
	average_change = (sum)/(months)




	#print statements, formatted for currency, adding dates to min and max
	print("Financial Analysis")
	print("~"*30)
	print("Total Months:", (months))
	print("Total Profit/Lose:", '${:,.2f}'.format(profit_lose))
	print("Average Change:",'${:,.2f}'.format(round(average_change,2)))
	print("Greatest Increase:",(dates[values.index(max_profit)]),"~~",'${:,.2f}'.format(max_profit))
	print("Greatest Decrease:",(dates[values.index(min_profit)]),"~~",'${:,.2f}'.format(min_profit))
	

	#write text file to Analysis folder
	# set location
	outputplace = os.path.join('Analysis','Financial_Results.txt')

	#open file with write
	with open(outputplace, 'w', newline='') as datafile:
		txtwriter = csv.writer(datafile, delimiter=' ')

		txtwriter.writerow(["Financial Analysis"])
		txtwriter.writerow(["~"*30])
		txtwriter.writerow(["Total Months:", (months)])
		txtwriter.writerow(["Total Profit/Lose:", '${:,.2f}'.format(profit_lose)])
		txtwriter.writerow(["Average Change:",'${:,.2f}'.format(round(average_change,2))])
		txtwriter.writerow(["Greatest Increase:",(dates[values.index(max_profit)]),"~~",'${:,.2f}'.format(max_profit)])
		txtwriter.writerow(["Greatest Decrease:",(dates[values.index(min_profit)]),"~~",'${:,.2f}'.format(min_profit)])














