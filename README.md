# Seniority-Role-Predict (srpredict)

A data processing microservice for doing job title seniority classifications.

Build

    docker-compose build

    docker-compose up -d

Test

    curl -I "http://localhost:8080/seniority?job_title=Director%20of%20operations"

Seniority

    curl "http://localhost:8080/seniority?job_title=Director%20of%20operations"

### Probability Option

    curl "http://localhost:8080/role?job_title=Director%20of%20operations&type=probability"

### Example Seniority ranking by title

1. Chief Executive Officer
2. Chief Operating Officer (COO), Chief Commercial Officer (CCO), etc
3. President
4. Executive Vice President
5. Senior Vice President
6. Vice President
7. Assistant Vice President
8. Associate Vice President
9. Senior Director
10. Director
11. Assistant Director
12. Manager
13. Middle Manager of people or a function
14. Employees, freelancers, contract employees, temporary employees, contingent employees. part time employees

### Seniority - Summarized

| New         | Current   |
|-------------|-----------|
| c_level     | executive |
| vp_level    | executive |
| director    | director  |
| manager     | manager   |
| non_manager | (blank)   |
| junior      | (blank)   |
