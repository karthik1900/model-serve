import random
from fastapi import FastAPI
from entities import Input, Output
from processing import pre_process, post_process
from models import linear_reg_model, lasso_model, dtree_model
app = FastAPI()

@app.post("/model", response_model=Output)
async def serve(input: Input):
    model = random.choice((linear_reg_model,lasso_model,dtree_model))
    processed_inputs = await pre_process(input)
    predictions = await model(processed_inputs)
    output = post_process(predictions, model.__name__)
    
    return output