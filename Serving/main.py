import random
from fastapi import FastAPI, Query
from entities import Input, Output
from utils import pre_process, model, post_process
app = FastAPI()

@app.post("/applications", response_model=Output)
async def create_application(id: int, application: Input):

    processed_inputs = await pre_process(Input)
    predictions = await model(processed_inputs)
    output = post_process(predictions, processed_inputs)
    
    return output
    
    
    first_name = application.first_name
    last_name = application.last_name
    proba = random.random()
    acceptance = proba > 0.5

    output = {
        "first_name": first_name,
        "last_name": last_name,
        "probability": proba,
        "acceptance": acceptance,
    }
    return output