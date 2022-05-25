#!/bin/sh
echo "Waiting for PostgreSQL..."
while ! nc -z postgresql 5432; do
    sleep 0.1
done
echo "PostgreSQL Started"
CMD ["gunicorn -w 2 -b :5000 app:app"]