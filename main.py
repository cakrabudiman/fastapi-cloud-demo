from fastapi import FastAPI

app = FastAPI(title="My First Cloud API")

@app.get("/")
def read_root():
    return {
        "status": "success",
        "message": "Halo! Aplikasi ini berhasil berjalan di Cloud!",
        "environment": "Production"
    }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}