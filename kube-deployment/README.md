## Steps to deploy the server in kubernetes

1. Build Docker Image
```
cd model-serve
docker build -t model-serve:latest
```

2. Push Docker Image to a repository accessible to kubernetes

```
## You push to any repository as per your requirement
## For AWS ECR follow: https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html
```

3. Modify Image Name in manifest file `deployment.yaml`
```
##Replace image name in Line 18
image: model-serve:latest
##to
image: <your_image_uri>
```

4. Apply the manifest file `deployment.yaml`
```
kubectl apply -f deployment.yaml
```

## Deployment

`deployment.yaml` creates a [kubernetes deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) which creates pods as per the config in manifest file.

It also creates a [kubernets service](https://kubernetes.io/docs/concepts/services-networking/) which in my case is of type `LoadBalancer`.

Annotations
I have added appropriate [annotations for aws load balancer](https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.2/guide/service/annotations/)
```
  annotations:
      service.beta.kubernetes.io/aws-load-balancer-internal: "true"
      service.beta.kubernetes.io/aws-load-balancer-scheme: "internal"
      service.beta.kubernetes.io/aws-load-balancer-type: nlb
```
