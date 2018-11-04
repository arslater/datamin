import math

def prob(y):
    """Returns a tuple (c1,c2
    of the instances with a 1 and 0 respectively
    of a certain calss occuring
    """
    c1=0
    c2=0

    for item in y:
        if item == 1:
            c1+=1
        if item == 0:
            c2+=1
    return(c1,c2)
def split(D,index,value):
    """Returns Dy and Dn, tuples of the split"""
    X, y = D

    xn = []
    xy = []
    yn = []
    yy = []

    ny = 0
    nn = 0

   # print("Splitting at column:", index, " when value <", value)
    for i in range(0, len(X) - 1):
       # print(X[i][index],"??",value)
        if (X[i][index] <= value):
            xy.append(X[i][index])
            yy.append(y[i])
        else:
           # print("DING")
            xn.append(X[i][index])
            yn.append(y[i])

    Dy = (xy, yy)
    Dn = (xn, yn)

    return (Dy,Dn)
def entrophy(D):

    X,y = D

    c1,c2=prob(y)

    prob_c1=c1/(c1+c2)
    prob_c2=c2/(c1+c2)

    return(-(prob_c1)*math.log(prob_c1,2)
           +(prob_c2*math.log(prob_c2,2)))


def IG(D, index, value):
    """Compute the Information Gain of a split on attribute index at value
    for dataset D.

    Args:
        D: a dataset, tuple (X, y) where X is the data, y the classes
        index: the index of the attribute (column of X) to split on
        value: value of the attribute at index to split at

    Returns:
        The value of the Information Gain for the given split
    """
    Dy,Dn = split(D,index,value)

    Xy,yy = Dy  ## Data set of yes's
    Xn,yn = Dn  ## Data set of No's

    # nn=0
    # ny=0
    #
    # for item in yy:
    #     if item == 1:
    #         ny += 1
    # for item in yn:
    #     if item == 0:
    #         nn +=1
    #print(nn,len(yn),ny,len(yy))
    return(entrophy(D)-((len(yy)/len(y)*entrophy(Dy))
                       +(len(yn)/len(y)*entrophy(Dn))))
def G(D, index, value):
    """Compute the Gini index of a split on attribute index at value
    for dataset D.

    Args:
        D: a dataset, tuple (X, y) where X is the data, y the classes
        index: the index of the attribute (column of X) to split on
        value: value of the attribute at index to split at

    Returns:
        The value of the Gini index for the given split
    """
    Dy,Dn = split(D,index,value)

    Xy,yy=Dy
    Xn,yn=Dn

    print(Dn)

    yc1,yc2 = prob(yy)
    nc1,nc2 = prob(yn)

    ## G(DY)
    prob_c1=yc1/(yc1+yc2)
    prob_c2=yc2/(yc1+yc2)

    Gdy=1 - ((prob_c1 ** 2) + (prob_c2 ** 2))

    ## G(DN)
    prob_c1 = nc1 / (nc1 + nc2)
    prob_c2 = nc2 / (nc1 + nc2)

    Gdn = 1 - ((prob_c1 ** 2) + (prob_c2 ** 2))

   # print("Prob of ys",(len(yy)/len(y)))
   # print("Prob of ns",(len(yn)/len(y)))

    return(((len(yy)/len(y))*Gdy)+((len(yn)/len(y))*Gdn))

def CART(D, index, value):
    """Compute the CART measure of a split on attribute index at value
    for dataset D.

    Args:
        D: a dataset, tuple (X, y) where X is the data, y the classes
        index: the index of the attribute (column of X) to split on
        value: value of the attribute at index to split at

    Returns:
        The value of the CART measure for the given split
    """
    X,y = D

    Dy,Dn = split(D,index,value)

    Xy,yy = Dy
    Xn,yn = Dn

    coef = 2*(len(yy)/len(y))*(len(yn)/len(y))

    yc1,yc2 = prob(yy)
    ## Gets the number of c1's and c2's in the yes split

    nc1,nc2 = prob(yn)
    ## Gets the number of c1s and c2s in class no

    #yc1: The number of c1s in split yes
    #yc2: The number of c2s in split yes
    #nc1: The number of c1s in split no
    #nc2: The number of c2s in split no

    #yy: contains the calsses for each entry in split yes
    #yn: contains the classes for each entry in split no

    print(yy)
    print("NUMBER OF 1s IN YEZ",yc1,len(yy))

    Pc1y = (yc1/len(yy))  # prob of c1 in yes
    Pc1n = (nc1/len(yn))  # prob of c1 in no
    Pc2y = (yc2/len(yy))  # prob of c2 in yes
    Pc2n = (nc2/len(yn))  # prob of c2 in no

    cart = coef*(abs(Pc1y-Pc1n)+abs(Pc2y-Pc2n))
    print(cart)

def bestSplit(D, criterion):
    """Computes the best split for dataset D using the specified criterion

    Args:
        D: A dataset, tuple (X, y) where X is the data, y the classes
        criterion: one of "IG", "GINI", "CART"

    Returns:
        A tuple (i, value) where i is the index of the attribute to split at value
    """

    #functions are first class objects in python, so let's refer to our desired criterion by a single name

    X,y = D
    indexToTest = len(X[0])

    cols = []
    valuesToTest = []

    for i in range(0, indexToTest):
        col = []
        for j in range(0, len(y)):
            col.append(X[j][i])
        cols.append(col)
        valuesToTest.append((min(col),max(col)))
    print(valuesToTest)

    if criterion == "IG":
        print("IG")


    elif criterion == "GINI":
        print("GINI")
    elif criterion == "CART":
        print("CART")
    else:
        print("Option not recognized!")
        exit(-1)

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
                #print(word)
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

X,y=load("train.txt")
#IG((X,y),1,28)
#G((X,y),0,0)
#print(y)
#CART((X,y),0,0)
print(bestSplit((X,y),"IG"))
#print(entrophy(load("train.txt")))
def classifyIG(train, test):
    """Builds a single-split decision tree using the Information Gain criterion
    and dataset train, and returns a list of predicted classes for dataset test

    Args:
        train: a tuple (X, y), where X is the data, y the classes
        test: the test set, same format as train

    Returns:
        A list of predicted classes for observations in test (in order)
    """


def classifyG(train, test):
    """Builds a single-split decision tree using the GINI criterion
    and dataset train, and returns a list of predicted classes for dataset test

    Args:
        train: a tuple (X, y), where X is the data, y the classes
        test: the test set, same format as train

    Returns:
        A list of predicted classes for observations in test (in order)
    """


def classifyCART(train, test):
    """Builds a single-split decision tree using the CART criterion
    and dataset train, and returns a list of predicted classes for dataset test

    Args:
        train: a tuple (X, y), where X is the data, y the classes
        test: the test set, same format as train

    Returns:
        A list of predicted classes for observations in test (in order)
    """



def main():
    """This portion of the program will run when run only when main() is called.
    This is good practice in python, which doesn't have a general entry point
    unlike C, Java, etc.
    This way, when you <import HW2>, no code is run - only the functions you
    explicitly call.
    """


# if __name__=="__main__":
# 	"""__name__=="__main__" when the python script is run directly, not when it
# 	is imported. When this program is run from the command line (or an IDE), the
# 	following will happen; if you <import HW2>, nothing happens unless you call
# 	a function.
# 	"""
# 	main()
