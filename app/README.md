## Serve Application

I have used fastapi to serve model as an api. This application accepts only one feature vector in a request.

Run the application
`uvicorn app.main:app`


I am using 3 different models in one application. Model is being chosen at random in runtime.

API Request
```
{
    "age": float
    "sex": float
    "bmi": float
    "bp": float
    "s1": float
    "s2": float
    "s3": float
    "s4": float
    "s5": float
    "s6": float 
}
```
** All the variables are in type `float` as per the dataset

API Response
```
{
    "progression": float
    "model": str
}
```

## Extensions

This code can be extended in following ways

### Fetching features
`processing.py` module can be used to fetch features in real-time
```
async def pre_process(inputs):

    ## Add calls to databases to fetch other features in realtime
    ## since the function is async, it will handle a delay as well
    
    processed_inputs = pd.DataFrame(inputs, index = [0])
    return processed_inputs
```

### Choosing model
We can add intelligent way of choosing a model based on the input features
```
## main.py
async def serve(input: Input):
   ..
   model = random.choice((linear_reg_model,lasso_model,dtree_model))
   ## this choice can also be decided intelligently depending on the use case
   ..
   ..
```

### Analysing/Monitoring models
Since the API response also sends the model used, upstream consumers can use data to analyse model performance & compare in real-time.

