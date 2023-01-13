import random
from fastapi import FastAPI
from app.entities import Input, Output
from app.processing import pre_process, post_process
from app.models import linear_reg_model, lasso_model, dtree_model
app = FastAPI()

@app.post("/model", response_model=Output)
async def serve(input: Input):
    input = input.dict()
    model = random.choice((linear_reg_model,lasso_model,dtree_model))
    processed_inputs = await pre_process(input)
    predictions = await model(processed_inputs)
    output = post_process(predictions, model._name_)
    
    return output
