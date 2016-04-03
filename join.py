
import MapReduce
import sys

TABLE_1 = 'order'
TABLE_2 = 'line_item'

mr = MapReduce.MapReduce()


def mapper(record):
    tablename = record[0]
    order_id = record[1]
    fields = record[2:]
    
    mr.emit_intermediate( order_id, [ tablename, fields] )

def reducer(key, list_of_values):
    '''
    The output should be a joined record.
    '''
    table1 = [table[1] for table in list_of_values if table[0] == TABLE_1 ]
    table2 = [table[1] for table in list_of_values if table[0] == TABLE_2 ]

    for record1 in table1:
        for record2 in table2:
            res = []

            res.append(TABLE_1)
            res.append(key)
            res.extend(record1)
            res.append(TABLE_2)
            res.append(key)
            res.extend(record2)           

            mr.emit( res )


inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)