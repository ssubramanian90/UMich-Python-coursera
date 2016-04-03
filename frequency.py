from __future__ import division
import sys
import json

def main():
	tweetfile=open(sys.argv[1])
	termdict={}
	tweets=[]
	total=0
	for line in tweetfile:
		line=line.strip()
		tweets.append(json.loads(line))
    	for tweet in tweets:
		if 'text' in tweet:			
			tweetsplit=tweet['text'].split()
			for i in tweetsplit:
				if termdict.has_key(i):
					termdict[i]+=1
				else:
					termdict[i]=1
				total+=1
	for i in sorted(termdict, key=termdict.get):
		print i +'%.3f'%(termdict[i]/total)

	
if __name__ == '__main__':
 	main()
