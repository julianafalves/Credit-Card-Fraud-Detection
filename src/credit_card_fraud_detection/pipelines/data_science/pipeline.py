from kedro.pipeline import Pipeline, pipeline,node


from .nodes import train,predict

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([node(func=train,
                          inputs=[ 'X_train', 'y_train'],
                          outputs='model'),
                    node(
                        func=predict,
                        inputs=['X_test','model'],
                        outputs='prediction',
                        name="predict",
                    )])
