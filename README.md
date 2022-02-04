[![license](https://img.shields.io/badge/license-MIT-blue.svg)](https://choosealicense.com/)

# port

Port is a personal web server that empowers individuals with their data. 

It's still very early in the development and proof-of-concept stage. The current stack includes:

    Docker
    Python
    Flask
    Postgres
    SQLAlchemy
    Marshmallow
    Flask-Dance
    pip-env
    git
    
Port is similar to a shipping port for your data.
    
| Shipping Port | Port |
| --- | --- |
| Cargo ships deliver goods to it | Web services deliver data to it |
| Goods can be stored for a long time | Data can be stored for a long time |
| It can send goods to other shipping ports | It can send data to other port users |
| It can distribute goods to local services | It can distribute data to web services |
| It enables the further processing of goods | It enables the further processing of data |
| Only the port owner knows what is in the containers | Only the data owner knows what is in the data |

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
