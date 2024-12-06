FROM postgres:13-alpine

# Copy initialization scripts
COPY init.sql /docker-entrypoint-initdb.d/

# Set default environment variables (these will be overridden by docker-compose)
ENV POSTGRES_USER=myuser \
    POSTGRES_PASSWORD=mypassword \
    POSTGRES_DB=myapp

# Expose the PostgreSQL port
EXPOSE 5432

# Add healthcheck
HEALTHCHECK --interval=5s --timeout=5s --retries=3 \
    CMD pg_isready -U "$POSTGRES_USER" -d "$POSTGRES_DB" || exit 1
