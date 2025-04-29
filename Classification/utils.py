


# utils.py 
# Utility functions for the project reusable functions

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay



# Function to plot a confusion matrix for classification tasks
def plot_confusion_matrix(y_true, y_pred, classes, title=None, cmap=plt.cm.Blues, size=(8, 6)):
    """
    Plot a confusion matrix using matplotlib.

    Parameters:
    y_true (list): True labels
    y_pred (list): Predicted labels
    classes (list): List of class names
    title (str): Title for the plot
    cmap: Colormap for the plot
    size (tuple): Size of the plot

    Returns:
    None
    """
    cm = confusion_matrix(y_true, y_pred, labels=classes)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=classes)
    
    # Plot the confusion matrix
    disp.plot(cmap=cmap)
    
    if title:
        plt.title(title)
    
    plt.show()