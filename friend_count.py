
import MapReduce
import sys

mr = MapReduce.MapReduce()


def mapper(record):
    '''
    The input: [personA, personB]
    personA: name of person
    personB: names of friends
    '''
    person = record[0]
    
    mr.emit_intermediate(person,1)

def reducer(person, list_of_values):
         
    mr.emit( ( person, len(list_of_values)) )


inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)