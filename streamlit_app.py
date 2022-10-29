import streamlit as st
from datetime import datetime

st.set_page_config(layout="wide",page_icon="🚀",page_title='Dashboard')

st.title('Application')


project = ['空','🀄️麻将','🕙血染','🐺狼人杀','📚剧本杀','🎲桌游']

def create_position(term):
    result = st.selectbox(term,project)
    #st.button(term)
    return (result,term)

with st.container():
    col1,col2,col3,col4 = st.columns(4)

    with col1:
        b1 = create_position('包3')
    with col2:
        b2 = create_position('包2')
    with col3:
        b3 = create_position('包1')
    with col4:
        rb = create_position('日包')

with st.container():
    col1,col2,col3,col4,col5,col6 = st.columns(6)

    with col1:
        k1 = create_position('卡四')
    with col2:
        k2 = create_position('卡三')
    with col3:
        k3 = create_position('卡二')
    with col4:
        k4 = create_position('卡一')
    with col5:
        lw = create_position('里外')
    with col6:
        ll = create_position('里里')
with st.container():
    col1,col2,col3,col4,col5,col6 = st.columns(6)

    with col5:
        dtw = create_position('大厅外')
        dtl = create_position('大厅里')
    with col6:
        qqw = create_position('秋千外')
        qql = create_position('秋千里')
    
position = [k1,k2,k3,k4,lw,ll,dtw,dtl,qqw,qql,b1,b2,b3,rb]    


def create_status(term):
    st.markdown('## ' + term)
    for p in position:
        if p[0] == term:
            st.markdown('- ' + p[1])
    
with st.sidebar:
    st.title('正在进行')
    create_status('🀄️麻将')    
    create_status('🐺狼人杀')    
    create_status('🕙血染')    
    create_status('📚剧本杀')    
    create_status('🎲桌游')    