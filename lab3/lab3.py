import itertools

f_string = [i.strip('\n').split(',') for i in open('data.txt')]

for i in range(0, 18):
	for j in range(0, 3):
		f_string[i][j] = float(f_string[i][j]) * float(f_string[18][j])

f_string.pop(18)
# print(len(f_string))
for i in f_string:
	print(i)

a_test = f_string

res_arr = []

for i in range(0, 18):
	test = a_test[i]
	for j in range(0, 18):
		if test[0] > a_test[j][0] and test[1] > a_test[j][1]  and test[2] > a_test[j][2]:
			# f_string.remove(a_test[i])
			res = a_test[i]
			res_arr.append(res)
		else:
			continue

res_arr.sort()
res_arr = list(res_arr for res_arr,_ in itertools.groupby(res_arr))

# for i in res_arr:
# 	print(i)

for i in range(0, len(res_arr) ):
	f_string.remove(res_arr[i])

# print(len(f_string))
# for i in f_string:
# 	print(i)