Mobile Price Prediction API
This project provides an API that predicts the price of a mobile phone based on various features 
such as battery power, RAM, processor speed, and more. 
The model is a RandomForestRegressor trained on a dataset of mobile phone specifications and their respective prices.

Installation
To run this API locally, follow the steps below:

1. Clone the repository:
    git clone https://github.com/Abebaw-Addis/machine_learning1.git
    cd project

2. Set up a virtual environment (optional but recommended):
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Install dependencies:
    pip install -r requirements.txt
4. Run the FastAPI application:
    uvicorn api:app --reload
The app will be available at http://127.0.0.1:8000.

API Usage
The API provides a POST endpoint /predict that predicts the mobile phone price based on the input features.

Model and Files
Model: A Random Forest Regressor is trained on the dataset of mobile phone specifications.
Scaler: The target variable price is standardized before training to improve model performance.
The model is saved in the file model.joblib, and the scaler is saved in price_scaler.joblib.


Frontend (Optional)
The project includes a simple frontend with an HTML form to input mobile phone features and display the predicted price. 
This is located in the template directory. You can access it by visiting http://127.0.0.1:8000/template/index.html.


Deployment
Once tested locally, you can deploy the FastAPI application on a cloud platform such as Render, Heroku, or AWS.

For example, on Render:

Create a new "Web Service" and connect to your GitHub repository.
Set the build command to pip install -r requirements.txt and the start command to uvicorn api:app --host 0.0.0.0 --port 80.

Model is deployed on render go and visit it https://machine-learning1-719x.onrender.com/


Future Improvements
Model Improvement: Experiment with other models (e.g., XGBoost, LightGBM) and compare performance.
Input Validation: Enhance input validation to handle edge cases and provide better error messages.
Optimization: Optimize the model and FastAPI application for production environments (e.g., using multiple workers, caching).

Conclusion
This project demonstrates how to use machine learning for price prediction using a Random Forest model. 
The FastAPI application provides a simple way to make predictions through a RESTful API.
