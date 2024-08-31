# src/evaluation.py

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def evaluate_model(classifier, X_train, Y_train, X_test, Y_test):
    Y_train_pred = classifier.predict(X_train)
    Y_test_pred = classifier.predict(X_test)

    train_accuracy = accuracy_score(Y_train, Y_train_pred)
    test_accuracy = accuracy_score(Y_test, Y_test_pred)
    cnf_matrix = confusion_matrix(Y_test, Y_test_pred)
    class_report = classification_report(Y_test, Y_test_pred)

    # Save evaluation report
    with open('reports/model_evaluation_report.txt', 'w') as f:
        f.write(f'Accuracy score of training dataset: {train_accuracy}\n')
        f.write(f'Accuracy score of test dataset: {test_accuracy}\n')
        f.write('Confusion Matrix:\n')
        f.write(str(cnf_matrix) + '\n')
        f.write('Classification Report:\n')
        f.write(class_report)
    
    return train_accuracy, test_accuracy, cnf_matrix, class_report
