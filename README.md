# Diabetes Prediction ML Model

## Overview

This project develops a machine learning model to predict diabetes using a Support Vector Machine (SVM) classifier. It includes data preprocessing, model training, evaluation, and reporting. Results of the model evaluation are saved to a report, and model predictions are assessed through unit tests.

## Folder Structure

```plaintext
diabetes_prediction/
│
├── data/
│   └── raw/
│       └── diabetes.csv           # Raw data file
│
├── reports/
│   ├── model_evaluation_report.txt # Model evaluation results
│
├── src/
│   ├── __init__.py                 # Initialize src module
│   ├── config.py                   # Configuration loading
│   ├── data_preprocessing.py        # Data loading and preprocessing
│   ├── feature_engineering.py       # Placeholder for feature engineering
│   ├── model_training.py            # Model training and saving
│   ├── evaluation.py                # Model evaluation
│   └── utils.py                     # Utility functions
│
├── configs/
│   └── config.yaml                 # Configuration settings
│
├── models/
│   └── model.pkl                    # Saved model
│
├── docs/
│   └── documentation.md             # Project documentation
│
├── notebooks/
│   └── exploratory_analysis.ipynb   # Jupyter notebook for exploratory data analysis
│
├── tests/
│   └── test_model.py                # Unit tests for the model
│
├── main.py                          # Main script to run the pipeline
├── requirements.txt                 # Python dependencies
└── README.md                        # Project documentation
```

## Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-repository/diabetes_prediction.git
   cd diabetes_prediction
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Main Script**

   To execute the entire pipeline including data preprocessing, model training, and evaluation:

   ```bash
   python main.py
   ```

2. **Run Tests**

   To run unit tests and generate the test results report:

   ```bash
   pytest
   ```

## Configuration

Configuration settings are located in the `configs/` directory:

- **`config.yaml`**: Contains parameters for data processing and model training:

    ```yaml
    data:
      test_size: 0.2
      random_state: 2

    model:
      kernel: 'rbf'

    logging:
      level: 'INFO'
    ```

## Reports

- **Model Evaluation Report**: `reports/model_evaluation_report.txt` - Contains accuracy scores, confusion matrix, and classification report for the model.

## Documentation

Additional project documentation can be found in `docs/documentation.md`.

## Notebooks

Jupyter notebooks for exploratory data analysis and other experiments are available in the `notebooks/` directory:

- `notebooks/exploratory_analysis.ipynb` - Notebook for exploratory data analysis.

## Models

Saved model files are located in the `models/` directory:

- `models/model.pkl` - The trained SVM model saved using `joblib`.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Dependencies

Required Python packages are listed in `requirements.txt`:

```plaintext
pandas==2.0.1
numpy==1.25.0
scikit-learn==1.3.0
joblib==1.3.2
pytest==7.4.0
pyyaml==6.0
```
