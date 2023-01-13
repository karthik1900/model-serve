from joblib import load
async def linear_reg_model(data):
    model = load("../models/linear_reg.joblib")
    predictions = model.predict(data)
    return predictions

async def lasso_model(data):
    model = load("../models/lasso.joblib")
    predictions = model.predict(data)
    return predictions

async def dtree_model(data):
    model = load("../models/dtree.joblib")
    predictions = model.predict(data)
    return predictions
