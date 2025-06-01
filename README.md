for dev mode use: 
```uv run src/app.py```

for production use: 
``` gunicorn -w 4 -b 0.0.0.0:4000 src.wsgi:app```

note:
-w 4 means 4 worker process
-b means bind to port

todos:
- need to write test