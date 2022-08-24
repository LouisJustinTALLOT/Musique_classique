#!/usr/bin/env bash

echo "Compiling Svelte app"
cd frontend && npm run build && cd ..

echo "Launching Django server"
cd backend && python manage.py runserver && cd ..