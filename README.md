# Modern Web Application with Docker

A containerized web application built with Flask and PostgreSQL, demonstrating modern DevOps practices and clean architecture.

## Technology Stack
- **Backend**: Python Flask
- **Database**: PostgreSQL 13
- **Containerization**: Docker & Docker Compose
- **Architecture**: Microservices-based approach

## Features
- Containerized application deployment
- PostgreSQL database integration
- Environment-based configuration
- Production-ready Docker setup

## Project Structure
```
.
├── web/           # Web application source code
├── db/            # Database configuration and migrations
├── docker-compose.yml
└── .env           # Environment configuration
```

## Getting Started

### Prerequisites
- Docker
- Docker Compose

### Quick Start
1. Clone the repository:
```bash
git clone https://github.com/rayen003/Web_app.git
cd Web_app
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configurations
```

3. Build and run the application:
```bash
docker-compose up --build
```

The application will be available at `http://localhost:5000`

### Development Mode
For development with debug mode:
```bash
docker-compose up -d --build
```

### Stopping the Application
```bash
docker-compose down
```

## Architecture
- **Web Service**: Flask application running on port 5000
- **Database**: PostgreSQL 13 with custom configuration
- **Docker**: Multi-container orchestration

## Contributing
Feel free to submit issues and enhancement requests!
