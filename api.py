from fastapi import FastAPI
import joblib
import pandas as pd
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles


# Load the trained model and scaler
model = joblib.load("model.joblib")
price_scaler = joblib.load("price_scaler.joblib")  # Load the scaler used to standardize 'price'

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your frontend's origin for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Serve static files
app.mount("/template", StaticFiles(directory="template"), name="template")


class HouseData(BaseModel):
    battery_power: float
    ram: float
    int_memory: float
    mobile_wt: float
    processor_speed: float
    fc: int
    pc: int
    n_cores: int
    talk_time: int
    brand: str
    os: str
    touch_screen: int
    wifi: int
    three_g: int
    four_g: int
    dual_sim: int

@app.post("/predict")
def predict_price(data: HouseData):
    try:
        # Convert input data to DataFrame
        input_data = pd.DataFrame([data.model_dump()])

        # Make prediction (this will be in standardized form)
        standardized_prediction = model.predict(input_data)[0]

        # Convert prediction back to original scale
        actual_price = price_scaler.inverse_transform([[standardized_prediction]])[0][0]

        # Round the predicted price to remove decimals
        actual_price_rounded = round(actual_price)

        return JSONResponse(content={"predicted_price": actual_price_rounded})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    
@app.get("/")
async def read_root():
    return FileResponse("template/index.html")