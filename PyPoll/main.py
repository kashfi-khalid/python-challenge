import os
import csv
import collections


file_path = os.path.join(os.getcwd(), 'Resources', 'election_data.csv')


# Opening the data file
with open(file_path, 'r') as csv_file:

	csv_reader = csv.reader(csv_file, delimiter=',')

	header = next(csv_reader)

	vote_list = list()
	candidate_list = list()

	for c in csv_reader:
		vote_list.append(c[0])
		candidate_list.append(c[2])

	
	total_votes = len(vote_list)

	print('Election Results')
	print('-------------------------')
	print(f'Total Votes: {total_votes}')

	# print(set(candidate_list))

	candiate_list_with_votes = dict(collections.Counter(candidate_list))

	result_dict = dict()

	for key, value in candiate_list_with_votes.items():

		result_dict[key] = round(value/total_votes * 100,3)


	for cand, val in result_dict.items():
		cand_votes = candiate_list_with_votes.get(cand)

		print(f"{cand}: {val}% ({cand_votes})")

	print('-------------------------')

	winner_details = max(result_dict, key=result_dict.get)

	print(f"Winner: {winner_details}")

	print('-------------------------')



analysis_file_path = os.path.join(os.getcwd(), 'analysis', 'output.txt')

with open(analysis_file_path, 'w') as file_write:
	file_write.write('Election Results\n')
	file_write.write('-------------------------\n')
	file_write.write(f'Total Votes: {total_votes}\n')
	file_write.write('-------------------------\n')

	for cand, val in result_dict.items():
		file_write.write(f"{cand}: {val}% ({candiate_list_with_votes.get(cand)})\n")

	file_write.write('-------------------------\n')
	file_write.write(f"Winner: {winner_details}\n")
	file_write.write('-------------------------')





