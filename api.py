from fastapi import FastAPI

app = FastAPI()

@app.post('/get_closing_price_app')
def get_closing_price_app():
    return "Closing price"