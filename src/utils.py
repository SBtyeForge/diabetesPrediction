# src/utils.py

def print_model_summary(train_accuracy, test_accuracy, cnf_matrix, class_report):
    print(f'Accuracy score of training dataset: {train_accuracy}')
    print(f'Accuracy score of test dataset: {test_accuracy}')
    print('Confusion Matrix:')
    print(cnf_matrix)
    print('Classification Report:')
    print(class_report)
