
import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    '''
    The input: [personA, personB]
    personA: name of person
    personB: names of friends
    '''
    pair = tuple(sorted(record))
    
    mr.emit_intermediate(pair,1)

def reducer(pair, list_of_values):
         
     if len(list_of_values) == 1:    
        mr.emit( (pair[0], pair[1]) )
        mr.emit( (pair[1], pair[0]) )


inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)