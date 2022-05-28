# Use this app in visualizing the dataset of your choice

import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import time


st.title("*Data Visualisation App*")

st.write("Visualisation has been made easy for data scientist using this app.")

st.subheader("Instructions:")

st.markdown(""" 1. Upload your dataset from your local device. \n
 2. Select your choice of Visualisation. \n
 3. Select the columns you would like on each axis.\n
 4. You can decide to give it a title or not. \n
 5. Download your Image by right clicking on the image. """)

st.markdown("Use this app to create any visualisation of your choice.")

file = st.file_uploader("Upload the dataset you would like to use.")


def load_file(fil):
    time.sleep(1)
    if fil is not None:
        df = pd.read_csv(fil)
    else:
        st.stop()
    return df


dataset = load_file(file)

for col in dataset.columns:
    if dataset[col].dtype == "object":
        if dataset[col].nunique() > 3:
            dataset.drop(col, inplace=True, axis=1)


st.write("Take a glimpse at the dataset.")

head = dataset.head() 
st.write(head)

st.write(f"Shape of {file.name[:-4]}", dataset.shape)


selected_plottype = st.selectbox("Pick the type of graph you would like to plot:", ['Scatter-plot', 'Count-plot',
                                 'Bar-plot', 'Histogram', 'Boxen-plot'])

if selected_plottype == 'Scatter-plot' or selected_plottype == 'Bar-plot' or selected_plottype == 'Histogram' or \
        selected_plottype == 'Boxen-plot':
    selected_x_var = st.selectbox("What column do you want on the X axis:", dataset.columns)
    selected_y_var = st.selectbox("What about y axis:", dataset.columns)
    
elif selected_plottype == 'Count-plot':
    count_col = []
    for col in dataset.columns:
        if dataset[col].nunique() < 3:
            count_col.append(col)
    selected_var = st.selectbox("Pick a column for your count plot:", count_col)

else:
    st.stop()
    
fig, ax = plt.subplots()
name = st.text_input("Name your graph:")

plt.title(name)

if selected_plottype == "Scatterplot":
    ax = sns.scatterplot(x=dataset[selected_x_var], y=dataset[selected_y_var])
elif selected_plottype == "Bar-plot":
    ax = sns.barplot(x=dataset[selected_x_var], y=dataset[selected_y_var])
elif selected_plottype == "Histogram":
    ax = sns.histplot(x=dataset[selected_x_var], y=dataset[selected_y_var])
elif selected_plottype == "Boxen-plot":
    ax = sns.boxenplot(x=dataset[selected_x_var], y=dataset[selected_y_var])
elif selected_plottype == "Count-plot":
    ax = sns.countplot(x=dataset[selected_var])

st.pyplot(fig)

st.download_button(label='Download Image.', file_name='download', data=fig)