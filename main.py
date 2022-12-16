from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def getItems():
    return ['Item 1', 'Item 2', 'Item 3']




if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")