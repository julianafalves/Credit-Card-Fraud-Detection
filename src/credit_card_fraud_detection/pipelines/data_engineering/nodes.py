import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

def scale_dataframe(df):
    scaler = MinMaxScaler()
    X = df.drop('Class',axis=1)
    scaled_array = scaler.fit_transform(X)
    scaled_X = pd.DataFrame(scaled_array, columns=X.columns)
    print(scaled_X.head())
    return pd.concat([scaled_X,df['Class']],axis=1)

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