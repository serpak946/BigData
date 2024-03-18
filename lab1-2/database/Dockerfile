FROM postgres:latest
VOLUME /data/db:/var/lib/postgresql/data
ENV POSTGRES_PASSWORD=secret
ENV POSTGRES_USER=postgres
ENV POSTGRES_DB=database
COPY create_fixtures.sql /docker-entrypoint-initdb.d/create_fixtures.sql
EXPOSE 5432
LABEL authors="serpak"