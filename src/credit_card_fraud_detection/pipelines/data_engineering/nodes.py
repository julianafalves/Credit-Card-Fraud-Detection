import pandas as pd
from sklearn.model_selection import train_test_split

def load(df):
    print(df.head())

def split_data(df, params: dict):
    """
    Split DataFrame into training and testing sets.

    Args:
    df (DataFrame): Input DataFrame.
    params (dict): Parameters for train-test split.

    Returns:
    tuple: X_train, X_test, y_train, y_test.
    """
    X_train, X_test, y_train, y_test = train_test_split(df.drop('Class',axis=1), df['Class'], 
                                                        test_size=params['test_size'], 
                                                        random_state=params['random_state'])
    return X_train, X_test, y_train, y_test