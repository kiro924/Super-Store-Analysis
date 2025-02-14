
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide',
                  page_title='Sales Overview'
                   )

x=pd.read_csv('Super Store Analysis Modified')
df=pd.DataFrame(x)

st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
        font-size: 60px;  # Adjust the size as needed
        color: green;
        font-weight: bold;
    }
    </style>
    <h1 class="centered-title">Store Overview Sales</h1>
    """, unsafe_allow_html=True
)

col1, col2, col3, col4, col5, col6=st.columns(6)

col1.metric(label='Total Sales', value=f"{int(df['Sales'].sum()):,}")

col2.metric(label='Total Customers', value=f"{df['Customer Name'].nunique()}")

col3.metric(label='New York City', value=f"{252463:,}")

col4.metric(label='November', value=f"{350162:,}")

col5.metric(label='2018', value=f"{722052:,}")

col6.metric(label='Saturday', value=f"{420905:,}")

col1, col2, col3=st.columns([4,4,4])

top_cities=df.groupby('City')['Sales'].sum().astype(int).sort_values(ascending=False).head(10).round()
fig1=go.Figure()
fig1.add_trace(go.Bar(x=top_cities.index,
                      y=top_cities.values,
                      marker=dict(color=px.colors.qualitative.Bold[1])
                     ))

fig1.update_layout(
title="Top 10 Cities by Sales",
xaxis_title="City",
yaxis_title="Sales")
col1.plotly_chart(fig1)

top_years=df.groupby('Year')['Sales'].sum().astype(int).sort_values(ascending=False).round()
fig2=go.Figure()
fig2.add_trace(go.Bar(x=top_years.index,
                      y=top_years.values,
                      marker=dict(color=px.colors.qualitative.Bold[1])
                     ))

fig2.update_layout(
title="Total Sales In Each Year",
xaxis_title="Years",
yaxis_title="Sales")
col2.plotly_chart(fig2)

top_days=df.groupby('Day')['Sales'].sum().astype(int).sort_values(ascending=False).round()
fig3 = go.Figure()
fig3.add_trace(go.Scatter(
    x=top_days.index,  
    y=top_days.values,  
    mode='lines',  
    line=dict(color=px.colors.qualitative.Bold[1])  
))

fig3.update_layout(
    title="Total Sales In Each Day",
    xaxis_title="Days",
    yaxis_title="Sales"
)

col3.plotly_chart(fig3)
