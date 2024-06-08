from sklearn.metrics import make_scorer, accuracy_score, precision_score, recall_score, f1_score

def test_model( X_test, y_test,y_predict):
    """
    Test a machine learning model and evaluate its performance.

    Args:
    randomized_search (RandomizedSearchCV): Trained model.
    X_test (DataFrame): Test features.
    y_test (Series): Test labels.

    Returns:
    DataFrame: Evaluation metrics.
    estimator: Best estimator.
    """
    # Best model
    result = {}


    print("Random Forest Evaluation (CN vs AD) - gridsearch 5 folds")
    print("------------------------------------------------------")
    print('Score (Accuracy): ')
    print(accuracy_score(y_test, y_predict))
    result['accuracy'] = accuracy_score(y_test, y_predict)
    print("------------------------------------------------------")
    print('Precision Score (tp / (tp + fp)):')
    print(precision_score(y_test, y_predict))
    result['precision_score'] = precision_score(y_test, y_predict)
    print("------------------------------------------------------")
    print('Recall Score (tp / (tp + fn)):')
    print(recall_score(y_test, y_predict))
    #result['recall_score'] = recall_score(y_test, y_predict)
    print("------------------------------------------------------")
    print('F1 Score (F1 = 2 * (precision * recall) / (precision + recall) ):')
    print(f1_score(y_test, y_predict))
    #result['f1_score'] = f1_score(y_test, y_predict)
    
    return result