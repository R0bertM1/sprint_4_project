import pandas as pd
import streamlit as st
import plotly.express as px

vehicles = pd.read_csv('C:/Users/rober/OneDrive/Documents/sprint_4_project/vehicles_us.csv')

# Function to plot histograms based on condition
def plot_histograms(df, conditions):
    for condition in conditions:
        filtered_df = vehicles[vehicles['condition'] == condition]
        if not filtered_df.empty:
            fig = px.histogram(filtered_df, x='days_listed', title=f'Days Listed for {condition.capitalize()} Condition')
            st.plotly_chart(fig)

# Main Streamlit app
def main():
    st.header('Days Listed By Condition')

    # Checkbox for each condition
    conditions = ['salvage', 'fair', 'good', 'excellent', 'like new', 'new']
    selected_conditions = [st.checkbox(condition, value=True) for condition in conditions]

    # Plot histograms based on selected conditions
    for condition, selected in zip(conditions, selected_conditions):
        if selected:
            plot_histograms(vehicles, [condition])
    
    st.header('Days Listed By Price')
    fig = px.scatter(vehicles, x='price', y='days_listed')
    st.plotly_chart(fig)

# Run the app
if __name__ == '__main__':
    main()