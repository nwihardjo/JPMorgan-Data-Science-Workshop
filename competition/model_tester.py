#!/bin/bash

"""
This code tests that your files work and that you can submit them.
It does not guarantee that your model will work on the test data (see 'Important Note'
in the notebook) but it reduces the likelihood that it will fail.

Run this code by writing:

    python model_tester.py

provided everything works, it will print "MODEL RAN SUCCESSFULLY" in your terminal.

DO NOT MODIFY THIS CODE
"""

import pandas as pd
import numpy as np

import predictive_model
from sklearn.metrics import accuracy_score

if __name__ == "__main__":

    kick = pd.read_csv("kick.csv", low_memory=False)
    response = kick["state"]
    del kick["state"]

    response = response.apply(lambda el: 1 if el == 'successful' else 0)

    # subsampling 10% of the training data, "pseudo test set"
    nrows = kick.shape[0]
    mask = np.random.randint(0, nrows, int(0.1*nrows))

    kick = kick.loc[mask, :]
    response = response[mask]

    predicted_response = predictive_model.predict(kick)

    print("Accuracy score (dummy test set): {0:.4f}".format(
        accuracy_score(response, predicted_response)))
    print("MODEL RAN SUCCESSFULLY")
