## Benchmarking

I have used [locust](https://github.com/locustio/locust) to do a load test on the model sever deployed in kubernetes

model sever configuration
```
2 containers
container config: 1 core cpu and 1GB memory
```
Locust run command
```
locust -f benchmarking.py
```

## Reports

I have done two tests with different concurrency, test report links (html viewer) are below

test 1 : 2 concurrent users

[Link to the Report1](https://htmlpreview.github.io/?https://github.com/karthik1900/model-serve/blob/main/benchmarking/reports/report_1673632000.8523982.html)

test 2 : 4 concurrent users

[Link to the Report2](https://htmlpreview.github.io/?https://github.com/karthik1900/model-serve/blob/main/benchmarking/reports/report_1673632370.2312684.html)
