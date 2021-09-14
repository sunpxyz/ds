'''
    source.py
'''

# import kNN
#
# group, labels = kNN.createDataSet()
#
# print group
# print labels


#------------------------------------------------------------------

# import feedparser
# import bayes
#
# #bayes.testingNBx()
#
# ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
# sf = feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')
#
# vocabList, pSF, pNY = bayes.localWords(ny, sf)



#------------------------------------------------------------------

# import trees
#
# myDat, labels = trees.createDataSet()
# myTree = trees.createTree(myDat, labels)
#
# print myTree


#------------------------------------------------------------------
# import treePlotter
#
# treePlotter.createPlot()


#------------------------------------------------------------------
# from sklearn import datasets
#
# iris = datasets.load_iris()
#
# from sklearn.naive_bayes import GaussianNB
#
# gnb = GaussianNB()
#
# y_pred = gnb.fit(iris.data, iris.target).predict(iris.data)
#
# print "Number of mislabeled points out of a total %d points : %d" % (iris.data.shape[0],(iris.target != y_pred).sum())


#------------------------------------------------------------------
# import treePlotter
# import trees
#
# myData, labels = trees.createDataSet()
# myTree = treePlotter.retrieveTree(0)
#
# print trees.classify(myTree, labels, [1,1])


#------------------------------------------------------------------
# import logRegres
# from numpy import *
#
# #dataArr, labelMat = logRegres.loadDataSet()
# #weights = logRegres.gradAscent(dataArr, labelMat)
# #weights = logRegres.stocGradAscent0(dataArr, labelMat)
# #weights = logRegres.stocGradAscent1(array(dataArr), labelMat, 500)
# #logRegres.plotBestFit(weights)
#
# logRegres.multiTest()


#------------------------------------------------------------------
from numpy import *
import kNN
import matplotlib
import matplotlib.pyplot as plt

# datingDataMat, datingLabels =kNN.file2matrix('datingTestSet2.txt')
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(datingDataMat[:,0], datingDataMat[:,1], 15.0*array(datingLabels),15.0*array(datingLabels))
# plt.show()

# kNN.datingClassTest()
# kNN.classifyPerson()

# testVector = kNN.img2vector('data/digits/testDigits/0_13.txt')
# print testVector[0, 0:31]

# kNN.handwritingClassTest()


#------------------------------------------------------------------
import svmMLiA

dataArr, labelArr = svmMLiA.loadDataSet('data/testSet.txt')
b, alphas = svmMLiA.smoSimple(dataArr, labelArr, 0.6, 0.001, 40)
print b
print alphas[alphas>0]