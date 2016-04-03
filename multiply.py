
import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    # record: [matrix, i, j, value]
    for i in range(5):
    	if record[0]=="a":
    		mr.emit_intermediate((record[1], i), record)
    	else:
    		mr.emit_intermediate((i, record[2]), record)

def reducer(key, list_of_values):
    # split the list into two parts
    a_value = {}
    b_value = {}
    for record in list_of_values:
    	if record[0]=="a":
    		a_value[record[2]] = record[3]
    	else:
    		b_value[record[1]] = record[3]
    sum = 0
    for col_num in a_value:
    	if col_num in b_value:
    		sum += a_value[col_num]*b_value[col_num]
    mr.emit(key+(sum,))

   



inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
