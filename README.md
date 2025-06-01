for dev mode use: 
```uv run src/app.py```

for production use: 
```gunicorn -w 4 -b 0.0.0.0:4000 src.wsgi:app```

note:
1. -w 4 means 4 worker process
2. -b means bind to port

todos:
1. post body validation with pydantic
2. make it async (sync IO can be bottleneck)
3. think deeper about error handling
4. write some tests
5. write some benchmarks