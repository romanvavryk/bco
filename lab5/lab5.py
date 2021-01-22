import pandas

f_string = [i.strip('\n').split(',') for i in open('data.txt')]

for i in range(0, 5):
	for j in range(0, 3):
		f_string[i][j] = float(f_string[i][j])

weights = f_string[4] 

L = [(10 * i) for i in weights]

f_string.pop(4)

columns_names = ['Ціна', 'Відстань', 'Площа']
row_names = ['A', 'B', 'C', 'D']

data_frame = pandas.DataFrame(data=f_string, columns=columns_names, index=row_names)


def сoncordance():
	сoncordance_matrix = pandas.DataFrame(index=row_names, columns=row_names)
	weight_sum = sum(weights)
	for i in row_names:
	    for j in row_names:
	        if i != j:
	            test = 0
	            for k in range(len(columns_names)):
	                if data_frame.loc[i][k] > data_frame.loc[j][k]:
	                    weight_sum += weights[k]
	            сoncordance_matrix.loc[i][j] = test / weight_sum
	
	return сoncordance_matrix

def discordance():
	discordance_matrix = pandas.DataFrame(index=row_names, columns=row_names)
	for i in row_names:
	    for j in row_names:
	        if i != j:
	            list_ = []
	            for k in range(len(columns_names)):
	                res = (data_frame.loc[i][k]-data_frame.loc[j][k])/L[k]
	                list_.append(res)
	            discordance_matrix.loc[i][j] = max(list_)

	return discordance_matrix

сoncordance = сoncordance()
discordance = discordance()

сoncordance_arr = []
discordance_arr = []

for i, column in enumerate(row_names):
    сoncordance_arr.append(сoncordance[column].max())
    discordance_arr.append(discordance[column].min())

dictionary = dict(zip(row_names, discordance_arr))

for k,v in sorted(dictionary.items(), key=lambda p:p[1], reverse=True):
	print(f'{k}, {v}')