import numpy as np
import pandas as pd
import streamlit as st

# 文字輸出
'''
st.title("Demo")
st.header("123")
st.text("123")
st.write("123")
st.write("## 123")

a = np.array([10,20,30,40])
st.write(a)

df = pd.DataFrame({"name":["JOE", "ALEX", "JANE"], "age":[19,20,21]})
st.write(df)
st.table(df)
st.info("123")
'''
# 核取方塊
st.write("核取方塊")
cb = st.checkbox("是否外帶")
if cb:
    st.info("外帶")
else:
    st.info("內用")

# 選項按鈕
st.write("選項按鈕")
rb = st.radio("性別:", ["男","女","不知"])
st.info(rb)

# 下拉選單
st.write("下拉選單")
se = st.selectbox("選擇飲料:",["奶茶","咖啡","不用"])
st.info(se)

se2 = st.selectbox("選擇飲料:",["奶茶","咖啡","不用"], key="se2")
st.info(se2)

# 按鈕
st.write("按鈕")
def check():
    st.text("12312313")

btn = st.button("OK")
if btn:
    st.info("OK")
    check()

# 滑桿
st.write("滑桿")
num = st.slider("選擇數量:", 2, 20, step=2)
st.info(num)

# 側邊欄
st.sidebar.write("側邊欄")
se3 = st.sidebar.selectbox("選擇飲料:",["奶茶","咖啡","不用"], key="se3")
st.sidebar.info(se3)

#分欄
cols = st.columns(4)
with cols[0]:
    n0 = st.number_input("...", key="n0")
with cols[1]:
    n1 = st.number_input("...", key="n1")
with cols[2]:
    n2 = st.number_input("...", key="n2")
with cols[3]:
    n3 = st.number_input("...", key="n3")

sum = n0+n1+n2+n3
st.write(n0, n1, n2, n3)
st.info(sum)