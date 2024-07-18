from kedro.pipeline import Pipeline, pipeline,node


from .nodes import train,predict

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
            node(
                func=train,
                inputs=["X_train", "y_train", "params:isolation_forest.params", "params:isolation_forest.name"],
                outputs="model_if",
                name="train_IF_model",
                tags=["isolation_forest"]
            ),
            node(
                func=train,
                inputs=["X_train", "y_train", "params:CBLOF.params", "params:CBLOF.name"],
                outputs="model_CBLOF",
                name="train_CBLOF_model",
                tags=["local_outlier_factor"]
            ),
            node(
                func=predict,
                inputs=['X_test','model_if'],
                outputs='y_predict_IF',
                name="predict_IF",
                    ),
            node(
                func=predict,
                inputs=['X_test','model_CBLOF'],
                outputs='y_predict_CBLOF',
                name="predict_CBLOF",
                    )])
