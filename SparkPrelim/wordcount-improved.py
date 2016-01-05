from pyspark import SparkContext 
from pyspark import SparkConf
import sys, operator
import re, string
import unicodedata
 
inputs = sys.argv[1]
output = sys.argv[2]
 
conf = SparkConf().setAppName('word count')
sc = SparkContext()

text = sc.textFile(inputs)

wordsep= re.compile(r'[%s\s]+' % re.escape(string.punctuation))

words1=text.flatMap(lambda line: wordsep.split(line.lower())).filter(lambda x: len(x) > 0)

#words2=words1.map(lamda w1 : unicodedata.normalize('NFD', w1))

words = words1.map(lambda w: (unicodedata.normalize('NFD', w), 1))

wordcount = words.reduceByKey(operator.add).coalesce(1).cache()

outdata = wordcount.sortBy(lambda (w,c): w).map(lambda (w,c): u"%s %i" % (w, c))

outdata.saveAsTextFile(output + '/byword')

outdata1=wordcount.sortBy(lambda (w,c): (-c,w)).map(lambda (w,c): u"%s %i" % (w, c))

outdata1.saveAsTextFile(output + '/by-freq')
#outdata.saveAsTextFile(output+ '/by-freq')