"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.19.6
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import load

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([node(func=load,
                          inputs='creditCard',
                          outputs=None)])
