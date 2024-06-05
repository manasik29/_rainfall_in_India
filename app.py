import streamlit as st
import pandas as pd
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')

df = pd.read_excel("processed_data.xlsx", index_col=False)


def yearly_filter_data(df, start_year, end_year):
    filtered_df = df[(df['YEAR'] >= start_year) & (df['YEAR'] <= end_year)]
    return filtered_df


def main():
    st.set_page_config(page_title="Monsoon Chronicles",
                       page_icon=":umbrella_with_rain_drops:", layout="wide")
    st.markdown("<h1 style='text-align: center;'>Indian Monsoon - A Deep Dive</h1>", unsafe_allow_html=True)
    # st.title("Monsoon Chronicles: India's Rainfall Journey")
    st.markdown('<style>div.block-container{padding-top:1rem;}<style>',
                unsafe_allow_html=True)
    st.write("""
             Hello folks,

             If you have ever lived in India, you must know rainfall in India
             is a significant aspect of the country's climate. The Indian
             monsoon, which typically occurs from June to September,
             brings the majority of the annual rainfall. However,
             rainfall patterns can vary significantly across
             different regions and time periods. Analyzing historical
             rainfall data can provide insights into trends, variability,
             and potential impacts of climate change on India's rainfall
             patterns.

             This web app explores monthly rainfall data of 36 meteorological
             sub-divisions of India from the years 1901 to 2015, sourced from
             [Open Goverment Data (OGD) Platform India](https://data.gov.in/),
             aiming to visualize trends and patterns over time.
    """)
    # Divider line between write-up and year selector
    st.markdown("<hr style='height: 1px; background-color: white;'>",
                unsafe_allow_html=True)
    st.sidebar.title("Slicers")
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    # Create 2 columns for start year, end year
    col1, col2 = st.sidebar.columns([1, 1])
    # Input for start year
    with col1:
        start_year = st.number_input(":calendar: Start Year", min_value=1901,
                                     max_value=2015, step=1, value=1901)
    # Input for end year
    with col2:
        end_year = st.number_input(":calendar: End Year", min_value=1901,
                                   max_value=2015, step=1, value=2015)
    # Validation for start year < end year
    if start_year > end_year:
        st.sidebar.error("Start year cannot be greater than end year.")
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    subdivision = st.sidebar.multiselect(":round_pushpin: Subdivisions",
                                         df["SUBDIVISION"].unique(),
                                         placeholder="Multiple selections")
    if not subdivision:
        df2 = df.copy()
    else:
        df2 = df[df["SUBDIVISION"].isin(subdivision)]
    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    seasons = st.sidebar.multiselect(":partly_sunny_rain: Seasons",
                                     #  df.columns[-5:],
                                     ['SPRING', 'SUMMER', 'MONSOON', 'AUTUMN',
                                      'WINTER'],
                                     placeholder="Multiple selections")
    if not seasons:
        df3 = df2.copy()
    else:
        df3 = df2[['SUBDIVISION', 'YEAR'] + seasons]
    st.sidebar.markdown("<br>", unsafe_allow_html=True)

    st.sidebar.markdown("<br>", unsafe_allow_html=True)
    # Execute filtering process
    if st.sidebar.button("Display Data") and start_year <= end_year:
        # Filter the DataFrame based on selected years
        yearly_filtered_df = yearly_filter_data(df3, start_year, end_year)
        st.write(yearly_filtered_df)


if __name__ == "__main__":
    main()
