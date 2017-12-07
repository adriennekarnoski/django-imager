server {
    listen 80;
    server_name ec2-52-26-163-169.us-west-2.compute.amazonaws.com; 
    access_log  /var/log/nginx/test.log;

    location / {
        proxy_pass http://127.0.0.1:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
