import google.cloud.dataflow as df

def parse_record(e):
	import json
	r=json.load(e)
	return r['ProductId'],r['Price']
##Returns key-value pairs of product ID and price

def run():
	parser=argparse.ArgumentParser()
	parser.add_argument('--input')
	parser.add_argument('--output')
	known_args, pipeline_args=parser.parse_known_args(sys.srgv)

	p=df.Pipeline(‘DirectPipelineRunner‘)
	(p
		| df.io.Read(df.io.TextFileSource('datain'))
		|df.Map(parse_record)
		|df.CombinePerKey(sum)##(k,v) =>k,sum(v....)
		|df.io.Write(df.io.TextFileSink('dataout'))
	)
	p.run()
run()

#Thus we have built a pipeline to map and combine. We are writing into a Sinkfile.
# Now we can write python googlecloudplatform.py --input --output

#For BigQuery


def parse_record(e):
	import json
	r=json.load(e)
	yield r['ProductId'],r['Price']
##Returns key-value pairs of product ID and price

def run():
	parser=argparse.ArgumentParser()
	parser.add_argument('--input')
	parser.add_argument('--output')
	known_args, pipeline_args=parser.parse_known_args(sys.srgv)

	p=df.Pipeline(‘DirectPipelineRunner‘)
	(p
		| df.io.Read(df.io.TextFileSource('datain'))
		|df.FlatMap(parse_record)
		|df.CombinePerKey(sum)##(k,v) =>k,sum(v....)
		|df.Map(lambda(pr,v)
		|df.io.Write(df.io.BigQuerySink(known_args.output, schema='ProductId: INTEGER, Value:FLOAT'))
	)
	p.run()
run()
## python current.py\ -- project siviuc-dataflow\ --job_name silviuc-demo\--runner BlockingDataflowPiplelineRunner \ --num_workers 10\
##					  --input gs://silviuc-dataflow/demo/events (A BigQuery Table)
##						--output 
##						--staginglocation

## In terms of batch, it is pretty similar to Spark
##
