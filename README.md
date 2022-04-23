# kNN-Implementation

**The Dataset**
The dataset for this assignment is the Pima Indian Diabetes dataset.
It contains 768 instances described by 8 numeric attributes. 
There are two classes - yes and no. Each entry in the dataset corresponds to a patient’s record; the attributes are personal characteristics 
and test measurements; the class shows if the person shows signs of diabetes or not. 
The patients are from Pima Indian heritage, hence the name of the dataset. 
A copy of the dataset can be downloaded from Canvas. There are 2 files associated with the dataset. 
The first file, pima-indians-diabetes.names, describes the data, including the number and the type of the attributes and classes, 
as well as their meaning. This file can be opened in any text editor and its purpose is to give you information about the dataset. 
Make sure you read the whole file to learn more about the meaning of the attributes and the classes. The second file, 
pima-indians-diabetes.data, contains the data itself. Your task is to predict the class, where the class can be yes or no.

Note: The original dataset can be sourced from UCI Machine Learning Repository. 
However, you need to use the dataset available on Canvas as it has been modified for consistency.

The functions will accept two filenames, given as strings. 
The first contains a dataset to be used to train the classifier; the second contains a dataset without class values for testing. 
The classifier functions must return their classifications for each example in the testing file.

**Training data file**
The input training file will consist of several rows of data, each with n attributes plus a single class value (yes or no). The file will not have a header row, will have one example per line, and each line will consist of a normalised value for each of the non-class attributes separated by commas, followed by a class value. This example has 8 attributes, like pima.csv:

0.084,0.192,0.569,0.274,0.105,0.179,0.090,0.284,yes
0.091,0.287,0.255,0.234,0.191,0.175,0.174,0.000,no
0.000,0.929,0.681,0.106,0.238,0.348,0.003,0.000,no
0.193,0.455,0.379,0.284,0.187,0.355,0.058,0.096,yes
0.489,0.774,0.578,0.218,0.122,0.829,0.104,0.000,no
0.378,0.839,0.489,0.118,0.173,0.885,0.045,0.691,yes
Testing data file
The input testing data file will consist of several new examples to test your data on. 
The file will not have a header row, will have one example per line, 
and each line will consist of a normalised value for each of the non-class attributes separated by commas. 

An example input file could look as follows:

0.588,0.628,0.574,0.263,0.136,0.463,0.054,0.333
0.243,0.274,0.224,0.894,0.113,0.168,0.735,0.321
0.738,0.295,0.924,0.113,0.693,0.666,0.486,0.525

Note: your functions should be able to handle any number of attributes; 
not just the 8 attributes from pima.csv. You can assume that if the input 
training file has n attributes + a class column, then the testing file will 
also have n attributes. You'll need this versatility later.

Output
Your functions will return a list. 
Each element of the list, in order, corresponds to one of the examples in the given testing data file. 
The elements of the list should be strings - "yes" or "no" - representing the classification your function 
chose for the corresponding line in the testing data file. An example return value could be as follows:

["yes", "no", "yes"]
