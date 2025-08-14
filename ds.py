# streamlit_dashboard.py

import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# ---------------------
# 데이터 정의
# ---------------------
months = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']
sales_2024 = [12000000, 13500000, 11000000, 18000000, 21000000, 24000000, 22500000, 23000000, 19500000, 25000000, 26500000, 28000000]
sales_2023 = [10500000, 11200000, 12800000, 15200000, 18500000, 20100000, 19000000, 20500000, 18000000, 21500000, 23000000, 25000000]
growth_rate = [14.3, 20.5, -14.1, 18.4, 13.5, 19.4, 18.4, 12.2, 8.3, 16.3, 15.2, 12.0]
marketing_cost = [70, 80, 65, 95, 110, 150, 130, 125, 100, 140, 160, 180]

# ---------------------
# 페이지 제목
# ---------------------
st.set_page_config(page_title="2024년 월별 매출 분석 대시보드", layout="wide")
st.title("📊 2024년 월별 매출 분석 대시보드")

# ---------------------
# 주요 통계 요약
# ---------------------
col1, col2, col3, col4 = st.columns(4)
col1.metric("평균 매출액", f"{round(sum(sales_2024)/12/1_0000):,}만 원")
col2.metric("최고 매출액", f"{max(sales_2024)/1_0000:,.0f}만 원 (12월)")
col3.metric("최저 매출액", f"{min(sales_2024)/1_0000:,.0f}만 원 (3월)")
col4.metric("평균 증감률", f"{round(sum(growth_rate)/len(growth_rate), 1)} %")

st.markdown("---")

# ---------------------
# 분석 1: 증감률 (%)
# ---------------------
st.subheader("📈 분석 1: 전년 동월 대비 매출 증감률 (%)")

fig1 = go.Figure()
colors = ['crimson' if r < 0 else 'royalblue' for r in growth_rate]
fig1.add_trace(go.Bar(
    x=months,
    y=growth_rate,
    marker_color=colors,
    text=[f'{r:.1f}%' for r in growth_rate],
    textposition='auto'
))
fig1.update_layout(
    yaxis_title="증감률 (%)",
    margin=dict(l=20, r=20, t=30, b=20),
    height=400
)
st.plotly_chart(fig1, use_container_width=True)

# ---------------------
# 분석 2: 월별 매출 추이
# ---------------------
st.subheader("📉 분석 2: 2023년 vs 2024년 월별 매출 추이 비교")

fig2 = go.Figure()
fig2.add_trace(go.Scatter(x=months, y=sales_2024, mode='lines+markers', name='2024년 매출액', line=dict(color='royalblue')))
fig2.add_trace(go.Scatter(x=months, y=sales_2023, mode='lines+markers', name='2023년 매출액', line=dict(color='lightgray')))
fig2.update_layout(
    yaxis_title="매출액 (원)",
    margin=dict(l=20, r=20, t=30, b=20),
    height=400
)
st.plotly_chart(fig2, use_container_width=True)

# ---------------------
# 분석 3: 매출 vs 마케팅비용
# ---------------------
st.subheader("🔍 분석 3: 매출과 가상 마케팅 비용 심층 분석")

fig3 = go.Figure()
fig3.add_trace(go.Bar(x=months, y=[s/10000 for s in sales_2024], name="2024년 매출액 (만원)", marker_color='mediumturquoise', yaxis='y'))
fig3.add_trace(go.Scatter(x=months, y=marketing_cost, name="마케팅 비용 (가상 단위)", line=dict(color='salmon'), yaxis='y2'))

fig3.update_layout(
    yaxis=dict(title='매출액 (만원)', side='left'),
    yaxis2=dict(title='마케팅 비용', overlaying='y', side='right'),
    height=400,
    margin=dict(l=20, r=20, t=30, b=20)
)
st.plotly_chart(fig3, use_container_width=True)
