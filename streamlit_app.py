import streamlit as st
from datetime import datetime

st.set_page_config(layout="wide",page_icon="π",page_title='Dashboard')

st.title('Application')


project = ['η©Ί','ποΈιΊ»ε°','πθ‘ζ','πΊηΌδΊΊζ','πε§ζ¬ζ','π²ζ‘ζΈΈ']

def create_position(term):
    result = st.selectbox(term,project)
    #st.button(term)
    return (result,term)

with st.container():
    col1,col2,col3,col4 = st.columns(4)

    with col1:
        b1 = create_position('ε3')
    with col2:
        b2 = create_position('ε2')
    with col3:
        b3 = create_position('ε1')
    with col4:
        rb = create_position('ζ₯ε')

with st.container():
    col1,col2,col3,col4,col5,col6 = st.columns(6)

    with col1:
        k1 = create_position('ε‘ε')
    with col2:
        k2 = create_position('ε‘δΈ')
    with col3:
        k3 = create_position('ε‘δΊ')
    with col4:
        k4 = create_position('ε‘δΈ')
    with col5:
        lw = create_position('ιε€')
    with col6:
        ll = create_position('ιι')
with st.container():
    col1,col2,col3,col4,col5,col6 = st.columns(6)

    with col5:
        dtw = create_position('ε€§εε€')
        dtl = create_position('ε€§ει')
    with col6:
        qqw = create_position('η§εε€')
        qql = create_position('η§ει')
    
position = [k1,k2,k3,k4,lw,ll,dtw,dtl,qqw,qql,b1,b2,b3,rb]    


def create_status(term):
    st.markdown('## ' + term)
    for p in position:
        if p[0] == term:
            st.markdown('- ' + p[1])
    
with st.sidebar:
    st.title('ζ­£ε¨θΏθ‘')
    create_status('ποΈιΊ»ε°')    
    create_status('πΊηΌδΊΊζ')    
    create_status('πθ‘ζ')    
    create_status('πε§ζ¬ζ')    
    create_status('π²ζ‘ζΈΈ')    