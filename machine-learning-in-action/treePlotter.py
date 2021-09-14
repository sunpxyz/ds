# -*- coding: utf-8 -*-

'''
    treePlotter.py
    2018/04/05
'''


# import matplotlib.pyplot as plt
#
#
# decisionNode = dict(boxstyle="sawtooth", fc="0.8")
# leafNode = dict(boxstyle="round4", fc="0.8")
# arrow_args = dict(arrowstyle="<-")
#
#
# #########################
# def plotNode(nodeTxt, centerPt, parentPt, nodeType):
#     '''
#     下面这个函数原型是class matplotlib.axes.Axes()的成员函数annotate()
#     该函数的作用是为绘制的图上指定的数据点xy添加一个注释nodeTxt,注释的位置由xytext指定
#     其中，xycoords来指定点xy坐标的类型，textcoords指定xytext的类型，xycoords和textcoords的取值如下：
#     ‘figure points’：此时坐标表示坐标原点在图的左下角的数据点
#     ‘figure pixels’：此时坐标表示坐标原点在图的左下角的像素点
#     ‘figure fraction’：此时取值是小数，范围是([0, 1], [0, 1])
#                         ，在图的最左下角时xy是(0,0), 最右上角是(1, 1)
#                         ，其他位置按相对图的宽高的比例取小数值
#     ‘axes points’：此时坐标表示坐标原点在图中坐标的左下角的数据点
#     ‘axes pixels’：此时坐标表示坐标原点在图中坐标的左下角的像素点
#     ‘axes fraction’：类似‘figure fraction’，只不过相对图的位置改成是相对坐标轴的位置
#     ‘data’：此时使用被注释的对象所采用的坐标系（这是默认设置），被注释的对象就是调用annotate这个函数
#             那个实例，这里是ax1，是Axes类，采用ax1所采用的坐标系
#     ‘offset points’：此时坐标表示相对xy的偏移（以点的个数计），不过一般这个是用在textcoords
#     ‘polar’：极坐标类型，在直角坐标系下面也可以用，此时坐标含义为(theta, r)
#
#     参数arrowprops含义为连接数据点和注释的箭头的类型，该参数是dictionary类型，该参数含有一个
#     名为arrowstyle的键，一旦指定该键就会创建一个class matplotlib.patches.FancyArrowPatch类的实例
#     该键取值可以是一个可用的arrowstyle名字的字符串，也可以是可用的class matplotlib.patches.ArrowStyle类的实例
#     具体arrowstyle名字的字符串可以参考
#     http://matplotlib.org/api/patches_api.html#matplotlib.patches.FancyArrowPatch
#     里面的class matplotlib.patches.FancyArrowPatch类的arrowstyle参数设置
#
#     函数返回一个类class matplotlib.text.Annotation()的实例
#     '''
#     createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction', va='center', ha='center', bbox=nodeType,
#                             arrowprops=arrow_args)
#
#
# #########################
# def createPlot():
#     fig = plt.figure(1, facecolor='white')  # 创建新的figure 1, 背景颜色为白色
#     fig.clf()  # 清空figure 1的内容
#     '''
#      在新建的figure 1里面创建一个1行1列的子figure的网格,并把网格里面第1个子figure的Axes实例axes返回给ax1作为函数createPlot()的属性
#     ，这个属性ax1相当于一个全局变量,可以给plotNode函数使用
#     '''
#     createPlot.ax1 = plt.subplot(111, frameon=False)
#     plotNode('a decision node', (0.5, 0.1), (0.1, 0.5), decisionNode)
#     plotNode('a leaf node', (0.8, 0.1), (0.3, 0.8), leafNode)
#     plt.show()
#
#
# #########################
# def getNumLeafs(myTree):
#     numLeafs = 0
#     firstStr = myTree.keys()[0]
#     secondDict = myTree[firstStr]
#     for key in secondDict.keys():
#         if type(secondDict[key]).__name__ == 'dict':
#             numLeafs += getNumLeafs(secondDict[key])
#         else:
#             numLeafs += 1
#
#     return numLeafs
#
#
# ##########################
# def getTreeDepth(myTree):
#     maxDepth = 0
#     firstStr = myTree.keys()[0]
#     secondDict = myTree[firstStr]
#     for key in secondDict.keys():
#         if type(secondDict[key]).__name__ == 'dict':
#             thisDepth = 1 + getTreeDepth(secondDict[key])
#         else:
#             thisDepth = 1
#         if thisDepth > maxDepth:
#             maxDepth = thisDepth
#
#     return maxDepth
#
#
# ##########################
# def plotMidText(cntrPt, parentPt, txtString):
#     xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
#     yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
#     createPlot.ax1.text(xMid, yMid, txtString)
#
#
# ##########################
# def plotTree(myTree, parentPt, nodeTxt):
#     numLeafs = getNumLeafs(myTree)
#     depth = getTreeDepth(myTree)
#     firstStr = myTree.keys()[0]
#     cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW, plotTree.yOff)
#     plotMidText(cntrPt, parentPt, nodeTxt)
#     plotNode(firstStr, cntrPt, parentPt, decisionNode)
#     secondDict = myTree[firstStr]
#     plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
#     for key in secondDict.keys():
#         if type(secondDict[key]).__name__ == 'dict':
#             plotTree(secondDict[key], cntrPt, str(key))
#         else:
#             plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
#             plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
#             plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
#     plotTree.yOff = plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD
#
#
# ###########################
# def createPlot(inTree):
#     fig = plt.figure(1, facecolor='white')
#     fig.clf()
#     axprops = dict(xticks = [], yticks = [])
#     createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
#     plotTree.totalW = float(getNumLeafs(inTree))
#     plotTree.totalD = float(getTreeDepth(inTree))
#     plotTree.xOff = -0.5 / plotTree.totalW
#     plotTree.yOff = 1.0
#     plotTree(inTree, (0.5, 1.0), '')
#     plt.show()
#
#
# ###################################
# def retrieveTree(i):
#     listOfTrees = [{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
#                    {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}]
#
#     return listOfTrees[i]

#------------------------------------------------------
import matplotlib.pyplot as plt

decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round", fc="0.8")
arrow_args = dict(arrowstyle="<-")


##############################
def getNumLeafs(myTree):
    numLeafs = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[
                    key]).__name__ == 'dict':  # test to see if the nodes are dictonaires, if not they are leaf nodes
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs


##############################
def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = myTree.keys()[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[
                    key]).__name__ == 'dict':  # test to see if the nodes are dictonaires, if not they are leaf nodes
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth: maxDepth = thisDepth
    return maxDepth


##############################
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',
                            xytext=centerPt, textcoords='axes fraction',
                            va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)


##############################
def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString, va="center", ha="center", rotation=30)


##############################
def plotTree(myTree, parentPt, nodeTxt):  # if the first key tells you what feat was split on
    numLeafs = getNumLeafs(myTree)  # this determines the x width of this tree
    depth = getTreeDepth(myTree)
    firstStr = myTree.keys()[0]  # the text label for this node should be this
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW, plotTree.yOff)
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[
                    key]).__name__ == 'dict':  # test to see if the nodes are dictonaires, if not they are leaf nodes
            plotTree(secondDict[key], cntrPt, str(key))  # recursion
        else:  # it's a leaf node print the leaf node
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD


##############################
def createPlot(inTree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)  # no ticks
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5 / plotTree.totalW;
    plotTree.yOff = 1.0;
    plotTree(inTree, (0.5, 1.0), '')
    plt.show()


##############################
def retrieveTree(i):
    listOfTrees = [{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                   {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}
                   ]
    return listOfTrees[i]

# createPlot(thisTree)
