---
toc: true
layout: post
categories: [Trimester 1]
title: Deployment
---

## Deployment Process
1. Connect to EC2 instance on AWS

2. Clone directory
`git clone https://github.com/gwang1224/flask_portfolio.git`

3. Edit dockerfile
```dockerfile
FROM docker.io/python:3.9
WORKDIR /app
# --- Update environment and install python and pip ---
RUN apt-get update && apt-get upgrade -y && \
  apt-get install -y python3 python3-pip git
# --- Copy repo you updated with clone or pull ---
COPY . /app
# --- Install project specific dependencies ---
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install gunicorn
# --- Setup args to run 3 workers and run on port 8080 ---
ENV GUNICORN_CMD_ARGS="--workers=3 --bind=0.0.0.0:8080"
# --- Allow port 8080 to be accessed by system ---
EXPOSE 8080
# --- Run Web Application in production style ---
CMD [ "gunicorn", "main:app" ]`
```

4. Edit docker-compose file
```yml
version: '3'
services:
        web:
                image: flask_grace
                build: .
                ports:
                        - "8087:8080"
                volumes:
                        - persistent_volume:/app/volumes
volumes:
  persistent_volume:
    driver: local
    driver_opts:
      o: bind
      type: none
      device: /home/ubuntu/flask_portfolio/volumes
```
    3 things to change:
    * image: flask_grace
    * port (must be a different port than group in same AWS server)
    * device (must be the repo name and directory)

5. Installing and using docker
```bash
sudo apt install docker
sudo apt install docker-compose -y
sudo docker-compose up -d
```

6. To check port is running run any of these
```bash
sudo docker-compose ps
sudo docker ps
sudo docker images
sudo docker volume ls
```

7. Testing localhost endpoint
```
curl http://localhost:8087
```

![]({{ site.baseurl }}/images/curl_command.png "Output after running curl command")

8. To connect to internet with IP
```
sudo apt install nginx
cd /etc/nginx/sites-available
sudo nano test
```
Change test config file
```
server {
    listen 80;
    listen [::]:80;
    server_name 18.222.129.80;

    location / {
        proxy_pass http://localhost:8087;
        # Simple requests
        if ($request_method ~* "(GET|POST)") {
                add_header "Access-Control-Allow-Origin"  *;
        }

        # Preflight requests
        if ($request_method = OPTIONS ) {
                add_header "Access-Control-Allow-Origin"  *;
                add_header "Access-Control-Allow-Methods" "GET, POST, OPTIONS, HEAD";
                add_header "Access-Control-Allow-Headers" "Authorization, Origin, X-Requested-With, Content-Type, Accept";
                return 200;
        }
    }
}
```
Note: change server name and port

9. Test with public IP address on internet

![]({{ site.baseurl }}/images/flask_with_IP.png "My personal flask website is now currently running on a public IP address")

![]({{ site.baseurl }}/images/group_ip.png "Group flask public IP address")

