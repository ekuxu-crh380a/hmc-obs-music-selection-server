#!/usr/bin/bash

python -m gunicorn app.asgi:application -k uvicorn.workers.UvicornWorker
