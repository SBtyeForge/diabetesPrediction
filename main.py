# main.py

import logging
import os
from src.data_preprocessing import load_data, preprocess_data, split_data
from src.model_training import train_model, load_model
from src.evaluation import evaluate_model
from src.utils import print_model_summary

# Set up logging
logging.basicConfig(filename='reports/model_evaluation_report.txt', 
                    level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

def main():
    try:
        # Ensure 'reports' directory exists
        if not os.path.exists('reports'):
            os.makedirs('reports')

        logger.info("Starting the diabetes prediction pipeline")

        # Load and preprocess data
        df = load_data('data/raw/diabetes.csv')
        X, Y = preprocess_data(df)
        logger.info("Data loaded and preprocessed")

        # Split data
        X_train, X_test, Y_train, Y_test = split_data(X, Y)
        logger.info("Data split into training and testing sets")

        # Train model
        classifier = train_model(X_train, Y_train)
        logger.info("Model trained")

        # Evaluate model
        train_accuracy, test_accuracy, cnf_matrix, class_report = evaluate_model(classifier, X_train, Y_train, X_test, Y_test)
        logger.info("Model evaluated")

        # Print summary
        print_model_summary(train_accuracy, test_accuracy, cnf_matrix, class_report)
        logger.info("Model summary printed")

    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
