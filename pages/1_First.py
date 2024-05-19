import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time
import random

# 초기화
st.title("Real-time Random Number Graph")
placeholder = st.empty()

# 데이터 초기화
x = list(range(100))  # 0부터 99까지의 초기 x 값
y1 = [0] * 100        # 첫 번째 y 값 (파란 선)
y2 = [0] * 100        # 두 번째 y 값 (빨간 선)

# 그래프 업데이트 루프
while True:
    # 난수 생성
    new_value1 = random.uniform(-1, 1)
    new_value2 = random.uniform(-1, 1)
    y1.append(new_value1)
    y2.append(new_value2)
    y1.pop(0)  # y1 값의 길이를 100으로 유지
    y2.pop(0)  # y2 값의 길이를 100으로 유지

    # 그래프 그리기
    plt.figure(figsize=(10, 5))
    plt.plot(x, y1, label='Value 1', color='blue')
    plt.plot(x, y2, label='Value 2', color='red')
    plt.ylim(-1, 1)
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.title("Real-time Number Graph")
    plt.legend(loc='upper right')

    # Streamlit에 그래프 업데이트
    placeholder.pyplot(plt)
    plt.close()

    # 1초 대기
    time.sleep(0.05)
