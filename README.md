# Course Assignment: A3 Web Application

## Project Structure
```
A3/
├── web/           # Web application source code
├── db/            # Database-related files
├── docker-compose.yml
├── .env           # Environment configuration
└── TROUBLESHOOTING.md
```

## Prerequisites
- Docker
- Docker Compose

## Setup and Running the Application

### Environment Configuration
1. Copy `.env.example` to `.env`
2. Modify the `.env` file with your specific configuration

### Building and Running with Docker
```bash
# Build and start the containers
docker-compose up --build

# To run in detached mode
docker-compose up -d --build
```

### Stopping the Application
```bash
docker-compose down
```

## Services
- **Web Service**: Runs on port 5000
- **Database**: PostgreSQL 13, configured with custom user and database

## Troubleshooting
For common issues, refer to the [TROUBLESHOOTING.md](TROUBLESHOOTING.md) file.


