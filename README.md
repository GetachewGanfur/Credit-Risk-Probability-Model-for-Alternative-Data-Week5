# Credit-Risk-Probability-Model-for-Alternative-Data-Week5


Project for credit risk probability modeling using alternative data.

## Overview

This project implements a credit risk probability model using alternative data sources. The goal is to predict the likelihood of default for loan applicants, leveraging both traditional and non-traditional data.

## Features

- Data preprocessing and feature engineering
- Model training and evaluation
- API for model inference
- Dockerized for easy deployment

## Getting Started

### Prerequisites

- Python 3.13.1
- Docker (for containerized deployment)

### Installation

1. Clone the repository:

   ```
   git clone https://github.com/GetachewGanfur/Credit-Risk-Probability-Model-for-Alternative-Data-Week5.git
   ```

2. (Optional) Create and activate a virtual environment:

   ```
   python -m venv env
   env\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

### Running the Application

#### Locally

1. Prepare data and put it in the `data/` directory.
2. Run the main application:
   ```
   python main.py
   ```

#### With Docker

1. Build and run the container:
   ```
   docker-compose up --build
   ```

### Testing

Run tests using:
