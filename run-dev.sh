#!/usr/bin/bash

python -m uvicorn app.asgi:application --reload
