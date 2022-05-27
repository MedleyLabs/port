FROM python:3.7.0-slim
LABEL maintainer "Eric Yates <eric@medleyagency.com>"
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y \
    && apt-get -y install apt-utils gunicorn libpq-dev python3-dev gcc \
    && apt-get autoremove -y \
    && apt-get clean all
ENV INSTALL_PATH /usr/app/static
RUN mkdir -p $INSTALL_PATH
WORKDIR $INSTALL_PATH
COPY requirements.txt .
RUN pip install --upgrade pip -r requirements.txt
RUN pip install -e ../port
COPY . .

CMD ["/web/entrypoint.sh"]