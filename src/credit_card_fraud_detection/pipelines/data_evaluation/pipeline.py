from kedro.pipeline import Pipeline, pipeline, node
from .nodes import test_model,copy_temp_to_final

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=test_model,
            inputs=["params:isolation_forest.name","y_test","y_predict_IF", "df_metrics"],
            outputs="temp_df_metrics",
            name="evaluation_model_IF",
            tags=["evaluation"]),
        node(
            func=copy_temp_to_final,
            inputs=["temp_df_metrics"],
            outputs="df_metrics",
            name="copy_temp_df_to_final",
            tags=["evaluation"])
    ])
