
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st

st.set_page_config(layout='wide',
                  page_title='Charts'
                  )

x=pd.read_csv('Super Store Analysis Modified')
df=pd.DataFrame(x)
tab1, tab2= st.tabs(['Bi Variate Analysis','Multi Variate Analysis'])

with tab1:

    col1, col2, col3, col4=st.columns([4,4,4,4])
    
    top_years=df.groupby('Year')['Sales'].sum().astype(int).sort_values(ascending=False).round()
    fig1 = go.Figure()
    fig1.add_trace(go.Bar(
        x=top_years.index,  
        y=top_years.values,    
        marker=dict(color=px.colors.qualitative.Bold[0])  
    ))
    
    fig1.update_layout(
        title="Total Sales In Each Year",
        xaxis_title="Years",
        yaxis_title="Sales"
    )
    col1.plotly_chart(fig1)

    top_months=df.groupby('Month')['Sales'].sum().astype(int).sort_values(ascending=False).round()
    fig2 = go.Figure()
    fig2.add_trace(go.Bar(
        x=top_months.index,  
        y=top_months.values,    
        marker=dict(color=px.colors.qualitative.Bold[1])  
    ))
    
    fig2.update_layout(
        title="Total Sales In Each Month",
        xaxis_title="Months",
        yaxis_title="Sales"
    )
    col2.plotly_chart(fig2)
    
    
    top_days=df.groupby('Day')['Sales'].sum().astype(int).sort_values(ascending=False).round()
    fig3 = go.Figure()
    fig3.add_trace(go.Bar(
        x=top_days.index,  
        y=top_days.values,    
        marker=dict(color=px.colors.qualitative.Bold[2])  
    ))
    
    fig3.update_layout(
        title="Total Sales In Each Month",
        xaxis_title="Days",
        yaxis_title="Sales"
    )
    col3.plotly_chart(fig3)
    
    
    top_ship_mode=df.groupby('Day')['Sales'].sum().astype(int).sort_values(ascending=False).round()
    fig4 = go.Figure()
    fig4.add_trace(go.Bar(
        x=top_ship_mode.index,  
        y=top_ship_mode.values,    
        marker=dict(color=px.colors.qualitative.Bold[3])  
    ))
    
    fig4.update_layout(
        title="Total Sales In Each Ship Mode",
        xaxis_title="Ship Modes",
        yaxis_title="Sales"
    )
    col3.plotly_chart(fig4)
    
    top_cities=df.groupby('City')['Sales'].sum().astype(int).sort_values(ascending=False).round().head(10)
    fig5 = go.Figure()
    fig5.add_trace(go.Bar(
        x=top_cities.index,  
        y=top_cities.values,    
        marker=dict(color=px.colors.qualitative.Bold[0])  
    ))
    
    fig5.update_layout(
        title="Total Sales In Each City",
        xaxis_title="Cities",
        yaxis_title="Sales"
    )
    col1.plotly_chart(fig5)
    
    top_states=df.groupby('State')['Sales'].sum().astype(int).sort_values(ascending=False).round().head(10)
    fig6 = go.Figure()
    fig6.add_trace(go.Bar(
        x=top_states.index,  
        y=top_states.values,    
        marker=dict(color=px.colors.qualitative.Bold[1])  
    ))
    
    fig6.update_layout(
        title="Total Sales In Each State",
        xaxis_title="States",
        yaxis_title="Sales"
    )
    col2.plotly_chart(fig6)
    
    top_regions=df.groupby('Region')['Sales'].sum().astype(int).sort_values(ascending=False).round()
    fig7 = go.Figure()
    fig7.add_trace(go.Bar(
        x=top_regions.index,  
        y=top_regions.values,    
        marker=dict(color=px.colors.qualitative.Bold[2])  
    ))
    
    fig7.update_layout(
        title="Total Sales In Each Region",
        xaxis_title="Regions",
        yaxis_title="Sales"
    )
    col3.plotly_chart(fig7)
    
    fig8=px.pie(df,
               names='Category',
               color_discrete_sequence=px.colors.qualitative.Bold)
    fig8.update_layout(
        title="The Percentage Of Each Category"
    )
    col4.plotly_chart(fig8)


with tab2:
    col1, col2=st.columns([2,2])

    top_products = df.groupby(['Product Name', 'Season'])[['Sales']].sum().sort_values(ascending=False, by='Sales').reset_index().head(28)    
    fig1 = px.bar(top_products, 
                 x='Product Name', 
                 y='Sales', 
                 color='Season', 
                 title="Top 10 Products By Sales And Season",
                 color_discrete_sequence=px.colors.qualitative.Bold  
                )
    col1.plotly_chart(fig1)

    top_categories= df.groupby(['Category', 'Season'])[['Sales']].sum().sort_values(ascending=False, by='Sales').reset_index()
    fig3 = px.bar(top_categories, 
                 x='Category', 
                 y='Sales', 
                 color='Season',  
                 title="Top 10 Amount Of Model Name by Return Season",
                 color_discrete_sequence=px.colors.qualitative.Bold  
                )
    
    col2.plotly_chart(fig3)


    top_months= df.groupby(['Month Name', 'Country'])[['Sales']].sum().sort_values(ascending=False, by='Sales').reset_index()    
    fig4 = px.bar(top_months, 
                 x='Month Name', 
                 y='Sales', 
                 color='Country',  
                 title="profit in months and continent", 
                 color_discrete_sequence=px.colors.qualitative.Bold
                )
    col1.plotly_chart(fig4)

    top_months= df.groupby(['Day', 'Country'])[['Sales']].sum().sort_values(ascending=False, by='Sales').reset_index()    
    fig4 = px.bar(top_months, 
                 x='Day', 
                 y='Sales', 
                 color='Country',  
                 title="Profit In Days And Continent", 
                 color_discrete_sequence=px.colors.qualitative.Bold
                )
    col2.plotly_chart(fig4)
