"""
This is a boilerplate pipeline 'data_evaluation'
generated using Kedro 0.19.5
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import test_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
        func= test_model,
        inputs = ['X_test','y_test','y_predict'],
        outputs = 'metrics')
    ])
