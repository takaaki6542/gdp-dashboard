import streamlit as st
from pathlib import Path
from data_handler import GDPDataHandler
from visualization import GDPVisualization

def main():
    st.set_page_config(
        page_title='アメリカの非農業部門就業者数',
        page_icon=':earth_americas:',
    )

    # データ処理インスタンスの作成とデータの読み込み
    data_handler = GDPDataHandler(Path(__file__).parent / 'data/gdp_data.csv')

    # ページのタイトル
    '''
    # :earth_americas: GDP dashboard

    Browse GDP data from the [World Bank Open Data](https://data.worldbank.org/) website. As you'll
    notice, the data only goes to 2022 right now, and datapoints for certain years are often missing.
    But it's otherwise a great (and did I mention _free_?) source of data.
    '''

    min_value = data_handler.gdp_df['Year'].min()
    max_value = data_handler.gdp_df['Year'].max()

    from_year, to_year = st.slider(
        'Which years are you interested in?',
        min_value=min_value,
        max_value=max_value,
        value=[min_value, max_value])

    countries = data_handler.gdp_df['Country Code'].unique()

    if not len(countries):
        st.warning("Select at least one country")

    selected_countries = st.multiselect(
        'Which countries would you like to view?',
        countries,
        ['DEU', 'FRA', 'GBR', 'BRA', 'MEX', 'JPN'])

    # データのフィルタリングと表示
    filtered_gdp_df = data_handler.filter_data(selected_countries, from_year, to_year)

    st.header('GDP over time', divider='gray')
    GDPVisualization.render_chart(filtered_gdp_df)

    st.header(f'GDP in {to_year}', divider='gray')
    GDPVisualization.render_metrics(data_handler.gdp_df, selected_countries, from_year, to_year)

if __name__ == "__main__":
    main()
