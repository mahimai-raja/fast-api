from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"name":"Mahimai"}

@app.get("/name/{name}")
def write_name(name: str):
    return {"name":name}
