#!/bin/bash

"""
This file indicates:

    * how your feature engineering should be performed on a similar dataset
    * how to apply your model on the data

The file currently corresponds to that for the basic starter ipython notebooks
adapt it to match what you want be done on the data!
"""

# ==============================================================
# Essential libraries, DO NOT REMOVE OR MODIFY
# ==============================================================

#Nathaniel Wihardjo
#Colin Ong
#Julian

import pickle

# ==============================================================
# Add here all the libraries you need, MODIFY AT WILL
# ==============================================================

def predict(kick):
    """
    Function to apply your trained model to some data of the same
    format and return the predicted output.
    """
    # ==============================================================
    # NOTE: the dataset loaded here will NOT have the column "state"
    # you do NOT need to remove it or separate it.
    #
    # Load your trained classifier DO NOT REMOVE OR MODIFY
    # ==============================================================

    with open('predictive_model.pickle', 'rb') as input_file:
        (classifier,) = pickle.load(input_file)

    # ==============================================================
    # Apply your feature engineering steps on the data in order to
    # get the data into a form expected by your trained classifier
    # MODIFY AT WILL THE FOLLOWING LINES
    # ==============================================================

    kick = kick.drop(['location','friend','photo','name','blurb','slug','currency_trailing_code','currency_symbol','creator','profile','urls','source_url'],axis=1)
    kick['goal_in_usd'] = kick['goal']*kick['static_usd_rate']
    kick = kick.drop(['goal','currency','static_usd_rate'], axis = 1)
    
    
    communication = pd.get_dumies(kick['disable_communication'])
    
    kick = kick.drop('dissable_communication',axis=1)

    countries=pd.get_dummies(kick['country'])
    for c in countires.columns:
        kick[c] = countries[c]
        
    for c in communication.columns:
        kick[c] = communication[c]
        
    kick = kick.drop(['state_changed_at','created_at','launched_at','deadline'], axis=1)
    
    
    
    numerical_columns = kick.select_dtypes(
        include=['float64', 'int64']).columns

    kick = kick[numerical_columns]

    # ==============================================================
    # Apply the classifier to the data DO NOT REMOVE OR MODIFY
    # ==============================================================

    return classifier.predict(kick)
