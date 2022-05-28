from fastapi import FastAPI

app = FastAPI()

@app.post("/get_closing_price")
def get_closing_price():
    return "Closing price"