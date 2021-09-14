'''
    kMeans.py
    2018/08/09
'''

# from numpy import *
import numpy as np


def loadDataSet(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float, curLine)
        dataMat.append(fltLine)
    return np.mat(dataMat)


def distEclud(vecA,vecB):
    return np.sqrt(np.sum(np.power(np.array(vecA)-np.array(vecB), 2)))


def randCent(dataSet, k):
    dataSet = np.mat(dataSet)  #Added at 2018-08-09
    n = np.shape(dataSet)[1]
    centroids = np.mat(np.zeros((k,n)))
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = minJ + rangeJ * np.random.rand(k,1)
    return centroids


def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = np.shape(dataSet)[0]
    clusterAssment = np.mat(np.zeros((m,2)))
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = np.inf; minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j,:], dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i,0] != minIndex:
                clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        print centroids
        for cent in range(k):
            ptsInClust = dataSet[np.nonzero(clusterAssment[:,0].A == cent)[0]]
            centroids[cent,:] = np.mean(ptsInClust,axis=0)
    return centroids, clusterAssment


def biKmeans(dataSet, k ,distMeas=distEclud):
    m = np.shape(dataSet)[0]
    clusterAssment = np.mat(np.zeros((m,2)))
    centroid0 = np.mean(dataSet, axis=0).tolist()[0]
    centList = [centroid0]
    for j in range(m):
        clusterAssment[j,1] = distMeas(np.mat(centroid0), dataSet[j,:1]) ** 2
    while (len(centList) < k):
        lowestSSE = np.inf
        for i in range(len(centList)):
            ptsInCurrCluster = dataSet[np.nonzero(clusterAssment[:,0].A==i)[0],:]
            centroidMat, splitClustAss = kMeans(ptsInCurrCluster, 2, distMeas)
            sseSplit = np.sum(splitClustAss[:,1])
            sseNotSplit = np.sum(clusterAssment[np.nonzero(clusterAssment[:,0].A==i)[0],1])
            print "sseSplit, and notSplit:",sseSplit,sseNotSplit
            if (sseSplit + sseNotSplit) < lowestSSE:
                bestCentToSplit = i
                bestNewCents = centroidMat
                bestClustAss = splitClustAss.copy()
                lowestSSE = sseSplit + sseNotSplit
        bestClustAss[np.nonzero(bestClustAss[:,0].A == 1)[0],0] = len(centList)
        bestClustAss[np.nonzero(bestClustAss[:, 0].A == 1)[0], 0] = bestCentToSplit
        print "the bestCentToSplit is:",bestCentToSplit
        print "the len of bestClustAss is:",len(bestClustAss)
        centList[bestCentToSplit] = bestNewCents[1,:]
        clusterAssment[np.nonzero(clusterAssment[:,0].A==bestCentToSplit)[0],:] = bestClustAss
    return np.mat(centList),clusterAssment



dataMat = loadDataSet('data/testSet2.txt')
# randCent(dataMat,2)
# print randCent(dataMat,2)
# print distEclud(dataMat[0],dataMat[1])
# a = [1,2,3]
# b = [4,5,6]
# print distEclud(a,b)
centroids,clusterAssment = biKmeans(dataMat,3)