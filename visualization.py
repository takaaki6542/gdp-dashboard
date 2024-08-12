import streamlit as st
import math

class GDPVisualization:
    @staticmethod
    def render_chart(filtered_gdp_df):
        """GDPデータを線グラフとして描画する。"""
        st.line_chart(
            filtered_gdp_df,
            x='Year',
            y='GDP',
            color='Country Code',
        )

    @staticmethod
    def render_metrics(gdp_df, selected_countries, from_year, to_year):
        """選択された国のGDP成長率をメトリクスとして表示する。"""
        first_year = gdp_df[gdp_df['Year'] == from_year]
        last_year = gdp_df[gdp_df['Year'] == to_year]

        cols = st.columns(4)
        for i, country in enumerate(selected_countries):
            col = cols[i % len(cols)]
            with col:
                first_gdp = first_year[first_year['Country Code'] == country]['GDP'].iat[0] / 1000000000
                last_gdp = last_year[last_year['Country Code'] == country]['GDP'].iat[0] / 1000000000

                if math.isnan(first_gdp):
                    growth = 'n/a'
                    delta_color = 'off'
                else:
                    growth = f'{last_gdp / first_gdp:,.2f}x'
                    delta_color = 'normal'

                st.metric(
                    label=f'{country} GDP',
                    value=f'{last_gdp:,.0f}B',
                    delta=growth,
                    delta_color=delta_color
                )
