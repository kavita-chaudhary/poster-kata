FROM postgres:latest
ENV POSTGRES_PASSWORD=password321
ENV POSTGRES_USER=starship
ENV POSTGRES_DB=database
COPY initial_script.sql /docker-entrypoint-initdb.d/initial_script.sql