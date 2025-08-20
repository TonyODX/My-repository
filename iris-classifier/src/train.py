from sklearn.datasets import load_iris
import joblib
iris = load_iris()
X = iris.data
y = iris.target 
print(iris.feature_names, iris.target_names)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(random_state=42)

model.fit(X_train, y_train)

joblib.dump(model, "iris-classifier/outputs/decision_tree_model.joblib");
loaded_model = joblib.load("iris-classifier/outputs/decision_tree_model.joblib");

y_pred = model.predict(X_test)

print("Predictions:", y_pred[:5])
print("True labels:", y_test[:5])

from sklearn.neighbors import KNeighborsClassifier
model2 = KNeighborsClassifier(n_neighbors=5)
model2.fit(X_train, y_train)

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)
y_pred2 = model2.predict(X_test)
print("k-NN accuracy:", accuracy_score(y_test, y_pred2))

