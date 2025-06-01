for dev mode use: 
```uv run src/app.py```

for production use: 
```gunicorn -w 4 -b 0.0.0.0:4000 src.wsgi:app```

note:
1. -w 4 means 4 worker process
2. -b means bind to port

todos:
1. need to write test