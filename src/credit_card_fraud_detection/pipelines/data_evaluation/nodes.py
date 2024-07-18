import pandas as pd
import mlflow
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def get_new_run_id(metrics_df, model_name):
    """
    Generate a new run ID for the given model name.

    Args:
    metrics_df (DataFrame): DataFrame containing existing metrics.
    model_name (str): Name of the model.

    Returns:
    str: New run ID.
    """
    if metrics_df.empty or model_name not in metrics_df['model_name'].values:
        return f"{model_name}_1"
    else:
        last_run_id = metrics_df[metrics_df['model_name'] == model_name]['run_id'].max()
        last_run_num = int(last_run_id.split('_')[-1])
        return f"{model_name}_{last_run_num + 1}"

def test_model(model_name, y_test, y_predict, metrics_df):
    """
    Test a machine learning model and evaluate its performance.

    Args:
    model_name (str): Name of the model.
    X_test (DataFrame): Test features.
    y_test (Series): Test labels.
    y_predict (Series): Predicted labels.
    metrics_df (DataFrame): DataFrame to store metrics.

    Returns:
    DataFrame: Updated metrics DataFrame.
    """
    run_id = get_new_run_id(metrics_df, model_name)
    
    accuracy = accuracy_score(y_test, y_predict)
    precision = precision_score(y_test, y_predict)
    recall = recall_score(y_test, y_predict)
    f1 = f1_score(y_test, y_predict)
    ''' 
    # Log metrics to MLflow
    with mlflow.start_run(run_name=run_id, nested=True):
        mlflow.log_param("model_name", model_name)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.log_metric("precision_score", precision)
        mlflow.log_metric("recall_score", recall)
        mlflow.log_metric("f1_score", f1)'''

    # Update the metrics DataFrame
    new_metrics = {
        'model_name': model_name,
        'run_id': run_id,
        'accuracy': accuracy,
        'precision_score': precision,
        'recall_score': recall,
        'f1_score': f1
    }
    metrics_df = metrics_df.append(new_metrics, ignore_index=True)

    return metrics_df

def copy_temp_to_final(temp_dataset):
    """
    Copy the temporary dataset to the final CSV file.

    Args:
    temp_dataset (DataFrame): The temporary DataFrame containing metrics.
    final_dataset_path (str): The path to the final CSV file.

    Returns:
    None
    """
    return temp_dataset