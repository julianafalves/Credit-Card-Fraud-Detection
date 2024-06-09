from sklearn.ensemble import IsolationForest
import numpy as np

def train(X_train,y_train):
    clf = IsolationForest(
        random_state=42,
        bootstrap=True,
        contamination=0.001,
        n_estimators=500
    )

    clf.fit(X_train,y_train)
    return clf

def predict(X_test, clf):
    pred = clf.predict(X_test)
    pred_mod = np.array(list(map(lambda x: 1*(x == -1), pred)))
    print(pred_mod[0:5])


    return pred_mod