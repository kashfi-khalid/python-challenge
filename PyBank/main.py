import csv
import os


file_path = os.path.join(os.getcwd(), 'Resources', 'budget_data.csv')


with open(file_path, 'r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')

	csv_header = next(csv_reader)

	# print('HEADERS ARE', csv_header)

	month_list = []
	value_list = []


	for row in csv_reader:

		month_list.append(row[0])
		value_list.append(int(row[1]))



	change_in_revenue = list()

	# print('VALUE LIST', value_list)
	for i in range(1, len(value_list)):

		change_in_revenue.append(value_list[i] - value_list[i-1])


	# print('MONTH_LIST',month_list)
	
	print('Financial Analysis')
	print('----------------------------')
	print(f'Total Months: {len(month_list)}')

	print(f'Total: ${sum(value_list)}')
	print(f'Average Change: ${round(sum(change_in_revenue)/len(change_in_revenue),2)}')


	# print(change_in_revenue)

	maximum_change = max(change_in_revenue)
	minimum_change = min(change_in_revenue)

	index_of_maximum = change_in_revenue.index(maximum_change) + 1
	index_of_minimum = change_in_revenue.index(minimum_change) + 1

	max_month = month_list[index_of_maximum]
	min_month = month_list[index_of_minimum]

	print(f'Greatest Increase in Profits: {max_month} (${maximum_change})')
	print(f'Greatest Decrease in Profits: {min_month} (${minimum_change})')



analysis_file_path = os.path.join(os.getcwd(), 'analysis', 'output.txt')

with open(analysis_file_path, 'w') as file_write:
	file_write.write('Financial Analysis\n')
	file_write.write('----------------------------\n')
	file_write.write(f'Total Months: {len(month_list)}\n')
	file_write.write(f'Total: ${sum(value_list)}\n')
	file_write.write(f'Average Change: ${round(sum(change_in_revenue)/len(change_in_revenue),2)}\n')
	file_write.write(f'Greatest Increase in Profits: {max_month} (${maximum_change})\n')
	file_write.write(f'Greatest Decrease in Profits: {min_month} (${minimum_change})')








