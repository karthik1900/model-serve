from joblib import load
async def linear_reg_model(data):
    model = load("./models/linear_reg.joblib")
    predictions = model.predict(X)
    return predictions

async def lasso_model(data):
    model = load("./models/lasso.joblib")
    predictions = model.predict(X)
    return predictions

async def dtree_model(data):
    model = load("./models/dtree.joblib")
    X = pd.DataFrame(test_case, index = [0])
    predictions = model.predict(X)
    return predictions