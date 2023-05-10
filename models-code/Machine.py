"""""
import json
import joblib
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder 
from sklearn.preprocessing import MinMaxScaler
from pandas_profiling import ProfileReport
import seaborn as sns
from scipy.stats import beta
from scipy.stats import f


EarlyDiagnosis_df = pd.read_csv('diabetes_data.csv')


EarlyDiagnosis_df.head()




#encoding to transform gender from male & female to 1 & 0
label_encoder = LabelEncoder() 
EarlyDiagnosis_df['gender'] = label_encoder.fit_transform(EarlyDiagnosis_df['gender'])


EarlyDiagnosis_df.head(10)


# Choosing the features and the label
# Here, we separate between the last column that has the output we want the model to predict it and the rest of the data
# so X has all the columns except for Class and Y has nothing but the class column values
X = EarlyDiagnosis_df.iloc[:, :-1]
y = EarlyDiagnosis_df.iloc[:, -1]

print(X.shape)
print(X.iloc[:5, :])
print('\n')
print(y.shape)
print(y[:4])





# train and test split
# x_train 70% training set
# x_test 30% testing set
# y_train prediction output after training the model
# y_test the real values which will be compared to y_train to calculate the accuracy of the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=17)
X_train1, X_test1, y_train1, y_test1 = train_test_split(X, y, test_size=0.3, random_state=17)
print(X_train.shape)
print(y_train.shape)
print('\n')
print(X_test.shape)
print(y_test.shape)




# Scaling
# We use the fit_transform() method to get the mean and variance of the features in our training set, then we 
# use the transform() method to scale all the features using the mean and variance from the fit_transform() method
encoder = MinMaxScaler()
X_train = encoder.fit_transform(X_train)
X_test = encoder.transform(X_test)

pd.DataFrame(X_train, columns = X.columns)




Model_Score = []
# Random Forest Classifier


# Results
Model_Score = pd.DataFrame(Model_Score, columns=['Model', 'Train Score Average', 'Train Score SD', 'Test Score'])
Model_Score = Model_Score.sort_values(by=['Test Score'], ascending=True)
Model_Score




def find_best_n_estimators(X, y, n_estimators_range):
    
    Finds the best number of estimators for RandomForestClassifier using cross-validation.

    Args:
    - X: The input features.
    - y: The target variable.
    - n_estimators_range: A list or range of values representing the number of estimators to test.

    Returns:
    - best_n_estimators: The number of estimators that yields the highest mean cross-validated score.
    - results: A dictionary containing the cross-validated scores for each value of n_estimators.
    

    results = {}
    best_score = -np.inf
    best_n_estimators = None

    for n_estimators in n_estimators_range:
        clf = RandomForestClassifier(n_estimators=n_estimators)
        scores = cross_val_score(clf, X, y, cv=5)  # Perform 5-fold cross-validation
        mean_score = np.mean(scores)

        results[n_estimators] = mean_score

        if mean_score > best_score:
            best_score = mean_score
            best_n_estimators = n_estimators

    return best_n_estimators, results

    # Assuming you have your input features `X` and target variable `y` ready
n_estimators_range = [10, 50, 100, 200, 300]  # Specify the range of values to test

best_n_estimators, results = find_best_n_estimators(X, y, n_estimators_range)

print("Best number of estimators:", best_n_estimators)
print("Cross-validated scores for each number of estimators:")
for n_estimators, score in results.items():
    print("n_estimators =", n_estimators, ", Mean CV Score =", score)




classifier_rf = RandomForestClassifier(n_estimators=13, random_state=0)
classifier_rf.fit(X_train, y_train)
rf_test_score = classifier_rf.score(X_test, y_test)
rf_test_score = classifier_rf.score(X_test, y_test)
classifier_rf.predict([[0, 1, 0, 0, 0, 0 ,0 ,0 ,0, 0 ,0 ,0 ,0 ,0 ,0 ,0]])
rf_test_score


joblib.dump(classifier_rf, "./random_forest.joblib", compress=True)
joblib.dump(train_mode, "./train_mode.joblib", compress=True)
joblib.dump(encoder, "./encoders.joblib", compress=True)
label_encoder
joblib.dump(label_encoder, "./label_encoder.joblib", compress=True)

from sklearn.tree import export_graphviz
import graphviz

dot_data = export_graphviz(tree12, out_file=None, feature_names=X_train.columns, filled=True, rounded=True, special_characters=True, impurity=False)

graph = graphviz.Source(dot_data)
graph.format = 'png'
graph.view()
# View or save the simplified graph
graph.render("iris_decision_tree")
graph.view()
# or
graph.render("decision_tree.pdf")
"""