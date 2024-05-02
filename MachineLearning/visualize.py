import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree

# 1. Import the Data
music_data = pd.read_csv("music.csv")

# 2. Clean the Data
# Cleaning inicludes remov the duplicates and repeated data

x = music_data.drop(columns="Genre")
y = music_data["Genre"]

# More data we give for train, better we get result
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2) # test_size=0.2 is 20% of data allocate for the testing

# 4. Create a Model
model = DecisionTreeClassifier()

# 5. Train the Model
model.fit(x, y)
tree.export_graphviz(model, out_file='music-recommender.dot',
                     feature_names=['age', "gender"],
                     class_names=sorted(y.unique()),
                     label="all",
                     rounded=True,
                     filled=True)

# 6. Make a Prediction
# prediction1 = model.predict([[22,1]])
# print(prediction1)

# 7. Evaluate and Improve