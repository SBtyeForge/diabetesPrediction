# Design Document for Diabetes Prediction ML Model

## Table of Contents

1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Components](#components)
4. [Data Flow and Pipeline](#data-flow-and-pipeline)
5. [Configuration Management](#configuration-management)
6. [Error Handling and Logging](#error-handling-and-logging)
7. [Testing Strategy](#testing-strategy)
8. [Deployment](#deployment)
9. [Documentation](#documentation)
10. [Appendices](#appendices)

## Project Overview

The Diabetes Prediction ML Model project aims to develop and deploy a machine learning model that predicts the likelihood of diabetes based on patient data. The project encompasses the entire lifecycle of data handling, from loading and preprocessing to model training, evaluation, and reporting.

### Objectives
- Develop a machine learning pipeline using an SVM classifier.
- Preprocess data to ensure quality and scalability.
- Evaluate model performance using accuracy, confusion matrix, and classification reports.
- Generate and save evaluation reports for review.

## System Architecture

The system architecture is designed to be modular and maintainable, comprising several key components:

- **Data Ingestion**: Responsible for loading and preprocessing the data.
- **Model Training**: Handles training of the SVM classifier and saving the trained model.
- **Model Evaluation**: Evaluates the model's performance and generates reports.
- **Reporting**: Manages logging and reporting of model evaluation metrics.

The architecture is illustrated in the following diagram:

```plaintext
+---------------------+       +---------------------+
|    Data Ingestion   | ----> |   Model Training    |
|  (load_data,        |       |  (train_model)      |
|   preprocess_data,  |       |                     |
|   split_data)       |       +---------------------+
+---------------------+                |
                                       v
                              +---------------------+
                              |  Model Evaluation   |
                              |   (evaluate_model)  |
                              +---------------------+
                                       |
                                       v
                              +---------------------+
                              |      Reporting       |
                              |  (print_model_summary) |
                              +---------------------+
```

## Components

### 1. **`main.py`**

- **Purpose**: Entry point of the application, manages the workflow of the machine learning pipeline.
- **Responsibilities**:
  - Set up logging.
  - Load and preprocess data.
  - Train the model.
  - Evaluate and report results.

### 2. **`src/__init__.py`**

- **Purpose**: Initializes the `src` package.
- **Responsibilities**: Empty file necessary for package recognition in Python.

### 3. **`src/config.py`**

- **Purpose**: Manage configuration settings.
- **Responsibilities**:
  - Load and return configuration settings from `config.yaml`.

### 4. **`src/data_preprocessing.py`**

- **Purpose**: Handle data preprocessing tasks.
- **Responsibilities**:
  - Load data from CSV.
  - Scale features.
  - Split data into training and testing sets.

### 5. **`src/feature_engineering.py`**

- **Purpose**: Placeholder for feature engineering.
- **Responsibilities**: Currently no feature engineering implemented; future enhancements can be added here.

### 6. **`src/model_training.py`**

- **Purpose**: Model training and saving.
- **Responsibilities**:
  - Train the SVM classifier.
  - Save the trained model to a file.

### 7. **`src/evaluation.py`**

- **Purpose**: Model evaluation.
- **Responsibilities**:
  - Evaluate model performance.
  - Generate and save evaluation metrics to a file.

### 8. **`src/utils.py`**

- **Purpose**: Utility functions.
- **Responsibilities**:
  - Print model evaluation summaries.

## Data Flow and Pipeline

The data flow in the machine learning pipeline is as follows:

1. **Data Loading**: Data is loaded from `data/raw/diabetes.csv` using `load_data()`.
2. **Data Preprocessing**:
   - Features are separated from the target variable.
   - Features are scaled using `StandardScaler`.
   - Data is split into training and testing sets using `split_data()`.
3. **Model Training**:
   - An SVM classifier is trained using `train_model()`.
   - The trained model is saved to `models/model.pkl`.
4. **Model Evaluation**:
   - The model is evaluated using `evaluate_model()`.
   - Evaluation metrics are saved to `reports/model_evaluation_report.txt`.
5. **Reporting**:
   - Results are printed to the console using `print_model_summary()`.

## Configuration Management

Configuration settings are managed through `config/config.yaml`:

```yaml
data:
  test_size: 0.2
  random_state: 2

model:
  kernel: 'rbf'

logging:
  level: 'INFO'
```

## Error Handling and Logging

- **Error Handling**: Errors are caught using try-except blocks in `main.py` and logged to `reports/model_evaluation_report.txt`.
- **Logging**: Configured to record process details, including data preprocessing, model training, and evaluation.

## Testing Strategy

- **Unit Tests**: Located in `tests/test_model.py`, these tests cover model functionality and data handling.
- **Execution**: Tests are run using `pytest`.

## Deployment

1. **Environment Setup**: Use `requirements.txt` to install dependencies in a virtual environment.
2. **Execution**: Run `main.py` to execute the pipeline.
3. **Model Usage**: The trained model can be loaded and used for predictions using `load_model()` from `model_training.py`.

## Documentation

Detailed documentation and additional notes are available in `docs/documentation.md`.

## Appendices

### Dependencies

Dependencies are listed in `requirements.txt`:

```plaintext
pandas==2.0.1
numpy==1.25.0
scikit-learn==1.3.0
joblib==1.3.2
pytest==7.4.0
pyyaml==6.0
```

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
