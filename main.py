from fastapi import FastAPI
from prometheus_client import Counter, generate_latest
from starlette.responses import Response

app = FastAPI()
REQUEST_COUNT = Counter("app_requests_total", "Total HTTP Requests")

@app.get("/")
def root():
    REQUEST_COUNT.inc()
    return {"message": "Hello from SRE Stack!"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type="text/plain")