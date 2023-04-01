import streamlit as st
import plotly.express as px
import pandas as pd
import io
df = px.data.tips()
df["size"] = df["size"].astype(str)
df["profit"] = (0.86 * df["total_bill"]) + df["tip"]
st.set_page_config(layout='wide' , initial_sidebar_state="expanded")

def Main_page():
    st.title("Data Description")
    st.markdown("### Data Head")
    st.write(df.head(5))
    c1,c2 = st.columns([1.5,1])
    with c1 :
        st.markdown("### Data Info")
        buffer = io.StringIO()
        df.info(buf=buffer)
        s= buffer.getvalue()
        st.text(s)
    with c2 :
        st.markdown("### Descriptive Statstics")
        st.write(df.describe())
       
    st.markdown("### Categories Distribution")
    col1 , col2 , col3 , col4 , col5 = st.columns(5)
    with col1:
        st.write(df["sex"].value_counts())
    with col2:
        st.write(df["smoker"].value_counts())
    with col3 :
        st.write(df["day"].value_counts())
    with col4:
        st.write(df["time"].value_counts())
    with col5:
        st.write(df["size"].value_counts())
        
        
def Second_Page():
    st.title("Data Visualization")
    st.header("Numerical Graphs")
    st.sidebar.markdown("### Histogram Chart Options")
    Hist_Num_Col = st.sidebar.selectbox("Select Histogram Col" , ["total_bill","profit","tip"] )
    st.sidebar.markdown("### Scatter Chart Options")
    scatter_X_Col = st.sidebar.selectbox("Select Scatter X-axis Col" , ["total_bill","profit","tip"] )
    scatter_Y_Col = st.sidebar.selectbox("Select Y-axis Col" , ["total_bill","profit","tip"] )
    color_option = st.sidebar.checkbox("Scatter with color")
    st.markdown("### Histogram Chart ")
    st.plotly_chart(px.histogram(data_frame = df , x = Hist_Num_Col , title=Hist_Num_Col.capitalize() + " Distribution" , labels={Hist_Num_Col : Hist_Num_Col.capitalize()}))
    st.markdown("### Scatter Chart ")
    if color_option:
        color_col = st.sidebar.selectbox("Choose Color Col", ["sex","smoker","day","size"] )
        st.plotly_chart(px.scatter(data_frame = df , x = scatter_X_Col, y = scatter_Y_Col ,color=color_col,hover_data=[color_col] ,title="Corrleation Between " + scatter_X_Col.capitalize() +  "and " + scatter_Y_Col.capitalize(), labels={scatter_X_Col : scatter_X_Col.capitalize() , scatter_Y_Col:scatter_Y_Col.capitalize()}))
    else:
        st.plotly_chart(px.scatter(data_frame = df , x = scatter_X_Col, y = scatter_Y_Col , title="Corrleation Between " + scatter_X_Col.capitalize() +  "and " + scatter_Y_Col.capitalize(), labels={scatter_X_Col : scatter_X_Col.capitalize() , scatter_Y_Col:scatter_Y_Col.capitalize()}))

def Third_Page():
    st.title("Data Visualization_2")
    st.header("Categorical Graphs")
    st.sidebar.markdown("### CountPlot Chart Options")
    CountPlot_Col = st.sidebar.selectbox("Select Histogram Col" , ["sex","smoker","day","size"]  )
    CountPlot_color_option = st.sidebar.checkbox("Count Plot with color")
    st.sidebar.markdown("### BarPlot Chart Options")
    BarPlot_X_Col = st.sidebar.selectbox("Select Bar X Col" , ["sex","smoker","day","size"]  )
    BarPlot_Y_Col = st.sidebar.selectbox("Select Bar Y Col" , ["total_bill","profit","tip"]  )
    BarPlot_color_option = st.sidebar.checkbox("Bar Plot with color")
    if CountPlot_color_option:
        CountPlot_color_col = st.sidebar.selectbox("Choose Color Col", ["sex","smoker","day","size"] )
        st.plotly_chart(px.histogram(data_frame = df , x = CountPlot_Col ,color = CountPlot_color_col,barmode = "group",title=CountPlot_Col.capitalize() + " Distribution" , labels={CountPlot_Col : CountPlot_Col.capitalize()}))
    else:
        st.plotly_chart(px.histogram(data_frame = df , x = CountPlot_Col ,title=CountPlot_Col.capitalize() + " Distribution" , labels={CountPlot_Col : CountPlot_Col.capitalize()}))
    
    if BarPlot_color_option:
        Bar_color_col = st.sidebar.selectbox("Choose BarColor Col", ["sex","smoker","day","size"] )
        st.plotly_chart(px.bar(data_frame = df , x = BarPlot_X_Col, y = BarPlot_Y_Col ,color=Bar_color_col,hover_data=[Bar_color_col] ,title="Summation of " + BarPlot_Y_Col.capitalize()  + "grouped by " + BarPlot_X_Col.capitalize() , labels={BarPlot_X_Col : BarPlot_X_Col.capitalize() , BarPlot_Y_Col:BarPlot_Y_Col.capitalize()}))
    else:
        st.plotly_chart(px.bar(data_frame = df , x = BarPlot_X_Col, y = BarPlot_Y_Col ,title="Summation of " + BarPlot_Y_Col.capitalize()  + " grouped by " + BarPlot_X_Col.capitalize() , labels={BarPlot_X_Col : BarPlot_X_Col.capitalize() , BarPlot_Y_Col:BarPlot_Y_Col.capitalize()}))


    
Pages_to_Func = {
    
    "Data Description" : Main_page,
    "Numerical" : Second_Page,
    "Categorical" : Third_Page
}
    
Selected_Page = st.sidebar.selectbox("Select the Page" , Pages_to_Func.keys())
Pages_to_Func[Selected_Page]()
