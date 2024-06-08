"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.19.6
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import load,split_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([node(func=load,
                          inputs='creditCard',
                          outputs=None),
                    node(
                        func=split_data,
                        inputs=['creditCard','params:split'],
                        outputs=[ 'X_train', 'X_test', 'y_train', 'y_test'],
                        name="split_data",
                    )])
