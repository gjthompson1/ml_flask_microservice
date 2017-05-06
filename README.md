# Flask Micro Service for Machine Learning

A data processing microservice for doing seniority form job title.

Build

    docker-compose build

    docker-compose up -d

Test nginx is working:

    curl -I "http://localhost:8080/seniority?job_title=Director%20of%20operations"

Should get response of the form

    HTTP/1.1 200 OK
    Server: gunicorn/19.4.5
    Date: Thu, 04 May 2017 04:03:15 GMT
    Connection: close
    Content-Type: application/json
    Content-Length: 11

### Seniority

    curl "http://localhost:8080/seniority?job_title=Director%20of%20operations"

### Probability Option

    curl "http://localhost:8080/seniority?job_title=Director%20of%20operations&type=probability"
