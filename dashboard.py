import streamlit as st
import pandas as pd
import plotly.express as px

# --- Стилизация ---
bg_color = '#0B0909'
text_color = '#f1e1ae'
main_color = '#83380E'
secondary_colors = ['#616570', '#4e4a3e']
font_family = 'DejaVu Sans'

data = {
'Публикация': [
'Прототип за 10 дней', 'Лучшие инди-игры', 'Прототип за 10 дней: dzen',
'Shorts 1', 'Shorts 2', 'Shorts 3',
'Pinterest 1', 'Pinterest 2', 'Pinterest 3',
'TikTok 1', 'TikTok 2', 'TikTok 3',
'Dzen 1', 'Dzen 2', 'Dzen 3'
],
'Платформа': [
'DTF', 'DTF', 'Dzen',
'YouTube', 'YouTube', 'YouTube',
'Pinterest', 'Pinterest', 'Pinterest',
'TikTok', 'TikTok', 'TikTok',
'Dzen', 'Dzen', 'Dzen'
],
'Формат': [
'статья', 'статья', 'статья',
'видео', 'видео', 'видео',
'видео', 'видео', 'видео',
'видео', 'видео', 'видео',
'статья', 'статья', 'статья'
],
'Просмотры': [
3082, 1281, 9,
1763, 1209, 1158,
42, 39, 42,
120, 144, 148,
14, 43, 6
],
'Вовлеченность': [
0.14, 0.18, 0.33,
0.3, 0.5, 0.47,
0.25, 0.19, 0.29,
0.08, 0.12, 0.13,
0.21, 0.02, 0.17
],
'Реакции': [
17, 7, 1,
8, 11, 5,
4, 5, 4,
3, 4, 5,
2, 1, 0
],
'Комментарии': [
16, 0, 0,
6, 2, 2,
0, 0, 0,
0, 0, 0,
1, 0, 0
]
}
df = pd.DataFrame(data)


st.set_page_config(page_title="Дашборд", layout="wide", page_icon="")

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {bg_color};
        color: {text_color};
        font-family: {font_family}, sans-serif;
    }}
    .css-1d391kg, .css-1v0mbdj {{
        color: {text_color};
        background-color: {bg_color};
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Дашборд: On the Bottom of Nowhere")

# --- Фильтр по платформе ---
platforms_list = ['Все'] + sorted(df['Платформа'].unique())
selected_platform = st.selectbox("Выберите платформу", platforms_list)

if selected_platform != 'Все':
    filtered = df[df['Платформа'] == selected_platform]
else:
    filtered = df

# --- Графики ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Просмотры по публикациям")
    fig_views = px.bar(
        filtered, x='Публикация', y='Просмотры', color='Платформа',
        color_discrete_sequence=[main_color] + secondary_colors,
        labels={'Просмотры': 'Просмотры', 'Публикация': 'Публикация'},
        template='plotly_dark',
        title=None
    )
    
    fig_views.update_layout(
        title_text='', title='',
    font=dict(
        family='DejaVu Sans',  # или любой другой без засечек
        color='#f1e1ae',       # ваш цвет
        size=16
    ),
    title_font=dict(
        family='DejaVu Sans',
        color='#f1e1ae',
        size=20
    ),
    xaxis=dict(
        title_font=dict(
            family='DejaVu Sans',
            color='#f1e1ae',
            size=16
        ),
        tickfont=dict(
            family='DejaVu Sans',
            color='#f1e1ae',
            size=14
        )
    ),
    yaxis=dict(
        title_font=dict(
            family='DejaVu Sans',
            color='#f1e1ae',
            size=16
        ),
        tickfont=dict(
            family='DejaVu Sans',
            color='#f1e1ae',
            size=14
        )
    ),
    legend=dict(
        font=dict(
            family='DejaVu Sans',
            color='#f1e1ae',
            size=14
        )
    ),
    plot_bgcolor='#0B0909',
    paper_bgcolor='#0B0909',
    
)
    st.plotly_chart(fig_views, use_container_width=True)

with col2:
    st.subheader("Распределение реакций по платформам")
    fig_pie = px.pie(
        filtered, names='Платформа', values='Реакции',
        color_discrete_sequence=[main_color] + secondary_colors,
    )
    fig_pie.update_layout(
        title_text='', title='',
    font=dict(
        family='DejaVu Sans',  # или любой другой без засечек
        color='#f1e1ae',       # ваш цвет
        size=16
    ),
    title_font=dict(
        family='DejaVu Sans',
        color='#f1e1ae',
        size=20
    ),
    xaxis=dict(
        title_font=dict(
            family='DejaVu Sans',
            color='#f1e1ae',
            size=16
        ),
        tickfont=dict(
            family='DejaVu Sans',
            color='#f1e1ae',
            size=14
        )
    ),
    yaxis=dict(
        title_font=dict(
            family='DejaVu Sans',
            color='#f1e1ae',
            size=16
        ),
        tickfont=dict(
            family='DejaVu Sans',
            color='#f1e1ae',
            size=14
        )
    ),
    legend=dict(
        font=dict(
            family='DejaVu Sans',
            color='#f1e1ae',
            size=14
        )
    ),
    plot_bgcolor='#0B0909',
    paper_bgcolor='#0B0909'
)
    st.plotly_chart(fig_pie, use_container_width=True)

st.subheader("Вовлеченность vs Просмотры (размер — реакции)")
fig_scatter = px.scatter(
    filtered, x='Просмотры', y='Вовлеченность', size='Реакции',
    color='Платформа', hover_name='Публикация',
    color_discrete_sequence=[main_color] + secondary_colors,
)
fig_scatter.update_layout(
    title_text='', title='',
    font=dict(
        family='DejaVu Sans',  # или любой другой без засечек
        color='#f1e1ae',       # ваш цвет
        size=16
    ),
    title_font=dict(
        family='DejaVu Sans',
        color='#f1e1ae',
        size=20
    ),
    xaxis=dict(
        title_font=dict(
            family='DejaVu Sans',
            color='#f1e1ae',
            size=16
        ),
        tickfont=dict(
            family='DejaVu Sans',
            color='#f1e1ae',
            size=14
        )
    ),
    yaxis=dict(
        title_font=dict(
            family='DejaVu Sans',
            color='#f1e1ae',
            size=16
        ),
        tickfont=dict(
            family='DejaVu Sans',
            color='#f1e1ae',
            size=14
        )
    ),
    legend=dict(
        font=dict(
            family='DejaVu Sans',
            color='#f1e1ae',
            size=14
        )
    ),
    plot_bgcolor='#0B0909',
    paper_bgcolor='#0B0909'
)
st.plotly_chart(fig_scatter, use_container_width=True)

# --- Таблица ---
st.subheader("Данные по публикациям")
st.dataframe(filtered.style
    .set_properties(**{'background-color': bg_color, 'color': text_color, 'font-family': font_family, 'font-size': '16px'})
    .set_table_styles([{'selector': 'th', 'props': [('background-color', bg_color), ('color', text_color)]}])
)

st.markdown("---")
st.markdown("© Екатерина Лукиных, 2025")

