DeployFlask Microservice to Minikube with Prometheus and Grafana Monitoring

This project demonstrates a Flask microservice application that is deployed on Minikube and monitored using Prometheus and Grafana.

Prerequisites:
* Docker
* Minikube
* Helm

Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/MelekBadreddine/prometheus-grafana.git
2. Start Minikube:
   ```bash
   minikube start
3. Build and Push the Docker Image:
   ```bash
   docker build -t your-docker-registry/flask-app:latest .
   docker push your-docker-registry/flask-app:latest
4. Deploy the Flask Application:
   ```bash
   kubectl apply -f kubernetes/deployment.yaml
   kubectl apply -f kubernetes/service.yaml
5. Install Prometheus and Grafana using Helm:
   ```bash
   helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
   helm repo add grafana https://grafana.github.io/helm-charts
   helm repo update
   helm install prometheus prometheus-community/prometheus
   helm install grafana grafana/grafana
6. Expose Services:
   ```bash
   kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-ext
   kubectl expose service grafana-server --type=NodePort --target-port=3000 --name=grafana-ext
7. Access the UI:
   ```bash
   minikube service prometheus-server-ext
   minikube service grafana-ext
8. Get Default Password for Grafana:
   ```bash
   kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
9. Customize Monitoring:
   * In the Grafana UI, add Prometheus as a data source.
   * Create custom dashboards or use pre-built dashboards to monitor your Flask application.
   * Configure alerts and notifications in Prometheus and Grafana.

  ![Alt Text](https://github.com/MelekBadreddine/prometheus-grafana/assets/grafana.png)



    

   

