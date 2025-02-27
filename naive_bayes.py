#-------------------------------------------------------------------------
# AUTHOR: Julianne Ong
# FILENAME: naive_bayes.py
# SPECIFICATION: reads training and weather binary csv problem files, uses naive bayes algorithm to predict and show confidence levels
# FOR: CS 4210- Assignment #2
# TIME SPENT: 11:00AM -> 11:45AM (45 minutes) 
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#Importing some Python libraries
from sklearn.naive_bayes import GaussianNB
import csv

#Reading the training data in a csv file
#--> add your Python code here
db = []
X = []
Y = []
header = []

with open('weather_training.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i == 0:
         header = row
      elif i > 0: #skipping the header
         db.append (row)

#Transform the original training features to numbers and add them to the 4D array X.
#For instance Sunny = 1, Overcast = 2, Rain = 3, X = [[3, 1, 1, 2], [1, 3, 2, 2], ...]]

#Transform the original training classes to numbers and add them to the vector Y.
#For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]

#--> add your Python code here
for instance in db:
   row = []
   for feature in instance:
      if feature in ("Sunny", "Mild", "Normal", "Weak"):
         row.append(1)
      elif feature in ("Overcast", "Cool", "High", "Strong"):
         row.append(2)
      elif feature in ("Rain", "Hot"):
         row.append(3)
      elif feature in ("Yes"):
         Y.append(1)
      elif feature in ("No"):
         Y.append(2)
   X.append(row)

#Fitting the naive bayes to the data
clf = GaussianNB(var_smoothing=1e-9)
clf.fit(X, Y)

#Reading the test data in a csv file
#--> add your Python code here
testdb = []
testX = []
testY = []

with open('weather_test.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         testdb.append (row)

for instance in testdb:
   row = []
   for feature in instance:
      if feature in ("Sunny", "Mild", "Normal", "Weak"):
         row.append(1)
      elif feature in ("Overcast", "Cool", "High", "Strong"):
         row.append(2)
      elif feature in ("Rain", "Hot"):
         row.append(3)
   testX.append(row)



#Printing the header of the solution
#--> add your Python code here
printHeader = ""
for word in header:
   printHeader += word
   printHeader += "\t"
printHeader += "Confidence"
print(printHeader)

#Use your test samples to make probabilistic predictions. For instance: clf.predict_proba([[3, 1, 2, 1]])[0]
#--> add your Python code here
for instance in range(len(testX)):
   probability = clf.predict_proba([testX[instance]])[0]
   #print(probability)
   if(probability[0] >= 0.75): #Valid "Yes" class
      output = ""
      for feature in range(0, (len(testdb[instance]) - 1 )):
         output += testdb[instance][feature]
         output += "\t"
         if(feature == 2 or feature == 3):
            output += "\t"
      output += "Yes\t\t" 
      output += str(probability[0])
      print(output)
   elif(probability[1] >= 0.75): #Valid "No" class
      output = ""
      for feature in range(0, (len(testdb[instance]) - 1 )):
         output += testdb[instance][feature]
         output += "\t"
         if(feature == 2 or feature == 3):
            output += "\t"
      output += "No\t\t" 
      output += str(probability[1])
      print(output)
      

