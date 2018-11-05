#############################################
##
## CSI 431 -- Data Mining
##  HW2: Decision Tree Classifiers
##
##  by Anita Slater
##
import math

def prob(y):
    """ IMPORTANT ASSUMPTION HERE:
        ** c1 = 1 ** (class 1 is 1)
        ** c2 = 0 ** (class 2 is 0)

        This helper function takes a dataset, y, of all of the
        instances of classes in a dataset and returns the number
        of items in each class as a tuple, (c1,c2). Where c1
        represents the number of instances of class 1 and c2
        represents the number of instances of class 2.
    """
    c1=0    ## Number of 1's
    c2=0    ## Number of 0's

    for item in y:
        if item == 1:
            c1+=1
        if item == 0:
            c2+=1
    return(c1,c2)

def split(D,index,value):
    """ Another helper function, takes a dataset,D, and returns
        the tuple, (Dy,Dn) of the split of D according to the
        parameters: index and value.

        ** IMPORTANT ASSUMPTION:
            split happens when instance <= value
    """
    X, y = D

    xn = [] ## List of attributes in Yes
    xy = [] ## List of attributes in No
    yn = [] ## List of classes in No
    yy = [] ## List of classes in Yes

    for i in range(0, len(X) - 1):

        if (X[i][index] <= value):
            ## 'Yes' tree
            xy.append(X[i][index])
            yy.append(y[i])
        else:
            ## 'No' tree
            xn.append(X[i][index])
            yn.append(y[i])

    Dy = (xy, yy)   ## Data set of No's
    Dn = (xn, yn)   ## Data set pf Yes's

    return (Dy,Dn)

def entrophy(D):
    """ Helper function that returns the entrophy of a given dataset, D
    """
    X,y = D

    c1,c2=prob(y) ## Getting the number of each class in the dataset

    prob_c1=c1/(c1+c2)  ## Probability of class 1
    prob_c2=c2/(c1+c2)  ## Probability of class 2

    if ( prob_c1 == 1 or prob_c2 == 1):
        ## Perfect split, no entrophy
        return 0
    else:
        return(-((prob_c1)*math.log(prob_c1,2)
           +(prob_c2*math.log(prob_c2,2))))

def IG(D, index, value):
    """
    Args:
        D: a dataset, tuple (X, y) where X is the data, y the classes
        index: the index of the attribute (column of X) to split on
        value: value of the attribute at index to split at

    Returns:
        The value of the Information Gain for the given split
    """
    X,y = D
    Dy,Dn = split(D,index,value)

    Xy,yy = Dy  ## Data set of yes's | Xy=attributes, yy=classes in yes
    Xn,yn = Dn  ## Data set of No's  | Xy=attributes, yy=classes in no

    return(entrophy(D)-((len(yy)/len(y)*entrophy(Dy))
                       +(len(yn)/len(y)*entrophy(Dn))))
def G(D, index, value):
    """
    Args:
        D: a dataset, tuple (X, y) where X is the data, y the classes
        index: the index of the attribute (column of X) to split on
        value: value of the attribute at index to split at

    Returns:
        The value of the Gini index for the given split
    """
    X,y = D
    Dy,Dn = split(D,index,value)

    Xy,yy = Dy  ## Data set of yes's | Xy=attributes, yy=classes in yes
    Xn,yn = Dn  ## Data set of No's  | Xy=attributes, yy=classes in no

    yc1,yc2 = prob(yy)  ## Number of 1's,0's in yes tree
    nc1,nc2 = prob(yn)  ## Number of 1's,0's in no  tree

    ## G(DY)
    prob_c1=yc1/(yc1+yc2)
    prob_c2=yc2/(yc1+yc2)

    Gdy=1 - ((prob_c1 ** 2) + (prob_c2 ** 2))

    ## G(DN)
    prob_c1 = nc1 / (nc1 + nc2)
    prob_c2 = nc2 / (nc1 + nc2)

    Gdn = 1 - ((prob_c1 ** 2) + (prob_c2 ** 2))

    return(((len(yy)/len(y))*Gdy)+((len(yn)/len(y))*Gdn))

def CART(D, index, value):
    """
    Args:
        D: a dataset, tuple (X, y) where X is the data, y the classes
        index: the index of the attribute (column of X) to split on
        value: value of the attribute at index to split at

    Returns:
        The value of the CART measure for the given split
    """
    X,y = D

    Dy,Dn = split(D,index,value)

    Xy,yy = Dy  ## Data set of yes's | Xy=attributes, yy=classes in yes
    Xn,yn = Dn  ## Data set of No's  | Xy=attributes, yy=classes in no

    coef = 2*(len(yy)/len(y))*(len(yn)/len(y))
    ## The coefficent in front of the sumamtion

    yc1, yc2 = prob(yy)  ## Number of 1's,0's in yes tree
    nc1, nc2 = prob(yn)  ## Number of 1's,0's in no  tree

    #yc1: The number of c1(1)s in yes tree
    #yc2: The number of c2(0)s in yes tree
    #nc1: The number of c1(1)s in no  tree
    #nc2: The number of c2(0)s in no  tree

    #yy: contains the classes for each entry in yes tree
    #yn: contains the classes for each entry in no  tree

    Pc1y = (yc1/len(yy))  # prob of c1 in yes
    Pc1n = (nc1/len(yn))  # prob of c1 in no
    Pc2y = (yc2/len(yy))  # prob of c2 in yes
    Pc2n = (nc2/len(yn))  # prob of c2 in no

    cart = coef*(abs(Pc1y-Pc1n)+abs(Pc2y-Pc2n))
    return(cart)

def bestSplit(D, criterion):
    """
    Args:
        D: A dataset, tuple (X, y) where X is the data, y the classes
        criterion: one of "IG", "GINI", "CART"

    Returns:
        A tuple (i, value) where i is the index of the attribute to split at value
    """
    #functions are first class objects in python, so let's refer to our desired criterion by a single name

    X,y = D
    indexToTest  = len(X[0]) ## Gets number of indexes (attributes) in the dataset
    valuesToTest = []        ## Will contain the rage, as a touple of values in the dataset

    best      = 0.0 ## The "best" classification result to test against
    bestIndex =0    ## Once the "best" vlaue is found, capture the index
    bestValue =0    ## "                                          " value

    if criterion == "GINI":
        ## Want to minimize GINI
        best = 1

    for i in range(0, indexToTest):
        ## Getting the minimum and maximum values for each column
        ## and saving them as tuples (min,max) in valuesToTest
        col = []
        for j in range(0, len(y)):
            col.append(X[j][i])
        valuesToTest.append((min(col),max(col)))

    for i in range(0, indexToTest):
        minval, maxval = valuesToTest[i]
        for j in range(int(minval), int(maxval)):
            if criterion == "IG":
                result = IG(D,i,j)
            elif criterion == "GINI":
                result = G(D,i,j)
            elif criterion == "CART":
                result=CART(D,i,j)
            else:
                print("ERROR:Criteria not recognized!")
                exit(-1)
            if criterion != 'GINI':
                if result > best:
                    best = result
                    bestIndex = i
                    bestValue = j
            else:
                if result < best:
                    best = result
                    bestIndex = i
                    bestValue = j

    return(best, bestIndex, bestValue)

def load(filename):
    """Loads filename as a dataset. Assumes the last column is classes, and
    observations are organized as rows.

    Args:
        filename: file to read

    Returns:
        A tuple D=(X,y), where X is a list or numpy ndarray of observation attributes
        where X[i] comes from the i-th row in filename; y is a list or ndarray of
        the classes of the observations, in the same order
    """
    X=[]
    y=[]
    with open(filename) as datafile:
        for line in datafile:
            i=0
            x=[]
            for word in line.rstrip('\n').split(','):
                if i == 10:
                    y.append(float(word))
                else:
                    try:
                        x.append(float(word))
                    except:
                        pass
                i+=1
            X.append(x)
    return(X,y)

def classifyIG(train, test):
    """Builds a single-split decision tree using the Information Gain criterion
    and dataset train, and returns a list of predicted classes for dataset test

    Args:
        train: a tuple (X, y), where X is the data, y the classes
        test: the test set, same format as train

    Returns:
        A list of predicted classes for observations in test (in order)
    """
    test_X, test_y = test  ## X and y components of test
    test_y = [int(item) for item in test_y]  ## convert list of floats to int

    col_X = []  # Will be the attribute specified by index
    pval = []  # The list of predicted values

    classifier, index, value = bestSplit(train, "IG")

    ## Want to get the desired column of specified index from the best split
    for i in range(0, len(test_y)):
        col_X.append(test_X[i][index])

    for entry in col_X:
        ## actual classifiying done here
        if (entry <= value):
            pval.append(0)
        else:
            pval.append(1)

    return (pval)

def classifyG(train, test):
    """Builds a single-split decision tree using the GINI criterion
    and dataset train, and returns a list of predicted classes for dataset test

    Args:
        train: a tuple (X, y), where X is the data, y the classes
        test: the test set, same format as train

    Returns:
        A list of predicted classes for observations in test (in order)
    """
    test_X, test_y = test  ## X and y components of test
    test_y = [int(item) for item in test_y]  ## convert list of floats to int

    col_X = []  # Will be the attribute specified by index
    pval = []  # The list of predicted values

    classifier, index, value = bestSplit(train, "GINI")

    ## Want to get the desired column of specified index from the best split
    for i in range(0, len(test_y)):
        col_X.append(test_X[i][index])

    for entry in col_X:
        ## actual classifiying done here
        if (entry <= value):
            pval.append(0)
        else:
            pval.append(1)

    return (pval)


def classifyCART(train, test):
    """Builds a single-split decision tree using the CART criterion
    and dataset train, and returns a list of predicted classes for dataset test

    Args:
        train: a tuple (X, y), where X is the data, y the classes
        test: the test set, same format as train

    Returns:
        A list of predicted classes for observations in test (in order)
    """
    test_X, test_y = test ## X and y components of test
    test_y = [int(item) for item in test_y] ## convert list of floats to int

    col_X = []  # Will be the attribute specified by index
    pval  = []  # The list of predicted values

    classifier, index, value = bestSplit(train, "CART")

    ## Want to get the desired column of specified index from the best split
    for i in range(0, len(test_y)):
        col_X.append(test_X[i][index])

    for entry in col_X:
        ## actual classifiying done here
        if (entry <= value):
            pval.append(1)
        else:
            pval.append(0)

    return (pval)

def main():
    """This portion of the program will run when run only when main() is called.
    This is good practice in python, which doesn't have a general entry point
    unlike C, Java, etc.
    This way, when you <import HW2>, no code is run - only the functions you
    explicitly call.
    """
    X, y = load("test.txt")
    y = [int(item) for item in y]
    print(classifyCART(load("train.txt"), load("test.txt")))
    print(classifyIG(load("train.txt"), load("test.txt")))
    print(classifyG(load("train.txt"), load("test.txt")))
    print(y)

if __name__=="__main__":
# 	"""__name__=="__main__" when the python script is run directly, not when it
# 	is imported. When this program is run from the command line (or an IDE), the
# 	following will happen; if you <import HW2>, nothing happens unless you call
# 	a function.
# 	"""
 	main()