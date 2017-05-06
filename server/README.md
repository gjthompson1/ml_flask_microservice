### Error Silence

Add to api.py

    import logging
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)

### Run Gunicorn

    gunicorn -b 0.0.0.0:5000 -w 4 api:app
