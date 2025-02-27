#-------------------------------------------------------------------------
# AUTHOR: Julianne Ong
# FILENAME: decision_tree_1.py
# SPECIFICATION: Creates decision trees based on three different training sets, tests with a new set and checks accuracy of each.
# FOR: CS 4210- Assignment #2
# TIME SPENT: 8:15AM -> 10:00AM (1 hour 45 Minutes)
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#Importing some Python libraries
from sklearn import tree
import csv

dataSets = ['contact_lens_training_1.csv', 'contact_lens_training_2.csv', 'contact_lens_training_3.csv']
testSet = 'contact_lens_test.csv'

for ds in dataSets:

    dbTraining = []
    X = []
    Y = []
    accuracyList = []

    #Reading the training data in a csv file
    with open(ds, 'r') as csvfile:
         reader = csv.reader(csvfile)
         for i, row in enumerate(reader):
             if i > 0: #skipping the header
                dbTraining.append (row)

    #Transform the original categorical training features to numbers and add to the 4D array X.
    #For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
    #--> add your Python code here
    for i in dbTraining: #access each instance
        row = []
        for j in i: #access the feature values
            if j in ("Young", "Myope", "Yes", "Normal"):
                row.append(1)
            elif j in ("Presbyopic", "Hypermetrope", "No", "Reduced"):
                row.append(2)
            elif j == "Prepresbyopic":
                row.append(3)
        Y.append(row.pop(4)) #Turns training classes into numbers, adds to vectory Y.
        X.append(row)


    #Transform the original categorical training classes to numbers and add to the vector Y.
    #For instance Yes = 1 and No = 2, Y = [1, 1, 2, 2, ...]
    #--> add your Python code here
    #Already handled above with line 43 -----> Y.append(row.pop(4)) 

    #Loop your training and test tasks 10 times here
    for i in range (10):
        #Implemented a leave one out training method for variance
        partitionSize = len(X)/10
        endIndexA = int(i*partitionSize)
        endIndexB = int((i+1)*partitionSize)
        Xsubset = []
        Ysubset = []
        for i in range(0, endIndexA):
            Xsubset.append(X[i])
            Ysubset.append(Y[i])

        for i in range(endIndexB, len(X)):
            Xsubset.append(X[i])
            Ysubset.append(Y[i])

        #Fitting the decision tree to the data setting max_depth=3
        clf = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth=5)
        clf = clf.fit(Xsubset, Ysubset)

        #Read the test data and add this data to dbTest
        #--> add your Python code here
        dbTest = []
        with open(testSet, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for i, row in enumerate(reader):
                if i > 0: #skipping the header
                    dbTest.append (row)


        #Transform the features of the test instances to numbers following the same strategy done during training,
        #and then use the decision tree to make the class prediction. For instance: class_predicted = clf.predict([[3, 1, 2, 1]])[0]
        #where [0] is used to get an integer as the predicted class label so that you can compare it with the true label
        #--> add your Python code here

        # Converting features to numbers
        testX = []
        testYactual = []
        for i in dbTest: #access each instance
            row = []
            for j in i: #access the feature values
                if j in ("Young", "Myope", "Yes", "Normal"):
                    row.append(1)
                elif j in ("Presbyopic", "Hypermetrope", "No", "Reduced"):
                    row.append(2)
                elif j == "Prepresbyopic":
                    row.append(3)
            testYactual.append(row.pop(4)) #Turns training classes into numbers, adds to vectory Y.
            testX.append(row)

        testYpredicted = []
        # Testing instances, finding predictions
        for instance in testX:
            #print(instance)
            class_predicted = clf.predict([instance])[0]
            #print(class_predicted)
            testYpredicted.append(class_predicted)

        # print(testYpredicted)
        # print(testYactual)

        #Compare the prediction with the true label (located at data[4] -> now testYActual) of the test instance to start calculating the accuracy.
        #--> add your Python code here
        total = len(testYactual)
        correct = 0
        for i in range(total):
            if (testYactual[i] == testYpredicted[i]):
                correct += 1
        # print(correct)
        # print(total)
        accuracy = correct/total
        accuracyList.append(accuracy)
        # print(accuracy)


    

    #Find the average of this model during the 10 runs (training and test set)
    #--> add your Python code here
    avgAccuracy = 0
    for i in accuracyList:
        avgAccuracy += i
    avgAccuracy /= len(accuracyList)

    #Print the average accuracy of this model during the 10 runs (training and test set).
    #Your output should be something like that: final accuracy when training on contact_lens_training_1.csv: 0.2
    #--> add your Python code here
    fileTested = str(ds)

    print("Final accuracy when training on " + fileTested + ": " + str(avgAccuracy))



