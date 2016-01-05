from pyspark import SparkContext 
from pyspark import SparkConf
import sys, operator
import re, string
import json

def add_pairs((a,b), (c,d)):
    return ((a+c), (b+d))
    
inputs = sys.argv[1]
output = sys.argv[2]
 
conf = SparkConf().setAppName('reddit averages')
sc = SparkContext()

text = sc.textFile(inputs)

jsonrdd=text.map(lambda x: json.loads(x)).map(lambda line: (line['subreddit'],(line['score'],1)))

jred=jsonrdd.reduceByKey(add_pairs).coalesce(1)

jdump=jred.map(lambda (w,(a,b)):(w,float(a)/b)).map(lambda djson:(json.dumps(djson)))

jdump.saveAsTextFile(output)