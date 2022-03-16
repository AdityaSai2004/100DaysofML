# Welcome to 100DaysofML!
**References**
 - https://developers.google.com/machine-learning/crash-course/ml-intro
 - https://youtube.com/playlist?list=PLVBat3Ko2nN9z2L0izo1Reb3SmXdw7npz
 - https://www.coursera.org/learn/ai-for-everyone/
 - https://github.com/smithakolan/MachineLearningFundamentals/blob/c67148ad62146358ca545101e690033b757048dd/Machine%20Learning%20Roadmap%20for%20Absolute%20Beginners.pdf
 
**Colab file**

https://colab.research.google.com/drive/1tQtHQtNcf2hsYRR969xavsoCjZMChXZR?usp=sharing

## My Day 1 

## Day 1
**Types of Machine learning:**

 - Reinforcement learning
 - Unsupervised learning
 - Supervised learning

## Day 2
**Key terminologies:**
https://developers.google.com/machine-learning/crash-course/framing/ml-terminology

Label-output ( thing we're predicting )
Features-input

## Day 3
**Linear Regression**

    y=mx+c
    y=w1X1+w2X2+w3X3....+c

 ***Loss functions***
 
 **L2 loss:**
 Squared error
    =(observation-prediction)^2  
**Mean square error** (**MSE**)
    =sum of all the squared error/number of examples
    
***Model 1***
Salary prediction

## My Day 2

## Day 4
**Minimising lose function**

***Gradient descent***
[notes](https://developers.google.com/machine-learning/crash-course/reducing-loss/gradient-descent#expandable-1)

Iterative training : Both time and computation steps matter

Convex problems have only one minimum ( only one place where the slope is exactly 0).That minimum is where the loss function converges.

Steps:

 1. Pick starting point for w(doesn't matter though, so usually 0 or a random point)
 2. Algorithm calculates the slope of the loss curve at that point ( if more than 1 param then partial derivative)
 3. Next point of w is at the direction opposite to the gradient
 4. And the magnitude is found by multiplying the gradient magnitude with the learning rate 
 5. Learning rate shouldn't be : too small ( more computation time) or too large( might overshoot the minima)
 
 **Stochastic gradient descent (SGD)**
 Uses only 1 batch to estimate the gradient
 
 **Mini-batch stochastic gradient descent (Mini-batch SGD)**
Uses between 10 and 1,000 examples

## My Day 3

## Day 5

**Multivariable linear regression**

    y=w1X1+w2X2+w3X3....+c

## My Day 4

## Day 6

 - **Numpy** & **Pandas** revision 

