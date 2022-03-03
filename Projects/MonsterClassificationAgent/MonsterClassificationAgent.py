# Importing pandas and numpy
import pandas as pd
import numpy as np
class MonsterClassificationAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def solve(self, samples, new_monster):
        #Add your code here!
        #
        #The first parameter to this method will be a labeled list of samples in the form of
        #a list of 2-tuples. The first item in each 2-tuple will be a dictionary representing
        #the parameters of a particular monster. The second item in each 2-tuple will be a
        #boolean indicating whether this is an example of this species or not.
        #
        #The second parameter will be a dictionary representing a newly observed monster.
        #
        #Your function should return True or False as a guess as to whether or not this new
        #monster is an instance of the same species as that represented by the list.
        monsterdf=[]
        for a in samples:
            a[0]['is_monster']=a[1]
            monsterdf.append(a[0])
        data= pd. DataFrame(monsterdf)
        m1=pd.DataFrame([new_monster])
        cols_to_encode=['size',  'color', 'covering' ,'foot-type'  ,  'lays-eggs' , 'has-wings' , 'has-gills' , 'has-tail' ]
        one_hot_data = pd.get_dummies(data, columns= cols_to_encode)
        one_hot_m1 = pd.get_dummies(m1, columns= cols_to_encode)
        # print("here basi")
        a= (one_hot_data.keys())
        c= (one_hot_m1.keys())
        new_list = list(set(a).difference(c))
        for q in new_list:
            one_hot_m1[q]=0
        d=(one_hot_m1.keys())
        features = one_hot_data.drop('is_monster', axis=1)
        targets = one_hot_data['is_monster']
        test_features = one_hot_m1.drop('is_monster', axis=1)
        features,test_features=find_mean_and_std(features,test_features)
        # print(test_features)
        weights= train (features, targets)
        prediction=  predict(test_features, weights)
        print(prediction)
        return prediction > 0.4

def find_mean_and_std(data,data2):
    # meand=[]
    # stdd=[]
    for field in ['arm-count', 'eye-count','horn-count','leg-count']:
        mean, std = data[field].mean(), data[field].std()
        # meand.append({
        # field:mean})
        # stdd.append({
        # field:mean})
        data.loc[:,field] = (data[field]-mean)/std
        data2.loc[:,field] = (data2[field]-mean)/std
    return data,data2

# Activation (sigmoid) function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_prime(x):
    return sigmoid(x) * (1-sigmoid(x))
def error_formula(y, output):
    return - y*np.log(output) - (1 - y) * np.log(1-output)

def error_term_formula(x, y, output):
    return (y-output) * output * (1 - output)

# Neural Network hyperparameters
epochs = 100
learnrate = 0.5

# Training function
def train_nn(features, targets, epochs, learnrate):
    
    # Use to same seed to make debugging easier
    np.random.seed(42)

    n_records, n_features = features.shape
    last_loss = None

    # Initialize weights
    weights = np.random.normal(scale=1 / n_features**.5, size=n_features)

    for e in range(epochs):
        del_w = np.zeros(weights.shape)
        for x, y in zip(features.values, targets):
            # Loop through all records, x is the input, y is the target

            # Activation of the output unit
            #   Notice we multiply the inputs and the weights here 
            #   rather than storing h as a separate variable 
            output = sigmoid(np.dot(x, weights))

            # The error, the target minus the network output
            error = error_formula(y, output)

            # The error term
            error_term = error_term_formula(x, y, output)

            # The gradient descent step, the error times the gradient times the inputs
            del_w += error_term * x

        # Updating the weights here by taking The learning rate times the 
        # change in weights, divided by the number of records to average
        weights += learnrate * del_w / n_records

    return weights
def train (features, targets):
    return train_nn(features, targets, epochs, learnrate)
    
def predict(to_predict,weights):
    return sigmoid(np.dot(to_predict, weights))
