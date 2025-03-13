# A Python flask form for users to fill in their contact details.
- The root URL (/) displays an HTML form for the user to fill out.
- When the form is submitted, the data is sent to the /submit URL using a POST request.
- The /submit URL processes the form data and returns a thank you message with the submitted information.
- The application runs on http://localhost:5000 with debugging enabled.
- This is a simple Flask application that demonstrates handling form submissions and displaying the submitted data.
- This application has been deployed with Docker. 
The docker image is available in the Docker Registry at:
https://hub.docker.com/repository/docker/karin86/pythonapp/general

# Useful commands

docker build -t pyflaskapplication .
docker run -itd --name python-app -p 5000:5000 pyflaskapplication 

kubectl apply -f app-deployment.yaml  

kubectl get pods --> Check that all 3 replicas are running

minikube service pyflaskapplication --url --> Verify that the deployment is running

# Debugging commands

If you encounter any issues, check the output of the following commands for further troubleshooting:

kubectl get pods
kubectl describe pod <pod-name>
kubectl logs <pod-name>