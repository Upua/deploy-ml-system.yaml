apiVersion: apps/v1
kind: Deployment
metadata:
  name: ml-system-deployment
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ml-system
  template:
    metadata:
      labels:
        app: ml-system
    spec:
      containers:
      - name: ml-system
        image: your-docker-image:latest
        ports:
        - containerPort: 80
