


from datetime import datetime

print(datetime.now())

birthday = datetime(1998, 3, 19, 4, 25, 12)

print(birthday)

print(birthday.year)

print(birthday.weekday())



print(datetime(2018, 1, 1) - datetime(2017,1,1,))

print(datetime.now()- birthday)

parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y')

print(parsed_date)

date_string = datetime.strftime(datetime.now(), '%b %d, %Y')

print()

print(date_string)

#https://www.youtube.com/watch?v=tOD6g7rF7NA
#essentially youre given an arbitrarily long str of pi integers, a list of strings of digits. 
#Some of the strings can be found in the str of pi integers, enough of the strings of digits in the list will be able to be composed to create the string of pi digits you were given
#You need to use those two inputs to output a string of the pi integers you were initially given. 
#However you have to compose it with the strings from the list and have spaces in between the strings from the list that you used
#You also need to output the string with the fewest spaces possible 
#If you can make the initial string of pi integers multiple ways using the strings in the list, you have to give the one using the fewest strings from the list



pi_input = '3141592653589793238462643383279'
fav_nums = ['314', '49', '9001', '15926535897', '14', '9323', '8462643383279', '4', '793']
match_string = ''
space_string = ''
fav_nums_adj = fav_nums
pi_adj = pi_input
soln_dict = {}

#different test inputs:
#pi_input = "3141592"
#fav_nums = ['3', '1592','2','141','14','314159']
#fav_nums_adj = fav_nums
#pi_adj = pi_input
filler_match_string = match_string
filler_space_string = space_string

def check(fav_nums_adj, pi_adj, match_string, space_string,filler_match_string,filler_space_string):
	if match_string != pi_input:
		for num in fav_nums_adj:
			if num == pi_adj[:len(num)]:
				filler_match_string = match_string
				filler_space_string = space_string
				filler_pi_adj = pi_adj
				match_string += num
				space_string += num + " "
				pi_adj = pi_adj[len(num):]
				check(fav_nums_adj, pi_adj, match_string, space_string,filler_match_string,filler_space_string)
				match_string = filler_match_string
				space_string = filler_space_string
				pi_adj = filler_pi_adj
	else:
		count = 0
		for char in space_string:
			if char == " ":
				count += 1

		soln_dict[space_string] = count


check(fav_nums_adj, pi_adj, match_string, space_string,filler_match_string,filler_space_string)

min_space_num = float('inf')
best_soln = ''
for soln in soln_dict:
	if soln_dict[soln] < min_space_num:
		min_space_num = soln_dict[soln]

index = 0
for num in soln_dict.values():
	if num == min_space_num:
		print(list(soln_dict.keys())[index][:-1])
	index += 1





