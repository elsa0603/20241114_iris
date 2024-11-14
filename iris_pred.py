import streamlit as st

ps = st.navigation(
    [
        st.Page("pages/page1.py", title="IRIS品種預測",icon="🌹"),#path, title, 圖示
        st.Page("pages/page2.py", title="IRIS樣本分佈",icon="🔅")
    ]
)

ps.run()