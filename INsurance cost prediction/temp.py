# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st
import joblib

def main():
    html_temp= """
    <div style="background-color:lightblue;padding:16px">
    <h2 style="color:black";text-align:center> HEALTH INSURANCE COST PREDICTION USING ML<h2>
    </div>
    
    """
    
    st.markdown(html_temp,unsafe_allow_html=True)


if __name__=='__main__':
    main()