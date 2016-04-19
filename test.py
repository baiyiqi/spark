__author__ = 'yiqibai'

from pyspark import SparkConf, SparkContext
import collections

conf = SparkConf().setMaster("local").setAppName("RatingHistogram")
sc = SparkContext(conf = conf)

lines = sc.textFile("file:///Users/yiqibai/PycharmProjects/spark/ml-100k/u.data")
ratings = lines.map(lambda x : x.split()[2])
result = ratings.countByValue()

sortedResults = collections.OrderedDict(sorted(result.items()))
for key, value in sortedResults.iteritems():
    print "%s, %i" % (key, value)

print " this is to test github"