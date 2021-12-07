
large_reading = 1000000000000

def day_1_part_1():
	print("\nDAY 1 PART 1")
	filename = "AdventOfCodeDay1Input"
	increase_count = 0
	with open(filename, "r") as f:
		prev_reading = large_reading
		for line in f.readlines():
			current_reading = int(line)
			if (current_reading > prev_reading):
				increase_count += 1
			prev_reading = current_reading
	print(increase_count)


def day_1_part_2():
	print("\nDAY 1 PART 2")
	filename = "AdventOfCodeDay1Input"
	increase_count = 0
	with open(filename, "r") as f:
		prev_prev_reading = large_reading
		prev_reading = large_reading
		prev_window_sum = large_reading * 3
		for line in f.readlines():
			current_reading = int(line)
			current_window_sum = current_reading + prev_reading + prev_prev_reading
			if (current_window_sum > prev_window_sum):
				increase_count += 1
			prev_prev_reading = prev_reading
			prev_reading = current_reading
			prev_window_sum = current_window_sum
	print(increase_count)


def day_2_part_1():
	print("\nDAY 2 PART 1")
	filename = "AdventOfCodeDay2Input"
	increase_count = 0
	horizontal_position = 0
	depth = 0
	with open(filename, "r") as f:
		for line in f.readlines():
			line_array = line.split()
			instruction = line_array[0]
			magnitude = int(line_array[1])
			if instruction == 'forward':
				horizontal_position += magnitude
			elif instruction == 'down':
				depth += magnitude
			elif instruction == 'up':
				depth -= magnitude
	print(horizontal_position)
	print(depth)
	print(horizontal_position * depth)


def day_2_part_2():
	print("\nDAY 2 PART 2")
	filename = "AdventOfCodeDay2Input"
	increase_count = 0
	horizontal_position = 0
	depth = 0
	aim = 0
	with open(filename, "r") as f:
		for line in f.readlines():
			line_array = line.split()
			instruction = line_array[0]
			magnitude = int(line_array[1])
			if instruction == 'forward':
				horizontal_position += magnitude
				depth += aim * magnitude
			elif instruction == 'down':
				aim += magnitude
			elif instruction == 'up':
				aim -= magnitude
	print(horizontal_position)
	print(depth)
	print(horizontal_position * depth)


def day_3_part_1():
	print("\nDAY 3 PART 1")
	filename = "AdventOfCodeDay3Input"
	gamma_rate_str = ""
	epsilon_rate_str = ""
	balance = [0 for i in xrange(12)]
	file_contents = []
	with open(filename, "r") as f:
		file_contents = f.readlines()
	(gamma_rate_arr, epsilon_rate_arr) = calculate_most_common_bits(file_contents)
	gamma_rate = int("".join(gamma_rate_arr), 2)
	epsilon_rate = int("".join(epsilon_rate_arr), 2)
	print(gamma_rate)
	print(epsilon_rate)
	print(gamma_rate * epsilon_rate)


def day_3_part_2():
	print("\nDAY 3 PART 2")
	filename = "AdventOfCodeDay3Input"
	gamma_rate_str = ""
	epsilon_rate_str = ""
	bits_per_line = 12
	balance = [0 for i in xrange(bits_per_line)]
	file_contents = []
	most_common_bit = []
	least_common_bit = []
	with open(filename, "r") as f:
		file_contents = f.readlines()
	(most_common_bit, least_common_bit) = calculate_most_common_bits(file_contents)

	#OXYGEN GENERATOR RATING
	oxygen_generator_readings = file_contents
	for bit in xrange(bits_per_line):
		temp_oxygen_generator_readings = []
		for line in oxygen_generator_readings:
			if most_common_bit[bit] == line[bit]:
				temp_oxygen_generator_readings.append(line)
		oxygen_generator_readings = temp_oxygen_generator_readings
		if len(oxygen_generator_readings) == 1:
			oxygen_generator_reading = int("".join(oxygen_generator_readings[0]), 2)
		(most_common_bit, least_common_bit) = calculate_most_common_bits(oxygen_generator_readings)
	print(oxygen_generator_reading)

	#CO2 SCRUBBER RATING
	co2_scrubber_readings = file_contents
	for bit in xrange(bits_per_line):
		temp_co2_scrubber_readings = []
		for line in co2_scrubber_readings:
			if least_common_bit[bit] == line[bit]:
				temp_co2_scrubber_readings.append(line)
		co2_scrubber_readings = temp_co2_scrubber_readings
		if len(co2_scrubber_readings) == 1:
			co2_scrubber_reading = int("".join(co2_scrubber_readings[0]), 2)
		(most_common_bit, least_common_bit) = calculate_most_common_bits(co2_scrubber_readings)
	print(co2_scrubber_reading)

	print(co2_scrubber_reading * oxygen_generator_reading)


def calculate_most_common_bits(lines_to_check):
	most_common_bit = ["" for i in xrange(12)]
	least_common_bit = ["" for i in xrange(12)]
	balance = [0 for i in xrange(12)]
	for line in lines_to_check:
		bit_count = 0
		for bit in line:
			if (bit == "1"):
				balance[bit_count] += 1
			elif (bit == "0"):
				balance[bit_count] -= 1
			bit_count += 1
	bit_count = 0
	for bit in balance:
		if bit >= 0:
			most_common_bit[bit_count] = "1"
			least_common_bit[bit_count] = "0"
		elif bit < 0:
			most_common_bit[bit_count] = "0"
			least_common_bit[bit_count] = "1"
		bit_count += 1
	return (most_common_bit, least_common_bit)


def find_oxygen_reading(lines_to_check, bit_number, bit_value):
	lines_to_keep = []
	for line in lines_to_check:
		if line[bit_number] == bit_value:
			lines_to_keep.append(line)
	return lines_to_keep


def day_4_part_1():
	print("\nDAY 4 PART 1")
	filename = "AdventOfCodeDay4Input"
	lines = []
	with open(filename) as f:
		lines = f.readlines()
	bingo_calls = lines[0].split(',')
	(boards, boards_dict) = create_bingo_boards(lines[2:])
	for call in bingo_calls:
		for board_number in boards_dict[call]:
			boards[board_number] = [['X' if number == call else number for number in line] for line in boards[board_number]]
			if check_bingo_board_for_bingo(boards[board_number]):
				print(boards[board_number])
				print(add_remaining_numbers_on_board(boards[board_number]) * int(call))
				return


def day_4_part_2():
	print("\nDAY 4 PART 2")
	filename = "AdventOfCodeDay4Input"
	lines = []
	with open(filename) as f:
		lines = f.readlines()
	bingo_calls = lines[0].strip('\n').split(',')
	print(bingo_calls)
	(boards, boards_dict) = create_bingo_boards(lines[2:])
	boards_not_yet_won = [i for i in xrange(len(boards))]
	for call in bingo_calls:
		for board_number in boards_dict[call]:
			if board_number in boards_not_yet_won:
				boards[board_number] = [['X' if number == call else number for number in line] for line in boards[board_number]]
				if check_bingo_board_for_bingo(boards[board_number]):
					if len(boards_not_yet_won) == 1:
						last_winning_board_number = boards_not_yet_won[0]
						print(boards[last_winning_board_number])
						print(add_remaining_numbers_on_board(boards[last_winning_board_number]) * int(call))
						return
					boards_not_yet_won.remove(board_number)

def create_bingo_boards(lines):
	board_number = 0
	boards = []
	boards_dict = {}
	board_line = 0
	for line in lines:
		if board_line == 0:
			boards.append([[] for i in xrange(5)])
		if board_line < 5:
			for number in line.split():
				boards[board_number][board_line].append(number)
				if (not number in boards_dict.keys()):
					boards_dict[number] = set()
				boards_dict[number].add(board_number)
			board_line += 1
		if line == '\n':
			board_line = 0
			board_number += 1
	return (boards, boards_dict)


def check_bingo_board_for_bingo(board):
	for line in board:
		if line == ['X','X','X','X','X']:
			return True
	transposed_board = zip(*board)
	for line in transposed_board:
		if line == ('X','X','X','X','X'):
			return True
	return False

def add_remaining_numbers_on_board(board):
	total = 0
	for line in board:
		for number in line:
			if number != 'X':
				total += int(number)
	return total



# day_1_part_1()
# day_1_part_2()
# day_2_part_1()
# day_2_part_2()
# day_3_part_1()
# day_3_part_2()
day_4_part_1()
day_4_part_2()



