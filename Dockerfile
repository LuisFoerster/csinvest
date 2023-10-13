# Use the official PostgreSQL image as a base
FROM postgres:latest

# Install the `pg_trgm` extension
RUN echo "CREATE EXTENSION IF NOT EXISTS pg_trgm;" >> /docker-entrypoint-initdb.d/init.sql