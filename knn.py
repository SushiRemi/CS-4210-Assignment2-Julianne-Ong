#-------------------------------------------------------------------------
# AUTHOR: Julianne Ong
# FILENAME: knn.py
# SPECIFICATION: takes a binary classification problem csv file, uses LOO-CV for 1NN to test set for accuracy and error rate
# FOR: CS 4210- Assignment #2
# TIME SPENT: 10:00AM -> 10:45AM (45 minutes)
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#Importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []
totalTested = 0
totalCorrect = 0

#Reading the data in a csv file
with open('email_classification.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)

#print(db)

#Loop your data to allow each instance to be your test set
for i in range(len(db)):

    tempdb = db
    X = []
    Y = []
    testInstance = []
    

    #Add the training features to the 2D array X removing the instance that will be used for testing in this iteration.
    #For instance, X = [[1, 3], [2, 1,], ...]].
    #Convert each feature value to float to avoid warning messages

    # Y.append(row.pop(4)) #Turns training classes into numbers, adds to vectory Y.
    # X.append(row)

    #Transform the original training classes to numbers and add them to the vector Y.
    #Do not forget to remove the instance that will be used for testing in this iteration.
    #For instance, Y = [1, 2, ,...].
    #Convert each feature value to float to avoid warning messages

    #Store the test sample of this iteration in the vector testInstance
    #--> add your Python code here

    for instance in tempdb:
       instanceClass = instance[len(instance) - 1]
       if instanceClass in ("ham"):
           Y.append(float(1))
       elif instanceClass in ("spam"):
           Y.append(float(2))
           
       row = []
       for feature in range(len(instance) - 1): 
            row.append(float(instance[feature]))
       X.append(row)
          
    #print(X)
    #print(Y)
    testInstance = X.pop(i)
    testInstanceActual = Y.pop(i)
    #print(testInstance)
    #print(testInstanceActual)
       
        
    

    #Fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #Use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    classPredicted = clf.predict([testInstance])[0]

    #Compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    predicted = str(classPredicted)
    actual = str(testInstanceActual)
    #print("Predicted Classification: " + predicted + " Actual Classification: " + actual)
    totalTested += 1
    if (classPredicted == testInstanceActual):
        totalCorrect += 1


#Print the error rate
#--> add your Python code here
errorRate = 1 - (totalCorrect/totalTested)
print("Error rate: " + str(errorRate))






