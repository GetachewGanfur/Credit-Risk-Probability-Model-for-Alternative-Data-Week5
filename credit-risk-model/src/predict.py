# predict.py
# Script for inference

import pandas as pd
import numpy as np
import os
import joblib
import logging 
import mlflow
import mlflow.pyfunc
from src.data_processing import load_data, main # Import FeatureEngineer and load_data from data_processing
# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define paths for saved components
MODEL_PATH = '../models/best_model.pkl'
RFM_CLUSTERER_PATH = 'models/rfm_clusterer.pkl'
COLUMN_TRANSFORMER_PATH = 'models/column_transformer.pkl'
MLFLOW_MODEL_NAME = "CreditRiskProxyModel" # Name of the registered model in MLflow

def load_model(model_path=MODEL_PATH):
    
    if os.path.exists(model_path):
        try:
            model = joblib.load(model_path)
            logging.info(f"Model loaded successfully from local path: {model_path}")
            return model
        except Exception as e:
            logging.warning(f"Could not load model from local path ({model_path}): {e}. Attempting to load from MLflow registry.")


def preprocess_new_data(raw_data_df):
    
    try:
        logging.info("Starting preprocessing of new raw data...")
        # Step 1: Apply FeatureEngineer (stateless)
        customer_level_df = main(raw_data_df)
        logging.info(f"After FeatureEngineer, shape: {customer_level_df.shape}")

        cols_to_remove = ["CustomerId", "Unnamed: 0", "is_high_risk"]
        cust_id = customer_level_df['CustomerId']
        for cols in cols_to_remove:
            if cols in data.columns:
                data = data.drop(cols, axis=1)

        
        return customer_level_df, cust_id

    except Exception as e:
        logging.error(f"Error during data preprocessing: {e}")
        return None, None

def predict_risk(data_to_predict, customer_id):
    # Load model and preprocessor components
    model = load_model()
    dataset, customer_id = preprocess_new_data(data_to_predict)
    try:
        # Make predictions (probabilities for the positive class '1')
        risk_probabilities = model.predict_proba(dataset)[:, 1]
        # Predict the binary label (0 or 1)
        predicted_high_risk = model.predict(dataset)

        # Create a results DataFrame
        results_df = pd.DataFrame({
            'CustomerId': customer_id,
            'risk_probability': risk_probabilities,
            'predicted_high_risk': predicted_high_risk
        })
        logging.info("Prediction completed successfully.")
        return results_df

    except Exception as e:
        logging.error(f"Error during model prediction: {e}")
        return None