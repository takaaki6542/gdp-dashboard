import pandas as pd
from pathlib import Path
import streamlit as st

@st.cache_data
def load_gdp_data(data_path, min_year=1960, max_year=2022):
    """GDPデータをCSVファイルから読み込み、適切な形式に変換する。"""
    raw_gdp_df = pd.read_csv(data_path)
    gdp_df = raw_gdp_df.melt(
        ['Country Code'],
        [str(x) for x in range(min_year, max_year + 1)],
        'Year',
        'GDP',
    )
    gdp_df['Year'] = pd.to_numeric(gdp_df['Year'])
    return gdp_df

class GDPDataHandler:
    def __init__(self, data_path):
        self.data_path = data_path
        self.MIN_YEAR = 1960
        self.MAX_YEAR = 2022
        self.gdp_df = self.load_data()

    def load_data(self):
        """キャッシュされたデータを取得"""
        return load_gdp_data(self.data_path, self.MIN_YEAR, self.MAX_YEAR)

    def filter_data(self, selected_countries, from_year, to_year):
        """選択された国と年に基づいてGDPデータをフィルタリングする。"""
        return self.gdp_df[
            (self.gdp_df['Country Code'].isin(selected_countries))
            & (self.gdp_df['Year'] <= to_year)
            & (from_year <= self.gdp_df['Year'])
        ]
