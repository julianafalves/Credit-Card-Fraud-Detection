from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from pyod.models.cblof import CBLOF
from sklearn.cluster import KMeans

import numpy as np
import mlflow

def train(X_train, y_train, model_params, model_type):
    # Check if there's an active run
    if mlflow.active_run():
        print("Active run found. Ending the run.")
        mlflow.end_run()

    # Initialize the model based on the model_type using **model_params
    if model_type == 'IF':
        clf = IsolationForest(**model_params)
        clf.fit(X_train, y_train)

    elif model_type == 'CBLOF':
        clf = CBLOF(contamination=model_params['contamination'],
                    n_clusters=model_params['n_clusters'],
                    clustering_estimator=KMeans(n_clusters=model_params['n_clusters']))
        clf.fit(X_train)


    
    """
    # Register the model with MLflow
    with mlflow.start_run() as run:
        mlflow.log_params(model_params)  # log model parameters
        mlflow.sklearn.log_model(clf, "model")
        
        mlflow.register_model(
            "runs:/{}/model".format(run.info.run_id),
            "MyModel"
        )

    # End the run explicitly
    mlflow.end_run()

    """
    return clf

def predict(X_test, clf):
    pred = clf.predict(X_test)
    pred_mod = np.array(list(map(lambda x: 1*(x == -1), pred)))
    print(pred_mod[0:5])
    
    #mlflow.sklearn.log_model(clf, "iForest")



    return pred_mod