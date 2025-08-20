import kfp
from kfp import dsl

## components of pipeline
def data_processing_op():
    return dsl.ContainerOp(  
        name="Data Processing",  
        image="sanjayn96/colorectal-cancer:latest",   
        command = ["python", "src/data_processing.py"]
    )   

def model_training_op():
    return dsl.ContainerOp(   
        name="model training", 
        image="sanjayn96/colorectal-cancer:latest",   
        command = ["python", "src/model_training.py"]  
    ) 

## pipeline
@dsl.pipeline(
    name='mlops-pipeline',
    description="This is a kubeflow pipeline"
)
def mlops_pipeline():
    data_processing = data_processing_op()
    model_training = model_training_op()


if __name__=="__main__":
    kfp.compiler.Compiler().compile(mlops_pipeline, "mlops_pipeline.yaml")