# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 19:44:17 2021

@author: chrst
"""

import streamlit as st
import altair as alt
import time
import math
import numpy as np
import pandas as pd
from myStreamlit import myCaption


def howBuild():
    st.title('Build your own DIY permeability-meter!')
    st.header('Supplies:')
    text,pic1=st.beta_columns((3,2))
    size=200
    
    
    
    with text:
        st.markdown("""
            * **Plastic jar** – Anything plastic with a screw cap. Peanut \
                butter jars work well.
            * **Scissors or hammer** – have a grown up help you break \
                \away the top of the jar cap: make sure to leave the sides \
                    of the cap with the screw threading! 
            * **Soil or other grains** – to measure the permeability of \
                (see below for soils that work well).
            * **Cheesecloth** – to hold soil in.
            * **Ruler and Marker** – to mark lengths on bottle.
            * **Phone camera or stopwatch** – to time water motion.
            * **Jar or bucket** – to collect water runoff.
            """)
    with pic1:
        st.image('images\SketchJar.jpg')
        myCaption('Figure 1: Features to look for in the perfect flow meter jar.')
        st.image('images\PeanutJar.jpeg')
        myCaption('Figure 2: For example, this plastic peanut butter jar works well.')
        
        
    st.header('Building your permeameter:')
    text,pic1=st.beta_columns((1,1))
    size=200
    with text:
        st.markdown("""
            1. **Cut** the bottom off of your plastic jar with some scissors \
                (with the help of an adult). Try to make the cut straight (Figure 3).  \n
            2. **Mark** lines on the bottle using a marker and a ruler in \
                starting at the cap. Centimeters work a bit better since \
                    they're smaller.\
                    Write down the number every few so you can easily \
                        tell the height of water using these marks (Figure 4).  \n
            3. **Break** away the center of the screw cap of the plastic jar. \
                Have an adult help you use scissors or a hammer to break this \
                    away. Break away as much as you can, but make sure to \
                        leave the side with the screw threads completely intact (Figure 5).  \n
            4. **Attach** some cheesecloth to the bottom of the jar by covering \
                the lid opening and screwing on the cap. The screw cap should \
                    hold the cheesecloth tightly against the jar lid. The hole \
                        in the cap should be completely filled with the \
                            cheesecloth (Figure 6).  \n
            5. **Test** your setup (Figure 7) using some easy sample around the house \
                instead of a dirty soil. This could be a fine gravel or \
                aquarium sand! Fill the bottle to ~5 cm or ~2 in with this \
                “test sample” to make sure the water drains at a good \
                speed: ideally the bottle should take about 1 to 5 \
                minutes to drain so that you can watch it happen. \
                Try modifying your setup until you are happy with how quickly \
                    the water drains.  \n
            6. **Measure** the permeability of this test sample using the \
                directions below!
            """)
    with pic1:
        st.image('images\Build1.jpeg',width=size)
        myCaption('Figure 3: Cut the bottom off the jar')
        st.image('images\Build2.jpeg', width=size)
        myCaption('Figure 4: Mark heights in centimeters, starting at the cap')
        st.image('images\Build3.jpeg', width=size)
        myCaption('Figure 5: Break hole in center of screw cap')
        st.image('images\Build4.jpeg', width=size)
        myCaption('Figure 6: Attach cheesecloth using screw cap')
        st.image('images\Build5.jpeg', width=size)
        myCaption('Figure 7: Prototype permeability-meter ready for testing')

        
    st.header('Experiment:')
    text,vid=st.beta_columns((1.8,1))
    with text:
        st.markdown("""
            1. **Sample selection:** Fill your permeability-meter with a little \
                bit of your gravel or soil sample. Try to fill it up to one of \
                the lines you marked, like 5 cm or 2 in. Write down this soil height.
            1. **Prepare setup:** Use your sink to fill the bottle to the top \
                with water, and the quickly close off the top with the screw cap. \
                The cap should stop the water from flowing out the bottom, so \
                you can get ready for the experiment. Place your bottle above \
                a bucket, mason jar, or the drain of your sink so the water can \
                flow freely once the cap is unscrewed.
            1. **Observe:** When you’re ready to go, unscrew the cap and watch \
                the water drain. How quickly does it drain? Take notes about \
                how long it takes to completely drain, and if you would \
                categorize the sample as high permeability (water moves through \
                it quickly) or low permeability (water moves through it slowly).
            1. **Measure:** To be a bit more quantitative, use a stopwatch to \
                measure the actual speed. Write down the time on the stopwatch \
                when the water passes each marker, or use a camera to record \
                the experiment, and then re-watch the video. You can compute \
                the actual permeability (and retention) from this data using \
                the **process experiment data** tab on the left.
            1. **Iterate:** When engineers design and build systems, they \
                iterate between testing out their setup and redesigning a \
                better version. Try modifying your experimental setup to make \
                it better! You might try using different building materials, \
                constructing it differently, or changing how you watch and \
                record the experiment. **Water taking too long to drain?** \
                Try packing your permeability-meter with a shorter height of \
                your soil sample: the thinner sample will have less resistance \
                to flow, so the experiment will run faster.
                Feel free to go back and forth between \
                designing, building, and testing your experimental setup until \
                you are happy with how it works. 
            1. **Explore:** Now you’re ready to start measuring real soil \
                samples! Try exploring your neighborhood with a hand trowel \
                to collect soil samples to measure, and record what you find. 
            1. **Learn:** Read more about what soil permeability means for \
                plants as changing climate alter rainfall on the **what is \
                soil permeability** tab, and attempt the **designer soil\
                challenge** to try designing the best soil for growing plants!
            """)
    with vid:
        filenames=['images\gravel_1x.mp4','images\sand_10x.mp4']
        for i in range(2):
            video_file = open(filenames[i], 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)

        



    