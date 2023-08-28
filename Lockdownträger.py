import streamlit as st
import pandas as pd
import altair as alt

st.header("Viele Deutsche sind im Lockdown träger geworden")
st.subheader("Anteil der Befragten, die ihrer Selbsteinschätzung zufolge während der Lockdowns träger geworden sind (in %)")

source = pd.DataFrame({
        'Anteil(%)': [17.8, 26.9, 26.1, 21.4, 7.9],
        'Meinung': ['Stimme ganz zu', 'Stimme eher zu', 'Stimme eher nicht zu', 'Stimme überhaupt nicht zu', 'Weiß nicht']
     })
 
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil(%):Q',
        x='Meinung:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis: 2030 Befragte; in Deutschland; 2021
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle:  YouGOV")