# Author: Ayanle Aideed 
# Date: 04/05/2025 
# Description: This code implements a simple Perceptron algorithm for binary classification of bank notes. 
# The Perceptron is a type of linear classifier that makes its predictions based on a linear predictor function combining a set of weights with the feature vector.



# import the necessary libraries
import csv 
import random 

from sklearn.svm import SVC
from sklearn.linear_model import Perceptron 
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier


# initialize the model perceptron
# model = Perceptron()
model = SVC()


# load the dataset 
with open("data/banknotes.csv", "r") as file: 
    reader = csv.reader(file)
    next(reader)  # skip the header row

    data = []

    # read the data from the CSV file
    for row in reader:
        data.append({
            "evidence" : [float(cell) for cell in row[:4]], 
            "label": "Authentic" if row[4] == "0" else "Counterfeit"

        })


# Separete the data into training and testing sets 
holdout = int(0.5 * len(data))  # 50% for testing (not 20 80 split as standerd)
random.shuffle(data)  # shuffle the data randomly
testing = data[:holdout]  # first half for testing
training = data[holdout:]  # second half for training

# Train the model on trainging set 
X_training = [row["evidence"] for row in training]  # features
Y_training = [row["label"] for row in training]  # labels
model.fit(X_training, Y_training)  # fit the model to the training data

# Make the predictions on the testing set
X_testing = [row["evidence"] for row in testing]  # features
Y_testing = [row["label"] for row in testing]  # labels
predictions = model.predict(X_testing)  # make predictions



# Compute how well we peformed 
correct = 0 
incorrect = 0 
total = 0 
# loop through the predictions and compare them to the actual labels
for actual, predicted in zip(Y_testing, predictions):
    total += 1
    if actual == predicted:
        correct += 1
    else:
        incorrect += 1




print(f"Result for model {model.__class__.__name__}:")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"accuracy: {correct / total * 100:.2f}%")



# plot the confusion matrix
from utils import plot_confusion_matrix


plot_confusion_matrix(Y_testing, predictions, classes=["Authentic", "Counterfeit"], title="Confusion Matrix for Perceptron Model", size=(8, 6))
