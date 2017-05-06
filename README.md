# Flask Micro Service for Machine Learning

A data processing microservice for doing seniority form job title.

Build

    docker-compose build

    docker-compose up -d

Test

    curl -I "http://localhost:8080/seniority?job_title=Director%20of%20operations"

Seniority

    curl "http://localhost:8080/seniority?job_title=Director%20of%20operations"

### Probability Option

    curl "http://localhost:8080/role?job_title=Director%20of%20operations&type=probability"
