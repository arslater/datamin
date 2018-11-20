#######################################
##  CSI 431 -- HW 3
##
##  classifier.py
##  Anita Slater
import sys, os
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.metrics import f1_score
import matplotlib.pyplot as plt

def load(filename):
    """Loads filename as a dataset. Assumes the last column is classes, and
    observations are organized as rows.

    IMPORTANT: M = 1
               B = 0
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
                if i == 30:
                    if(word == "M"):
                        y.append(1)
                    else:
                        y.append(0)
                else:
                    try:
                        x.append(float(word))
                    except:
                        pass
                i+=1
            X.append(x)
    return(X,y)

def doSVM(dataset):
    X,y = dataset
    X_test,y_test=load("cancer-data-test.csv")
    i=0.01
    average = []

    C=[0.01, 0.1, 1, 10, 100]
    # C=[0.01,0.1,1]
    scores = []
   # f_meas = []

    for c in C:
        print("when c=",c)
        clf=svm.SVC(kernel='linear',C=c)
        clf.fit(X,y)
        i   = 0
        avg = 0

        for score in (cross_val_score(clf,X,y,cv=10,scoring='f1_macro')):
            avg += score
            i+=1
        scores.append(avg/i)

        # y_pred=clf.predict(X_test)
        # f_meas.append(f1_score(y_test,y_pred,average='weighted'))

    print(scores)
   # print("f: ", f_meas)

    plt.scatter(C,scores)
    plt.title("Configuring SVM")
    plt.xlabel("C Measures")
    plt.ylabel("F-Measure")
    plt.show()
    #print(y)
   # i *= 10
    # # Import scikit-learn dataset library
    # from sklearn import datasets
    #
    # # Load dataset
    # cancer = datasets.load_breast_cancer()
    # # Import train_test_split function
    # from sklearn.model_selection import train_test_split
    #
    # # Split dataset into training set and test set
    # X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, test_size=0.3,
    #                                                     random_state=109)  # 70% training and 30% test
    #
    # print(X_train,y_train)
    # print(X,y)
doSVM(load("cancer-data-train.csv"))
