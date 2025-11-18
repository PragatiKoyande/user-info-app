# user-info-app

Install minikube  to serve as a K8S cluster
https://github.com/amolshete/Minikube-Installation

Create some python code that accepts the following parameters:
First name
Last name
Street Address
City
State
refer app.py

Create a docker container
Has an entrypoint that is the python code from #2 above
Using python 3
Build the docker container locally
Push the docker container to a registry

Build Docker Image
docker build -t user-info-appv1:latest .
docker run --rm pragati/jupyter-job:1.0 \
  --first_name Pragati --last_name Koyande \
  --street "123 MG Road" --city Pune --state Maharashtra
Expected output:

Full Name: Pragati Koyande
Address: 123 MG Road, Pune, Maharashtra

docker login
Push:

docker push pragatikoyande/user-info-appv1:latest

Create a Kubernetes job to execute the container in #5
Create some configmaps to serve as parameters to the K8S job in #6
The Key values in the configmaps should equal to the command line options in #2
Create a secret to attach to the K8S job
Run the K8S job
Collect the K8S log to verify the output
Creae manisfest files 
Check status:
kubectl get jobs
kubectl get pods

Get logs:
kubectl logs <pod-name>

Expected output:

Full Name: Pragati Koyande
Address: 123 MG Road, Pune, Maharashtra

what if we change the value of configmaps ?
Example
You originally had:
data:
  CITY: Pune
Then you edit it:
data:
  CITY: Mumbai
and apply:

kubectl apply -f configmap.yaml
Kubernetes accepts the change, but existing Pods or Jobs do not automatically see it.

Why?

When a Pod starts, it reads the ConfigMap values at creation time and injects them as environment variables (or mounts them as files).

These values are snapshotted into the Pod spec — they do not dynamically update unless:

The Pod is restarted, or

The application is watching the mounted ConfigMap file and re-reads it (some apps do, but Python scripts like ours do not).

Demonstration
Change value:

kubectl edit configmap user-config
Change:
CITY: Mumbai

Re-run Job:
kubectl delete job user-info-job
kubectl apply -f job.yaml

Check logs:
kubectl get pods
kubectl logs <new-pod-name>

Now output shows:
Full Name: Pragati Koyande
Address: 123 MG Road, Mumbai, Maharashtra
