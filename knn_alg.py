class KNN:
    def __init__(self , k, problem: int=0, metric: int=0):
        self.k = k
        self.problem = problem
        self.metric = metric

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        import numpy as np
        from scipy import stats

        m = self.X_train.shape[0]
        n = X_test.shape[0]
        y_pred = []

        for i in range(n):
            distance = []
            for j in range(m):
                if self.metric == 0:
                    d = (np.sqrt(np.sum(np.square(X_test[i, :] - self.X_train[j, :]))))
                else:
                    d = np.absolute(X_test[i, :] - self.X_train[j, :])
                distance.append((d, self.y_train[j]))
            distance = sorted(distance)

            neighbors = []
            for item in range(self.k):
                neighbors.append(distance[item][1])

            if self.problem == 0:
                y_pred.append(np.mean(neighbors))
            else:
                y_pred.append(np.mean(neighbors))
        return y_pred


import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


iris = load_iris()
data = iris.data
target = iris.target

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size = 0.2)
X_train.shape, y_train.shape, X_test.shape, y_test.shape

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

train_error = []
test_error = []

for k in range(1, 31):
    knn= KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)

    y_pred1= knn.predict(X_train_scaled)
    train_error.append(np.mean(y_train!=y_pred1))

    y_pred2= knn.predict(X_test_scaled)
    test_error.append(np.mean(y_test!=y_pred2))

plt.figure(figsize=(10, 5))
plt.plot(range(1, 15), train_error, color='b', label="Train")
plt.plot(range(1, 15), test_error, color='r', label="Test")
plt.xlabel('Number of nearest neighbors (k)', fontsize=14)
plt.ylabel('Error', fontsize=14)
plt.title('Finding optimal value of K using error curves', fontsize=18, pad=15)
plt.legend()
plt.show()

knn = KNeighborsClassifier(n_neighbors=14)

knn.fit(X_train_scaled, y_train)

y_pred = knn.predict(X_test_scaled)

print("Accuracy: ", 100*np.round(accuracy_score(y_test, y_pred), 5), "%")

confusionmatrix = confusion_matrix(y_test, y_pred)
fig, ax = plt.subplots()
sns.heatmap(confusionmatrix, annot=True, linewidth=3, cmap='viridis')
plt.xlabel("Confusion Matrix", fontsize=18, labelpad=20)
ax.xaxis.tick_top()
plt.ylabel("True", fontsize=14, rotation=0, labelpad=30)
plt.yticks(rotation=0)
plt.title("Predicted", fontsize=14, pad=10)
plt.show()


bknn = KNN(k=14, problem=1, metric=0)
# model fitting
bknn.fit(X_train_scaled, y_train)
# predicting
b_y_pred = bknn.predict(X_test_scaled)

confusionmatrix = confusion_matrix(y_test, b_y_pred)

fig, ax = plt.subplots()
sns.heatmap(confusionmatrix, annot=True, linewidth=3, cmap='inferno')
plt.xlabel("Confusion Matrix", fontsize=18, labelpad=20)
ax.xaxis.tick_top()
plt.ylabel("True", fontsize=14, rotation=0, labelpad=30)
plt.yticks(rotation=0)
plt.title("Predicted", fontsize=14, pad=10)
plt.show()

