import pandas as pd
async def pre_process(inputs):
    processed_inputs = pd.DataFrame(inputs, index = [0])
    return processed_inputs

def post_process(predictions, model_name):
    return {"progression" : predictions[0], "model": model_name}