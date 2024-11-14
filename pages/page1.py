import streamlit as st
import pandas as pd
import joblib

st.title("IRIS品種預測")

#載入模型
knn = joblib.load("model/KNN.joblib")
lr = joblib.load("model/LR.joblib")
rf = joblib.load("model/RF.joblib")
svm = joblib.load("model/svm.joblib")

#佈置元件(側邊欄)
m = st.sidebar.selectbox("### 請選擇模型:",("KNN","LogisticRegression","RandomForest","SVM"))
if m == "KNN":
    model = knn
elif m == "LogisticRegression":
    model = lr
elif m == "RandomForest":
    model = rf
elif m == "SVM":
    model = svm

#佈置元件(main):接收資料
df = pd.read_csv("iris.csv")
se1 = st.slider("### 花萼長度(cm):", 
                float(df['sepal.length'].min()),
                float(df['sepal.length'].max()),
                float(df['sepal.length'].mean()))
se2 = st.slider("### 花萼寬度(cm):", 
                float(df['sepal.width'].min()),
                float(df['sepal.width'].max()),
                float(df['sepal.width'].mean()))
se3 = st.slider("### 花瓣長度(cm):", 
                float(df['petal.length'].min()),
                float(df['petal.length'].max()),
                float(df['petal.length'].mean()))
se4 = st.slider("### 花瓣寬度(cm):", 
                float(df['petal.width'].min()),
                float(df['petal.width'].max()),
                float(df['petal.width'].mean()))

st.image("iris.png")

#進行預測
labels = ["Setosa","Versicolor","Virginica"]
if st.button("進行預測"):
    X = [[se1,se2,se3,se4]]
    y = model.predict(X)
    st.write(y)
    st.write("### 預測結果:", labels[y[0]])

