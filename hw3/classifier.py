#######################################
##  CSI 431 -- HW 3
##
##  classifier.py
##  Anita Slater
import sys, os
import matplotlib.pyplot as plt
from sklearn import svm
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import recall_score
from sklearn.metrics import average_precision_score
from sklearn.metrics import f1_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

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

    return scores
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

def DTree(dataset):
    X,y = dataset

    gini_scores = []
    ig_scores   = []
    avg = 0
    i   = 0

    K=[2,5,10,20]

    for k in K:
        DT_gini = DecisionTreeClassifier('gini',max_leaf_nodes=k)
        DT_ig   = DecisionTreeClassifier('entropy',max_leaf_nodes=k)

        for score in (cross_val_score(DT_gini,X,y,cv=10,scoring='f1_macro')):
            avg += score
            i+=1
        gini_scores.append(avg/i)

        for score in (cross_val_score(DT_ig,X,y,cv=10,scoring='f1_macro')):
            avg += score
            i+=1
        ig_scores.append(avg/i)

    print(gini_scores)
    print(ig_scores)

    plt.plot(K,gini_scores)
    plt.plot(K,ig_scores)
    plt.xlabel('Values of k')
    plt.ylabel('Average F Measure')
    plt.legend(['Gini Tree', 'Information Gain Tree'])
    plt.show()

    return(gini_scores,ig_scores)

# doSVM(load("cancer-data-train.csv"))
# DTree(load("cancer-data-train.csv"))

def doLDA(dataset):
    X,y = dataset
    testX,testY=load("cancer-data-test.csv")
    clf = LDA()
    clf.fit(X,y)
    avg = 0
    i = 0

    for score in (cross_val_score(clf, X, y, cv=10, scoring='f1_macro')):
        avg += score
        i += 1
    score=avg/i

    return score

def classify(dataset):
    ##
    ## 1: Training the data with the best SVM parameters (c=.1
    X,y = dataset
    testX,testY = load("cancer-data-test.csv")
    metrics = ('Avg Precision','Avg Recall','Avg F-Measure')

    classify_svm  = svm.SVC(kernel='linear',C=.1)
    classify_svm.fit(X,y)
    predict_svm   = classify_svm.predict(testX)
    precision_svm = average_precision_score(testY,predict_svm)
    confusion_svm = confusion_matrix(testY,predict_svm)
    f1_svm        = f1_score(testY,predict_svm)
    recall_svm    = recall_score(testY,predict_svm)

    metrics_svm=[precision_svm,recall_svm,f1_svm]
    print(precision_svm,recall_svm,confusion_svm,f1_svm)

    plot_svm = plt
    plot_svm.bar(metrics,metrics_svm)
    plot_svm.xlabel('Metrics')
    plot_svm.ylabel('Values')
    plot_svm.show()
classify(load("cancer-data-train.csv"))