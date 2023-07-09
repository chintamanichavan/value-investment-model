import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib

# Load and preprocess the dataset
df = pd.read_csv('your_dataset.csv')  # Replace 'your_dataset.csv' with the actual filename/path of your dataset
# Perform any necessary preprocessing steps

# Split the dataset into features and target variable
X = df.drop('target_variable', axis=1)  # Replace 'target_variable' with the name of your target variable column
y = df['target_variable']

# Perform train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the machine learning model
model = LinearRegression()  # Replace with the desired machine learning algorithm
model.fit(X_train, y_train)

# Save the trained model to a file
joblib.dump(model, 'model.pkl')  # Replace 'model.pkl' with the desired filename/path to save the trained model
