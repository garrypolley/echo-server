# echo-server

A simple python+Django echo server

Implementation for the echo server stolen from: https://arunrocks.com/django-application-in-one-file/

## Running

* `python -m venv .venv`
* `source .venv/bin/activate`
* `pip install -r requirements.txt`
* `python app.py runserver 8099`

## Usage

After running you can use this as an echo server to see what's happening for a given request.

Good for locally testing webhooks. http://localhost:8099/your-webhook-url
