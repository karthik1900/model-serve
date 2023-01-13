from sklearn import datasets
import random
import pandas as pd
from locust import HttpUser, task


data = datasets.load_diabetes(as_frame=True)
features = data['feature_names']
df = pd.DataFrame(data['data'], columns=features)

maximums = dict(df.max())
minimums = dict(df.min())

def get_test_case():
    test_case = {}
    for feature in features:
        test_case[feature] = round(random.uniform(minimums[feature],maximums[feature]),4)
    return test_case

class Benchmarking(HttpUser): 
    
    @task 
    def model(self): 
        test_case = get_test_case()
        self.client.post(url='/model', json=test_case)