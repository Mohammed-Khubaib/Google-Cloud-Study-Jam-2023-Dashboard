import datetime
import pytz
import json
import time
import numpy as np 
import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
from st_on_hover_tabs import on_hover_tabs
from streamlit_elements import nivo
from streamlit_elements import elements, mui
from streamlit_gsheets import GSheetsConnection

st.set_page_config('GDSC MCET',page_icon="./assets/logo.png",layout="wide")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)
#load lottie files
def load_lottie_file(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)
def subheadingtext(text:str):
    message = []
    response = st.empty()
    tokens = list(text)
    for i in tokens:
        message.append(i)
        result = "".join(message)
        response.markdown(f'### {result} ',unsafe_allow_html=True)
        time.sleep(0.035)
        # time.sleep(0.12)
def pieChart(tab,yes_count,no_count) :
    with elements(str(tab)):
                DATA = [
                    {"id": "Yes", "label": "Yes", "value": int(yes_count),"color": "hsl(21, 70%, 50%)"},
                    {"id": "No", "label": "No", "value": int(no_count), "color": "hsl(0, 70%, 50%)"}
                ]
                with mui.Box(sx={"height": 350}):
                    nivo.Pie(
                        data= DATA,
                        keys=["Yes","No"],
                        margin={ "top": 40, "right": 80, "bottom": 80, "left": 80 },
                        innerRadius=0.5,
                        padAngle=0.7,
                        cornerRadius=3,
                        activeOuterRadiusOffset=8,
                        borderWidth=1,
                        borderColor = {
                            'from' : "DATA",
                            "modifiers": [
                                [
                                    "darker",
                                    0.2
                                ]
                            ]
                        },
                        arcLinkLabelsSkipAngle=10,
                        arcLinkLabelsTextColor="#fff",
                        arcLinkLabelsThickness=5,
                        arcLinkLabelsColor={ "from": 'color' },
                        arcLabelsSkipAngle=2,
                        arcLabelsTextColor={
                        "from": 'color',
                        "modifiers": [
                            [
                                'darker',
                                2
                            ]
                        ]
                        },
                        defs = [
                        {
                            "id": "dots",
                            "type": "patternDots",
                            "background": "inherit",
                            "color": "#FFFFFF4D",
                            "size": 4,
                            "padding": 2,
                            "stagger": "true"
                        },
                        {
                            "id": "lines",
                            "type": "patternLines",
                            "background": "inherit",
                            "color": "rgba(255, 255, 255, 0.3)",
                            "rotation": -45,
                            "lineWidth": 6,
                            "spacing": 10
                        }
                        ],

                    fill = [
                        {
                            "match": {
                                "id": "Yes"
                            },
                            "id": "dots"
                        },
                        {
                            "match": {
                                "id": "No"
                            },
                            "id": "lines"
                        }
                    ],
                    legends=[
                                {
                                    "anchor": 'bottom',
                                    "direction": 'row',
                                    # "justify": "false",
                                    "translateX": 1,
                                    "translateY": 76,
                                    "itemsSpacing": 10,
                                    "itemWidth": 100,
                                    "itemHeight": 18,
                                    "itemTextColor": '#999',
                                    "itemDirection": 'left-to-right',
                                    "itemOpacity": 2,
                                    "symbolSize": 10,
                                    "symbolShape": 'circle',
                                    "effects": [
                                        {
                                            "on": 'hover',
                                            "style": {
                                                "itemTextColor": '#fff'
                                            }
                                        }
                                    ]
                                }
                            ],
                            theme={
                            "background": "#0e1016",
                            "textColor": "#fff",
                            "tooltip": {
                                "container": {
                                    "background": "#111",
                                    "color": "#fff",
                                }
                            }
                        }
                    )


def pieChart4(tab,completed_status) :
    with elements(str(tab)):
                DATA = [
                    {"id": "0/4", "label": "0", "value": int(completed_status[0]),"color": "hsl(21, 70%, 50%)"},
                    {"id": "1/4", "label": "1", "value": int(completed_status[1]), "color": "hsl(0, 70%, 50%)"},
                    {"id": "2/4", "label": "2", "value": int(completed_status[2]),"color": "hsl(21, 70%, 50%)"},
                    {"id": "3/4", "label": "3", "value": int(completed_status[3]), "color": "hsl(0, 70%, 50%)"},
                    {"id": "4/4", "label": "4", "value": int(completed_status[4]), "color": "hsl(0, 70%, 50%)"},
                ]
                with mui.Box(sx={"height": 350}):
                    nivo.Pie(
                        data= DATA,
                        keys=["0","1","2","3","4"],
                        margin={ "top": 40, "right": 80, "bottom": 80, "left": 80 },
                        innerRadius=0.5,
                        padAngle=0.7,
                        cornerRadius=3,
                        activeOuterRadiusOffset=8,
                        borderWidth=1,
                        borderColor = {
                            'from' : "DATA",
                            "modifiers": [
                                [
                                    "darker",
                                    0.2
                                ]
                            ]
                        },
                        arcLinkLabelsSkipAngle=10,
                        arcLinkLabelsTextColor="#fff",
                        arcLinkLabelsThickness=5,
                        arcLinkLabelsColor={ "from": 'color' },
                        arcLabelsSkipAngle=2,
                        arcLabelsTextColor={
                        "from": 'color',
                        "modifiers": [
                            [
                                'darker',
                                2
                            ]
                        ]
                        },
                        defs = [
                        {
                            "id": "dots",
                            "type": "patternDots",
                            "background": "inherit",
                            "color": "#FFFFFF4D",
                            "size": 4,
                            "padding": 2,
                            "stagger": "true"
                        },
                        {
                            "id": "lines",
                            "type": "patternLines",
                            "background": "inherit",
                            "color": "rgba(255, 255, 255, 0.3)",
                            "rotation": -45,
                            "lineWidth": 6,
                            "spacing": 10
                        }
                        ],

                    fill = [
                        {
                            "match": {
                                "id": "0/4"
                            },
                            "id": "dots"
                        },
                        {
                            "match": {
                                "id": "1/4"
                            },
                            "id": "lines"
                        },
                        {
                            "match": {
                                "id": "2/4"
                            },
                            "id": "lines"
                        },
                        {
                            "match": {
                                "id": "3/4"
                            },
                            "id": "dots"
                        },
                        {
                            "match": {
                                "id": "4/4"
                            },
                            "id": "lines"
                        }
                    ],
                    legends=[
                                {
                                    "anchor": 'bottom',
                                    "direction": 'row',
                                    # "justify": "false",
                                    "translateX": 1,
                                    "translateY": 76,
                                    "itemsSpacing": 10,
                                    "itemWidth": 50,
                                    "itemHeight": 18,
                                    "itemTextColor": '#999',
                                    "itemDirection": 'left-to-right',
                                    "itemOpacity": 2,
                                    "symbolSize": 10,
                                    "symbolShape": 'circle',
                                    "effects": [
                                        {
                                            "on": 'hover',
                                            "style": {
                                                "itemTextColor": '#fff'
                                            }
                                        }
                                    ]
                                }
                            ],
                            theme={
                            "background": "#0e1016",
                            "textColor": "#fff",
                            "tooltip": {
                                "container": {
                                    "background": "#111",
                                    "color": "#fff",
                                }
                            }
                        }
                    )
def pieChart9(tab,completed_status) :
    with elements(str(tab)):
                DATA = [
                    {"id": "0", "label": "0", "value": int(completed_status[0]),"color": "hsl(21, 70%, 50%)"},
                    {"id": "1", "label": "1", "value": int(completed_status[1]), "color": "hsl(0, 70%, 50%)"},
                    # {"id": "2//49", "label": "2", "value": int(completed_status[2]),"color": "hsl(21, 70%, 50%)"},
                    # {"id": "3/9", "label": "3", "value": int(completed_status[3]), "color": "hsl(0, 70%, 50%)"},
                    # {"id": "4/9", "label": "4", "value": int(completed_status[4]), "color": "hsl(0, 70%, 50%)"},
                    # {"id": "5/9", "label": "5", "value": int(completed_status[5]), "color": "hsl(0, 70%, 50%)"},
                    # {"id": "6/9", "label": "6", "value": int(completed_status[6]), "color": "hsl(0, 70%, 50%)"},
                    # {"id": "7/9", "label": "7", "value": int(completed_status[7]), "color": "hsl(0, 70%, 50%)"},
                    # {"id": "8/9", "label": "8", "value": int(completed_status[8]), "color": "hsl(0, 70%, 50%)"},
                    # {"id": "9/9", "label": "9", "value": int(completed_status[9]), "color": "hsl(0, 70%, 50%)"},
                ]
                with mui.Box(sx={"height": 350}):
                    nivo.Pie(
                        data= DATA,
                        keys=["0","1","2","3","4","5","6","7","8","9"],
                        margin={ "top": 40, "right": 80, "bottom": 80, "left": 80 },
                        innerRadius=0.5,
                        padAngle=0.7,
                        cornerRadius=3,
                        activeOuterRadiusOffset=8,
                        borderWidth=1,
                        borderColor = {
                            'from' : "DATA",
                            "modifiers": [
                                [
                                    "darker",
                                    0.2
                                ]
                            ]
                        },
                        arcLinkLabelsSkipAngle=10,
                        arcLinkLabelsTextColor="#fff",
                        arcLinkLabelsThickness=5,
                        arcLinkLabelsColor={ "from": 'color' },
                        arcLabelsSkipAngle=2,
                        arcLabelsTextColor={
                        "from": 'color',
                        "modifiers": [
                            [
                                'darker',
                                2
                            ]
                        ]
                        },
                        defs = [
                        {
                            "id": "dots",
                            "type": "patternDots",
                            "background": "inherit",
                            "color": "#FFFFFF4D",
                            "size": 4,
                            "padding": 2,
                            "stagger": "true"
                        },
                        {
                            "id": "lines",
                            "type": "patternLines",
                            "background": "inherit",
                            "color": "rgba(255, 255, 255, 0.3)",
                            "rotation": -45,
                            "lineWidth": 6,
                            "spacing": 10
                        }
                        ],

                    fill = [
                        {
                            "match": {
                                "id": "0"
                            },
                            "id": "dots"
                        },
                        {
                            "match": {
                                "id": "1"
                            },
                            "id": "lines"
                        }
                    ],
                    legends=[
                                {
                                    "anchor": 'bottom',
                                    "direction": 'row',
                                    # "justify": "false",
                                    "translateX": 1,
                                    "translateY": 76,
                                    "itemsSpacing": 10,
                                    "itemWidth": 40,
                                    "itemHeight": 18,
                                    "itemTextColor": '#999',
                                    "itemDirection": 'left-to-right',
                                    "itemOpacity": 2,
                                    "symbolSize": 10,
                                    "symbolShape": 'circle',
                                    "effects": [
                                        {
                                            "on": 'hover',
                                            "style": {
                                                "itemTextColor": '#fff'
                                            }
                                        }
                                    ]
                                }
                            ],
                            theme={
                            "background": "#0e1016",
                            "textColor": "#fff",
                            "tooltip": {
                                "container": {
                                    "background": "#111",
                                    "color": "#fff",
                                }
                            }
                        }
                    )
# Hide the "Made with Streamlit" footer
# Define a CSS style for the text
hide_streamlit_style="""
    <style>
    #MainMenu{visibility:hidden;}
    footer{visibility:hidden;}
    h1 {
        color: #01FFB3 ;
    }
    h2 {
        color: darkorange;
    }
    h3 {
        color: red;
        # color: #12FFE2;
    }
    /* The progress bars */
        .stProgress > div > div > div > div {
            background: linear-gradient(to right, #00EEFF, #01FFB3);
            border-radius: 10px;
        }
        /* The text inside the progress bars */
        .stProgress > div > div > div > div > div {
            color: white;
        }
    </style>
    """
st.markdown(hide_streamlit_style,unsafe_allow_html=True)

lottie_file1 =load_lottie_file('./assets/GD.json')
lottie_file2 =load_lottie_file('./assets/GDSC.json')
lottie_file3 =load_lottie_file('./assets/GLoading.json')

with st.sidebar:
    st_lottie(lottie_file2,speed=0.5,reverse=False,height=100,width=260)
    # tabs = on_hover_tabs(tabName=['Dashboard','Cloud Foundations','GenAI'], 
    tabs = on_hover_tabs(tabName=['Dashboard'], 
                         iconName=['bar_chart_4_bars', 'cloud','sports_esports'], default_choice=0,
                         styles = {'navtab': {'background-color':'#272731',
                                                  'color': '#818181',
                                                  'font-size': '18px',
                                                  'transition': '.3s',
                                                  'white-space': 'nowrap',
                                                  'text-transform': 'uppercase'},
                                    'tabOptionsStyle': {':hover :hover': {'color': 'red',
                                                                      'cursor': 'pointer'}},              
                                                  
                                                  },
                        
                         )
# 'color': '#818181',

if tabs =='Dashboard':
    c1,c2= st.columns([0.3,1.2])
    with c2:
        st.title(":blue[G]:green[D]:orange[S]:red[C]   :blue[M]:green[C]:orange[E]:red[T] GCSJ :orange[Dashboard] : :red[2023]",anchor=False)
        # Get today's date

    desired_timezone = pytz.timezone('Asia/Kolkata')

    # Get the current time in the desired timezone
    current_time = datetime.datetime.now(desired_timezone)

    # Extract the date
    today = current_time.date()


    # Format and print today's date in a custom format (e.g., DD/MM/YYYY)
    formatted_date = today.strftime("%d/%m/%Y")
    st.header(formatted_date)
    # file = st.file_uploader("Upload The Results csv file",type='csv')
    # url = "https://docs.google.com/spreadsheets/d/1JDy9md2VZPz4JbYtRPJLs81_3jUK47nx6GYQjgU8qNY/edit?usp=sharing"
    url = "https://docs.google.com/spreadsheets/d/1OQEZzqf0tl5xrRAg0QQkBwI3ylXNlrAqIG5cMmD8VyE/edit?usp=sharing"
    conn = st.experimental_connection("gsheets", type=GSheetsConnection)
    file = conn.read(spreadsheet=url, usecols=[0, 1,2,3,4,5,6,7,8,9,10])
    # st.dataframe(file)
    # file = "./assets/MCET11.csv"
    # file = st.file_uploader("Upload The Results csv file",type='csv')
    if file is not None:
        # Df = pd.read_csv(file)
        Df = file
        
        # Count the number of "Yes" and "No" values in the "Redemption Status" column
        Ryes_count = (Df['Redemption Status'] == 'Yes').sum()
        Rno_count = (Df['Redemption Status'] == 'No').sum()
        Df = Df[Df['Redemption Status'] != 'No']
        Tyes_count = (Df['Total Completions of both Pathways'] == 'Yes').sum()
        Tno_count = (Df['Total Completions of both Pathways'] == 'No').sum()
        # Calculate the frequency of values in '# of Courses Completed'
        courses_completed_frequency = Df['# of Courses Completed'].value_counts()
        # Calculate the frequency of values in '# of Skill Badges Completed'
        skill_badges_completed_frequency = Df['# of Skill Badges Completed'].value_counts()
        for i in range(0,5):
            if i not in skill_badges_completed_frequency:
                skill_badges_completed_frequency[i] = 0
        # st.dataframe(skill_badges_completed_frequency)
        # st.error(len(skill_badges_completed_frequency))
        # st.error(skill_badges_completed_frequency[4])

        # Calculate the frequency of values in '# of GenAI Game Completed'
        genai_game_completed_frequency = Df['# of GenAI Game Completed'].value_counts()
        for i in range(0,10):
            if i not in genai_game_completed_frequency:
                genai_game_completed_frequency[i] = 0
        # st.error(genai_game_completed_frequency)
        # print(Df.head())
        # st.write(f'Number of "Yes" values: {Ryes_count}')
        # st.write(f'Number of "No" values: {Rno_count}')
        # st.dataframe(Df)
        # st.write(Df.columns)

    # if file is not None:
        # Df = pd.read_csv(file, index_col=None, encoding='utf-8')

        #  # Print the counts 
        # st.dataframe(Df)
    st.divider()
    listTabs = [
    '$$\color{skyblue}\\text{Leader Board}$$',
    '$$\color{orange}\\text{Progress Tracker}$$',
    '$$\color{red}\\text{Participant Progress}$$',
    '$$\color{LimeGreen}\\text{Redemption}$$',
    ]
    whitespace = 5
    # tab1,tab2,tab3,tab4 = st.tabs(['$$\color{skyblue}\\text{Leader Board}$$','$$\color{LimeGreen}\\text{Redemption}$$','$$\color{orange}\\text{Total Completions of both Pathways}$$','$$\color{red}\\text{Participant Progress}$$'])
    tab_labels = [s.center(len(s) + whitespace, "\u2001") for s in listTabs]
    tab = st.tabs(tab_labels)
    #----
    with tab[3]:
        st.markdown(
        f'<h1 style="font-family: your-font-family; color: limegreen;">Redemption Status</h1>',
        unsafe_allow_html=True
        )
        if file is not None:
            pieChart("Redemption Status",Ryes_count,Rno_count)
        st.divider()
    with tab[1]:

        c9,c10 = st.columns([0.5,0.5])
        c11,c12 = st.columns([0.5,0.5])
        with c9:
            st.markdown(
            f'<h3 style="font-family: your-font-family; color:orange">Course Badges Obtained /4 </h3>',
                unsafe_allow_html=True
            )
            pieChart4("Courses Completed",courses_completed_frequency)
            st.divider()
        with c10:
            st.markdown(
            f'<h3 style="font-family: your-font-family; color:orange">Skill Badges Obtained /4</h3>',
                unsafe_allow_html=True
            )
            pieChart4("Skill Badges Obtained",skill_badges_completed_frequency)
            # pieChart3("Skill Badges Obtained",genai_game_completed_frequency)

            st.divider()
        with c11:
            st.markdown(
            f'<h3 style="font-family: your-font-family; color:orange">GenAI Game Progress</h3>',
                unsafe_allow_html=True
            )
            pieChart9("GenAI Game Progress",genai_game_completed_frequency)

            st.divider()

        with c12 :
            st.markdown(
            f'<h3 style="font-family: your-font-family; color:orange">Total Completions of both Pathways</h3>',
                unsafe_allow_html=True
            )
            if file is not None:
                pieChart("Total Completions of both Pathways",Tyes_count,Tno_count)
            st.divider()

    #---------------------
    with tab[0]:
        st.markdown(
           f'<h1 style="font-family: your-font-family; color: skyblue;">Leader board</h1>',
            unsafe_allow_html=True
        )
        if file is not None :
            # st.dataframe(Df)
            Df["Score"] =  Df['# of Courses Completed'] +  Df['# of Skill Badges Completed'] +  Df['# of GenAI Game Completed']
            Df["Rank"] = Df["Score"].rank(method="dense" ,ascending=False)
            Df["Rank"] =  Df["Rank"].astype("int64")
            names = Df['Student Name'].tolist()

            # st.warning(len(names))
            # st.markdown(names)
            # st.warning(Df.columns)

            Df = Df.sort_values("Score",ascending=False,ignore_index=True)
            # st.dataframe(Df)
            Ndf = Df[["Student Name","# of Courses Completed","# of GenAI Game Completed","# of Skill Badges Completed","Rank"]].copy()
            condition = ~(Ndf[["# of Courses Completed", "# of GenAI Game Completed", "# of Skill Badges Completed"]] == 0).all(axis=1)

            # Apply the condition to filter rows
            Ndf = Ndf.loc[condition]
            Ndf.index = Ndf['Rank'].values
            st.dataframe(Ndf[["Student Name","# of Courses Completed","# of Skill Badges Completed","# of GenAI Game Completed"]].head(10),use_container_width=True)
            st.divider()
    #-------------------
    with tab[2]:
        st.markdown(
        f'<h3 style="font-family: your-font-family; color: OrangeRed;">If you are a participant then enter Your Name To know your progress :</h3>',
        unsafe_allow_html=True
        )       
        student_name = st.text_input("Enter Your Name")
        # Filter the DataFrame based on partial matches to the 'Student Name' column
        if student_name !="" :
            filtered_df = Df[Df['Student Name'].str.contains(student_name, case=False, na=False)]
            # Check if any matches were found
            if not filtered_df.empty:
                st.markdown("## :orange[Matching records found:]")
                st.dataframe(filtered_df[['Rank','Student Name', '# of Courses Completed', '# of Skill Badges Completed', '# of GenAI Game Completed', 'Total Completions of both Pathways', 'Redemption Status']],use_container_width=True,hide_index=True)
            else:
                st.markdown(
                        f'<h2 style="font-family: your-font-family; color: skyblue;">No Matching Record Found ! 😕</h2>',
                            unsafe_allow_html=True
                        )
if tabs =='GenAI':
    c1,c2= st.columns([0.4,1.2])

    with c2:    
        st.title(":orange[Generative] :red[AI] Arcade :blue[Game]")
        subheadingtext(f"⚠️ Stay tuned! This event starts on {':orange[16 October]'}")
    c3,c4= st.columns([0.5,1.2])
    with c4:
        st_lottie(lottie_file3,speed=0.5,reverse=False,height=110,width=350)
if tabs =='Cloud Foundations':
    c1,c2= st.columns([0.2,1.2])
    with c2:
        st.title(":red[Google] :blue[Cloud] Computing :orange[Foundations]")
    st.divider()
    # Create an expandable section
    with st.expander("Click to toggle"):
        st.markdown("""
    ## 1. Cloud Computing Fundamentals :
    - ### Create and Manage Cloud Resources
    ## 2. Infrastructure in Google Cloud :
    - ### Perform Foundational Infrastructure Tasks in Google Cloud
    ## 3. Networking & Security in Google Cloud :
    - ### Build and Secure Networks in Google Cloud
    ## 4. Data, ML, and AI in Google Cloud :
    - ### Perform Foundational Data, ML, and AI Tasks in Google Cloud
    """)
with c1: 
    st_lottie(lottie_file1,speed=0.5,reverse=False,height=150,width=300)

# Filter the DataFrame to get students with 'Redemption Status' equal to 'No'
# filtered_df = Df[Df['Redemption Status'] == 'No']

# Extract the 'Student Name' and 'Student Email' columns from the filtered DataFrame
# result = filtered_df[['Student Name', 'Student Email']]

# st.dataframe(result,use_container_width=True)
# st.warning(result.shape)
# st.warning(Df['Institution'].unique())



