
import streamlit as st

# EDA Pkgs
import pandas as pd
import numpy as np
import os

# Plotting Pkgs
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title("Bipolar Disorder Exploratory Data Analysis")
    st.markdown("""
    	#### Description
    	+ In statistics, exploratory data analysis is an approach of analyzing data sets to summarize their main characteristics, often using statistical graphics and other data visualization methods. """)


    my_dataset = "patient.csv"

    # To Improve speed and cache data
    @st.cache(persist=True)
    def explore_data(dataset):
    	df = pd.read_csv(os.path.join(dataset))
    	return df 

    # Load Our Dataset
    data = explore_data(my_dataset)

    # Show Dataset
    species_option = st.selectbox('View data',('Choose','Head','Tail'))
    if species_option == 'Head':
    	st.write(data.head())
    elif species_option == 'Tail':
    	st.write(data.tail())
    else:
        st.write()

    # Show All Column Names
    if st.checkbox("Show All Column Names"):
    	st.text("Columns:")
    	st.write(data.columns)

    # Show  Shape of Dataset
    data_dim = st.radio('Length of data ',('Rows','Columns'))
    if data_dim == 'Rows':
    	st.text("Showing Length of Rows")
    	st.write(len(data))
    if data_dim == 'Columns':
    	st.text("Showing Length of Columns")
    	st.write(data.shape[1])

    # Show Summary of Dataset
    if st.checkbox("Statistical details of Dataset"):
        st.markdown("""
    	#### Description
    	+ Shows the Statistical details such as mean,standard deviation ,min ,max etc of each column""")
    	
        st.write(data.describe())



    # Show Plots
    if st.checkbox(" Count Plot "):
        st.markdown("""
    	#### Description
    	+ Shows the counts of observations in each categorical bin using bars.""")

        sns.countplot(data['episode'],label="Count")
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()


    # Show Correlation Plots
    if st.checkbox(" Correlation Plot  "):
        st.markdown("""
    	#### Description
    	+ A correlation matrix is a tabular data representing the 'correlations' between pairs of variables in a given data""")
        sns.heatmap(data.corr())
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
    st.markdown(""" """)

    #KDE plots
    st.markdown("""Density Plots""")
    st.markdown("""
    	#### Description
    	+ A density plot is a representation of the probability density function of the parameter""")
    species_option = st.selectbox('',('Choose','Sleep_quality','Caffeine'))
    if species_option == 'Sleep_quality':
        sns.kdeplot(data=data, x='sleep_quality',shade=True,hue='episode')
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
    elif species_option == 'Caffeine':
        sns.kdeplot(data=data, x='caffeine',shade=True,hue='episode')
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
    else:
        st.write()

    #KDE plots
    st.markdown("""Violin Plots""")
    st.markdown("""
    	#### Description
    	+ A violin plot depicts distributions of numeric data for one or more groups using density curves""")
    species_option = st.selectbox('',('Choose','motivation','anxiety'))
    if species_option == 'anxiety':
        sns.violinplot(y="anxiety", x="episode",data=data, palette="muted",split=True)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
    elif species_option == 'motivation':
        sns.violinplot(y="motivation", x="episode",data=data, palette="muted",split=True)
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
    else:
        st.write()
        


if __name__ == "__main__":
    main()
