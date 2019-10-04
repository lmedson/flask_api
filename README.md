# A simple crud with Flask

## Installing the dependencies

Install the dependencies with pip, running:
`$ pip install -r requeriments.txt`.

## Setup env vars
```bash
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True
```

## Run the migrations
```bash
flask db init 
flask db migrate
flask db upgrade
```

## Runinng

Make sure you have installed all the dependencies. Run with command:

`$ flask run`.

## Result

If everything goes well you will have this result in your terminal:

```
  WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### Running with docker

Create `.env` file with vars `FLASK_APP=app, FLASK_ENV=Development, export FLASK_DEBUG=True` and run docker-compose up.
