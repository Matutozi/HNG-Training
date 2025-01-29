# Basic Information API

## Project Description

This FastAPI application serves basic information in JSON format including the registered email address, the current datetime in ISO 8601 format, and the GitHub URL of the project's codebase. Designed for backend interns as a demonstration of API development and deployment.

## Setup Instructions

**Prerequisites:**

- Python 3.6+
- pip

**Installation:**

1. Clone the repository:
   https://github.com/Matutozi/HNG-week1

2. Install dependencies:
   ```
   python3 -m venv venv
   source venv/bin/activate
   pip insall -r requirements
   ```

## API Documentation

**Endpoint URL:**
GET `/`

**Request/Response Format:**

- **Request**: No parameters required.
- **Response**: JSON
  ```json
  {
    "email": "your-email@example.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/yourusername/your-repo"
  }
  ```

### Example Usage: Using CURL:

```
curl -X GET "http://127.0.0.1:8000"

```

### Deployment
The API is deployed at 