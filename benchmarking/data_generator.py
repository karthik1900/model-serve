from sklearn import datasets
import random

data = datasets.load_diabetes(as_frame=True)
features = data['feature_names']
df = pd.DataFrame(data['data'], columns=features)

maximums = dict(df.max())
minimums = dict(df.min())

test_case = {}
for feature in features:
  test_case[feature] = round(random.uniform(minimums[feature],maximums[feature]),4)