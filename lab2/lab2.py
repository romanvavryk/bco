f_string = [i.strip('\n').split(',') for i in open('data.txt')]

for i in range(0, 3):
	for j in range(0, 5):
		f_string[i][j] = float(f_string[i][j])

res_matrix_1 = []

for i in range(0, 3):
	lst = []
	for j in range(1, 5):
		value = f_string[i][j] * f_string[i][0] / max(f_string[i])
		lst.append(value)
	res_matrix_1.append(lst)

# for i in res_matrix_1:
# 	print (i)

transponse_res_matrix_1 = [[res_matrix_1[j][i] for j in range(len(res_matrix_1))] for i in range(len(res_matrix_1[0]))] 

# print(transponse_res_matrix_1)

def minimax():
	value_list = []
	
	for i in range(0, 4):
		min_value = max(transponse_res_matrix_1[i])
		value_list.append(min_value)

	res = min(value_list)
	res_index = value_list.index(res) + 1

	print('mini_max method res')
	print('№', res_index, ', value = ', res)

def max_min():
	value_list = []
	
	for i in range(0, 4):
		min_value = min(transponse_res_matrix_1[i])
		value_list.append(min_value)

	res = max(value_list)
	res_index = value_list.index(res) + 1

	print('max_min method res')
	print('№', res_index, ', value = ', res)

def adaptive():
	all_values = []

	for i in range(0, 4):
		value = sum(transponse_res_matrix_1[i])
		all_values.append(value)

	for i in range(0, 4):
		print(f'Stanok {i + 1} = ', all_values[i])

	res = max(all_values)
	res_index = all_values.index(res) + 1

	print('adaptive method res')
	print('№', res_index, ', value = ', res)

def multiply():
	all_values = []

	for i in range(0, 4):
		res = 1
		for j in transponse_res_matrix_1[i]:
			res *= j
		all_values.append(res)
	print(all_values)

	for i in range(0, 4):
		print(f'Stanok {i + 1} = ', all_values[i])

	res = max(all_values)
	res_index = all_values.index(res) + 1

	print('multiply method res')
	print('№', res_index, ', value = ', res)

minimax() 
max_min()
multiply()
adaptive()