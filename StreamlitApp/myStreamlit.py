# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 14:46:00 2021

@author: chrst
"""

import streamlit as st
def myCaption(mystring):
    st.markdown('<p class="caption">'+
                mystring
                +'</p>', unsafe_allow_html=True)  
  