"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.19.6
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import scale_dataframe,split_data

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([node(func=scale_dataframe,
                          inputs='creditCard',
                          outputs='df_scaled'),
                    node(
                        func=split_data,
                        inputs=['df_scaled','params:split'],
                        outputs=[ 'X_train', 'X_test', 'y_train', 'y_test'],
                        name="split_data",
                    )])
