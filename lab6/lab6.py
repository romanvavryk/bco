import numpy
import pandas

input_data = pandas.read_csv('data.csv')

tuple_1 = pandas.read_csv('data_1.csv')
tuple_2 = pandas.read_csv('data_2.csv')
tuple_3 = pandas.read_csv('data_3.csv')
tuple_4 = pandas.read_csv('data_4.csv')

test_value = 3

def output_vector(dataframe):
    result_arr = []
    test_value = dataframe.iloc[0].size

    for i in dataframe.product(axis=1)**(test_value**(-1)):
        result_arr.append(i / sum(dataframe.product(axis=1)**(test_value**(-1))))
    
    return result_arr

input_vector = output_vector(input_data)

vector_1 = output_vector(tuple_1)
vector_2 = output_vector(tuple_2)
vector_3 = output_vector(tuple_3)
vector_4 = output_vector(tuple_4)

dataframe = pandas.DataFrame(data=numpy.c_[vector_1, vector_2, vector_3, vector_4], index=tuple_1.columns, columns=input_data.columns)

def alternates():
	output_dict ={'Вхідні дані' : input_data, 'Альтернатива №1:' : tuple_1, 'Альтернатива №2:' : tuple_2, 'Альтернатива №3:' : tuple_3, 'Альтернатива №3:' : tuple_4, 'Альтернатива №4:' : tuple_4}
	for k, v in output_dict.items():
		print(k, v)

def vectors():
	output_dict = {'Вхідний вектор =' : input_vector, 'vector №1' : vector_1, 'vector №2' : vector_2, 'vector №3' : vector_3, 'vector №4' : vector_4}
	for k, v in output_dict.items():
		print(k, v)

def results():
	test_list = list(numpy.zeros(test_value))
	
	for i in range(test_value):
	    for j in range(test_value + 1):
	        test_list[i] += dataframe.iloc[i][j] * input_vector[j]

	dataframe['Рейтинг'] = test_list
	print(dataframe.sort_values(['Рейтинг']).reset_index())

# alternates()
# vectors()
# results()