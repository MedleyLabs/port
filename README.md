[![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://choosealicense.com/)

# port

A personal web server that empowers individuals with their data.

    Docker
    Python
    Flask
    Postgres
    SQLAlchemy
    Marshmallow
    Flask-Dance
    pip-env
    git

## Installation

### Requirements

Docker (https://www.docker.com/get-started)

### Deploy

```bash
# Clone this repository using git
cd src/web
docker-compose up --build
# Navigate to http://localhost:8000/
```

### Destroy

```bash
docker-compose down -v
```


[(Back to top)](#top)

## Acknowledgements

Huge shout out to [@ericguu](https://github.com/ericcgu) for his repo [Flask-Gunicorn-Nginx-Postgres-Docker](https://github.com/ericcgu/Flask-Gunicorn-Nginx-Postgres-Docker). It only took me 5 minutes to get a basic server up and running, and I find that it's quite easily extensible also.
