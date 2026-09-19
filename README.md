# CloudOps System Monitor

A Python Flask-based system monitoring application that displays basic system information and resource utilization through a web dashboard and REST API endpoints.

This project is being developed as a practical DevOps and Cloud learning project. It demonstrates application development, system monitoring, automated testing, Git/GitHub workflow, application logging, and API-based health checks.

---

## Features

- System information monitoring
- CPU usage monitoring
- Memory usage monitoring
- Disk usage monitoring
- Disk free and total space monitoring
- Application health-check endpoint
- REST API for system information
- Application logging
- Automated tests using pytest
- Simple web dashboard
- Flask-based backend
- Git/GitHub version control

---

## Technologies Used

- Python
- Flask
- psutil
- HTML
- CSS
- pytest
- Git
- GitHub

---

## Project Architecture

```text
User / Browser
      |
      v
Flask Web Application
      |
      +----------------------+
      |                      |
      v                      v
Web Dashboard           REST API
      |                      |
      +----------+-----------+
                 |
                 v
          System Information
                 |
        +--------+--------+
        |        |        |
       CPU      RAM      Disk
```

---

## Project Structure

```text
cloudops-devops-platform/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── tests/
    └── test_app.py
```

---

## Application Endpoints

### Dashboard

```text
/
```

Opens the main CloudOps System Monitor web dashboard.

The dashboard displays:

- Operating System
- Python Version
- Hostname
- CPU Usage
- Memory Usage
- Disk Usage
- Free Disk Space
- Total Disk Space

### Health Check

```text
/health
```

Returns the current application/system health status in JSON format.

Example response:

```json
{
    "status": "healthy",
    "cpu_usage": 25.4,
    "memory_usage": 48.2,
    "timestamp": "2026-09-19T20:00:00"
}
```

The application currently considers the system healthy when CPU and memory usage are below 90%.

### System Information API

```text
/api/system
```

Returns system information and resource utilization in JSON format.

Example response:

```json
{
    "operating_system": "Windows",
    "platform": "Windows-11",
    "python_version": "3.13.7",
    "hostname": "Computer",
    "cpu_usage": 20.5,
    "memory_usage": 45.3,
    "disk_usage": 52.7,
    "disk_free_gb": 220.15,
    "disk_total_gb": 476.94
}
```

---

## How the Application Works

The application uses Flask to create the web application and REST API endpoints.

The `psutil` library is used to collect system resource information such as:

- CPU utilization
- Memory utilization
- Disk utilization

Python's built-in modules are used for additional system information and application logging.

The collected information is displayed on the web dashboard and can also be accessed through JSON API endpoints.

---

## Application Logging

The application records important events in a log file named:

```text
cloudops.log
```

The logging system currently records:

- Successful system information collection
- Application errors

Example log format:

```text
2026-09-19 20:00:00 - INFO - System information collected successfully
```

Log files are excluded from Git using `.gitignore`.

---

## Automated Testing

The project uses `pytest` for automated testing.

Current tests verify:

- Home/dashboard route
- Health-check endpoint
- System information API
- Important JSON response fields

Run the tests using:

```bash
python -m pytest
```

Current test result:

```text
3 passed
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Jhagopal2002/cloudops-devops-platform.git
```

### 2. Move into the project directory

```bash
cd cloudops-devops-platform
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows CMD:

```bash
venv\Scripts\activate
```

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

Start the Flask application:

```bash
python app.py
```

The application runs on:

```text
http://127.0.0.1:5000
```

Open the URL in a web browser to access the dashboard.

---

## Testing the API

### Health Check

Open:

```text
http://127.0.0.1:5000/health
```

### System Information API

Open:

```text
http://127.0.0.1:5000/api/system
```

Both endpoints return JSON responses.

---

## Development Workflow

The project follows a simple development workflow:

```text
Develop
   |
   v
Test Locally
   |
   v
Run Pytest
   |
   v
Git Add
   |
   v
Git Commit
   |
   v
Git Push
   |
   v
GitHub Repository
```

---

## Current Project Status

### Completed

- [x] Flask application
- [x] Web dashboard
- [x] CPU monitoring
- [x] Memory monitoring
- [x] Disk monitoring
- [x] Health-check API
- [x] System information API
- [x] Application logging
- [x] Automated tests
- [x] Git repository
- [x] GitHub repository
- [x] Project documentation

---

## Future Improvements

The following features are planned as the project evolves:

- [ ] Docker containerization
- [ ] Docker Compose
- [ ] GitHub Actions CI/CD pipeline
- [ ] Linux server deployment
- [ ] AWS EC2 deployment
- [ ] Nginx reverse proxy
- [ ] Terraform Infrastructure as Code
- [ ] Improved monitoring and alerting
- [ ] Cloud deployment documentation
- [ ] Kubernetes deployment

These features will be added and documented only after they are actually implemented and tested.

---

## Learning Objectives

This project is being developed to gain practical understanding of:

- Python application development
- Flask web applications
- REST APIs
- Linux and system administration concepts
- System resource monitoring
- Application logging
- Automated testing
- Git and GitHub
- Docker and containerization
- CI/CD concepts
- AWS cloud deployment
- Infrastructure as Code
- Basic production deployment concepts

---

## Project Goal

The goal of this project is to build a practical CloudOps/DevOps learning platform that gradually moves from a local Python application to containerization, CI/CD, cloud deployment, and infrastructure automation.

The project is intentionally developed step-by-step so that each technology and implementation can be understood and explained during technical interviews.

---

## Author

**Gopal Kumar Jha**

MCA | Python | Linux | Cloud & DevOps Fundamentals

### GitHub

https://github.com/Jhagopal2002

### LinkedIn

https://www.linkedin.com/in/gopal-kumar-jha-146316281/
