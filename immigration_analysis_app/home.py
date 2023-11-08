import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np


st.set_page_config(
    layout= "wide",
    page_title= "Immigration Analysis App",
    page_icon= "🧊",
)


years = list(range(1980,2014))
cols_to_drop = ['Type', 'Coverage', 'AREA','DEV','REG']
rename_dict = {'OdName':'Country',
                'AreaName':'Continent',
                'RegName':'Region',
                'DevName':'Status'}
def load_data(path):
    df = pd.read_excel('Canada.xlsx', sheet_name=1, skiprows=20, skipfooter=2)
    df.drop(columns=cols_to_drop, inplace=True)
    df.rename(columns=rename_dict, inplace=True)
    df['Total'] = df[years].sum(axis=1)
    df.set_index('Country', inplace=True)
    return df



with st.spinner('Processing Immigration Data ....'):
   df = load_data('Canada.xlsx')

st.image("https://prominentoverseas.com/wp-content/uploads/2019/03/Canada-Immigration-2019.jpg",use_column_width= True)
st.title("Immigration Analysis App")  



total_countries = df.shape[0]
duration = "1980-2013"
total_immigrations = df['Total'].sum()


c1,c2,c3,c4,c5 ,c6= st.columns(6)


c1.metric("Total Countries",total_countries)
c2.metric("Years",duration)
c3.metric("Total Immigration", total_immigrations )

st.subheader("Immigration Visyalization")
fig = px.line(df,x = df.index , y = 'Total', height = 500)
st.plotly_chart(fig,use_container_width= True)

top_countries = df.sort_values(by = 'Total', ascending= False).head(25)


c1 ,c2 = st.columns([1,3])

limit = c2.slider('Select number of countries',1,25,value =5)
countries = top_countries.index.tolist()[:limit]
countries_df = df.loc[countries,years].T
fig2 = px.area(countries_df ,x = countries_df.index , y = countries_df.columns)

c1.dataframe(top_countries)
c2.plotly_chart(fig2, use_container_width= True)


st.subheader("Trend comparison")
c1 , c2 = st.columns([1,3])
country_list = df.index.to_list()
countries = c2.multiselect("Select Countries", country_list)
if countries :
    countries_df = df.loc[countries,years].T
    fig3 = px.line(
        countries_df,
        x = countries_df.index,
        y = countries_df.columns
    )

    for country in countries:
        c1.info(f'{countries}:{df.loc[country , "Total"]} Immegrations')
    c2.plotly_chart(fig3, use_container_width=True)
    st.toast('Your graph has been loaded !', icon = '😊' ) 