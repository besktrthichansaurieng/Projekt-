# -*- coding: utf-8 -*-
"""Helen

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MTaUBDBwrzJbPwOya9yWSQiHEtvdBo9O
"""
!pip install seaborn
import subprocess
subprocess.check_call(["pip", "install", "streamlit"])
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
data = {
    "Tháng": ["Tháng 1", "Tháng 2", "Tháng 3", "Tháng 4", "Tháng 5", "Tháng 6",
              "Tháng 7", "Tháng 8", "Tháng 9", "Tháng 10", "Tháng 11", "Tháng 12"],
    "Thu nhập": [1200, 1500, 1700, 1600, 1400, 1800, 1900, 2000, 2100, 1800, 1750, 1850],
    "Chi tiêu": [1000, 1100, 1300, 1200, 1150, 1250, 1400, 1500, 1350, 1400, 1500, 1450]
}
df = pd.DataFrame(data)
fig, ax = plt.subplots(figsize=(10, 6))
sns.lineplot(x="Tháng", y="Thu nhập", data=df, marker="o", label="Thu nhập", ax=ax)
sns.lineplot(x="Tháng", y="Chi tiêu", data=df, marker="o", label="Chi tiêu", ax=ax)

ax.set_title("So sánh Thu nhập và Chi tiêu hàng tháng", fontsize=16)
ax.set_ylabel("Số tiền (USD)")
ax.set_xlabel("Tháng")
ax.legend()
st.title("Biểu đồ so sánh Thu nhập và Chi tiêu")
st.pyplot(fig)
