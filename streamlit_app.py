import streamlit as st
import altair as alt
import pandas as pd

st.title("What's My Prescription, Doc?")
# Subtitle with smaller font and info icon + note
st.markdown("""
### Antibiotic effectiveness varies based on the bacteria Genus  
<span style="font-size:18px; font-weight:bold;"></span> ℹ️ 
**What is MIC?** MIC is minimum inhibitory concentration - the lower the value, the more effective the antibiotic.
""", unsafe_allow_html=True)


data = [
  {
    "Bacteria":"Aerobacter aerogenes",
    "Penicillin":870,
    "Streptomycin":1,
    "Neomycin":1.6,
    "Gram_Staining":"negative",
    "Genus": "other"
  },
  {
    "Bacteria":"Bacillus anthracis",
    "Penicillin":0.001,
    "Streptomycin":0.01,
    "Neomycin":0.007,
    "Gram_Staining":"positive",
    "Genus": "other"
  },
  {
    "Bacteria":"Brucella abortus",
    "Penicillin":1,
    "Streptomycin":2,
    "Neomycin":0.02,
    "Gram_Staining":"negative",
    "Genus": "other"
  },
  {
    "Bacteria":"Diplococcus pneumoniae",
    "Penicillin":0.005,
    "Streptomycin":11,
    "Neomycin":10,
    "Gram_Staining":"positive",
    "Genus": "other"
  },
  {
    "Bacteria":"Escherichia coli",
    "Penicillin":100,
    "Streptomycin":0.4,
    "Neomycin":0.1,
    "Gram_Staining":"negative",
    "Genus": "other"
  },
  {
    "Bacteria":"Klebsiella pneumoniae",
    "Penicillin":850,
    "Streptomycin":1.2,
    "Neomycin":1,
    "Gram_Staining":"negative",
    "Genus": "other"
  },
  {
    "Bacteria":"Mycobacterium tuberculosis",
    "Penicillin":800,
    "Streptomycin":5,
    "Neomycin":2,
    "Gram_Staining":"negative",
    "Genus": "other"
  },
  {
    "Bacteria":"Proteus vulgaris",
    "Penicillin":3,
    "Streptomycin":0.1,
    "Neomycin":0.1,
    "Gram_Staining":"negative",
    "Genus": "other"
  },
  {
    "Bacteria":"Pseudomonas aeruginosa",
    "Penicillin":850,
    "Streptomycin":2,
    "Neomycin":0.4,
    "Gram_Staining":"negative",
    "Genus": "other"
  },
  {
    "Bacteria":"Salmonella (Eberthella) typhosa",
    "Penicillin":1,
    "Streptomycin":0.4,
    "Neomycin":0.008,
    "Gram_Staining":"negative",
    "Genus": "Salmonella"
  },
  {
    "Bacteria":"Salmonella schottmuelleri",
    "Penicillin":10,
    "Streptomycin":0.8,
    "Neomycin":0.09,
    "Gram_Staining":"negative",
    "Genus": "Salmonella"
  },
  {
    "Bacteria":"Staphylococcus albus",
    "Penicillin":0.007,
    "Streptomycin":0.1,
    "Neomycin":0.001,
    "Gram_Staining":"positive",
    "Genus": "Staphylococcus"
  },
  {
    "Bacteria":"Staphylococcus aureus",
    "Penicillin":0.03,
    "Streptomycin":0.03,
    "Neomycin":0.001,
    "Gram_Staining":"positive",
    "Genus": "Staphylococcus"
  },
  {
    "Bacteria":"Streptococcus fecalis",
    "Penicillin":1,
    "Streptomycin":1,
    "Neomycin":0.1,
    "Gram_Staining":"positive",
    "Genus": "Streptococcus"
  },
  {
    "Bacteria":"Streptococcus hemolyticus",
    "Penicillin":0.001,
    "Streptomycin":14,
    "Neomycin":10,
    "Gram_Staining":"positive",
    "Genus": "Streptococcus"
  },
  {
    "Bacteria":"Streptococcus viridans",
    "Penicillin":0.005,
    "Streptomycin":10,
    "Neomycin":40,
    "Gram_Staining":"positive",
    "Genus": "Streptococcus"
  }
]
df = pd.DataFrame(data)
df_long = df.melt(
    id_vars=['Bacteria', 'Genus', 'Gram_Staining'],
    value_vars=['Penicillin', 'Streptomycin', 'Neomycin'],
    var_name='Antibiotic',
    value_name='MIC'
)
dot_plot = alt.Chart(df_long).mark_circle(size=100, opacity=0.7).encode(
    alt.X('Antibiotic:N', title=None, axis=alt.Axis(labels=False, ticks=False)),
    alt.Y('MIC:Q', scale=alt.Scale(type='log'), title='MIC (log scale)'),
    alt.Color('Antibiotic:N', scale=alt.Scale(
        domain=['Penicillin', 'Streptomycin', 'Neomycin'],
        range=['#D95F02', '#6A994E', '#F2C14E']  # Rust, Olive, Gold
    ), title='Antibiotic'),
    tooltip=[
        alt.Tooltip('Bacteria:N'),
        alt.Tooltip('Genus:N'),
        alt.Tooltip('Gram_Staining:N'),
        alt.Tooltip('Antibiotic:N'),
        alt.Tooltip('MIC:Q')
    ]
).properties(
    width=150,
    height=300
).facet(
    column=alt.Column('Genus:N', header=alt.Header(labelAngle=0, labelOrient='bottom'))
).configure_view(
    stroke=None
).configure_axis(
    grid=False
)

dot_plot2 = alt.Chart(df_long).mark_circle(size=100, opacity=0.7).encode(
    alt.X('Antibiotic:N', title=None, axis=alt.Axis(labels=False, ticks=False)),
    alt.Y('MIC:Q', scale=alt.Scale(type='log', domain=[0.001, 2000]), title='MIC (log scale)'),
    alt.Color('Antibiotic:N',
        scale=alt.Scale(
            domain=['Penicillin', 'Streptomycin', 'Neomycin'],
            range=['#D95F02', '#6A994E', '#F2C14E']
        ),
        title='Antibiotic'
    ),
    tooltip=[
        alt.Tooltip('Bacteria:N'),
        alt.Tooltip('Genus:N'),
        alt.Tooltip('Gram_Staining:N'),
        alt.Tooltip('Antibiotic:N'),
        alt.Tooltip('MIC:Q')
    ]
).properties(
    width=150,
    height=300
).facet(
    column=alt.Column(
        'Genus:N',
        header=alt.Header(
            labelOrient='bottom',
            labelPadding=10,
            title=None
        )
    )
).configure_view(
    stroke=None
).configure_axis(
    grid=False
)

genus_order = df['Genus'].unique().tolist()

# Highlight rectangles
highlight_df = pd.DataFrame({
    'Genus': [genus_order[0], genus_order[1], genus_order[2]],
    'Antibiotic': ['Neomycin', 'Neomycin', 'Penicillin']
})

highlight = alt.Chart(highlight_df).mark_rect(
    fill='lightgray',
    opacity=0.3,
    stroke='black',
    strokeWidth=1
).encode(
    x=alt.X('Antibiotic:N'),
    y=alt.value(0),  # y-value not used for positioning; we span full chart
    y2=alt.value(1),
    facet=alt.Facet('Genus:N', columns=len(genus_order))
)

# Main dot plot
dot_plot3 = alt.Chart(df_long).mark_circle(size=100, opacity=0.7).encode(
    alt.X('Antibiotic:N', title=None, axis=alt.Axis(labels=False, ticks=False)),
    alt.Y('MIC:Q', scale=alt.Scale(type='log', domain=[0.001, 2000]), title='MIC (log scale)'),
    alt.Color('Antibiotic:N',
        scale=alt.Scale(
            domain=['Penicillin', 'Streptomycin', 'Neomycin'],
            range=['#D95F02', '#6A994E', '#F2C14E']
        ),
        title='Antibiotic'
    ),
    tooltip=[
        alt.Tooltip('Bacteria:N'),
        alt.Tooltip('Genus:N'),
        alt.Tooltip('Gram_Staining:N'),
        alt.Tooltip('Antibiotic:N'),
        alt.Tooltip('MIC:Q')
    ]
).properties(
    width=150,
    height=300
)

# Facet by Genus with better padding
facet = alt.Facet('Genus:N', columns=len(genus_order),
    header=alt.Header(labelOrient='bottom', labelPadding=10, title=None)
)



label_data = pd.DataFrame({
    'Genus': genus_order,
    'Label': [
        'Neomycin highlight',
        'Neomycin highlight',
        'Penicillin highlight',
        'Penicillin highlight'
    ],
    'Color': [
        '#F2C14E',
        '#F2C14E',
        '#D95F02',
        '#D95F02'
    ]
})

labels = alt.Chart(label_data).mark_text(
    align='center',
    fontSize=12,
    fontWeight='bold',
    dy=20  # Push text down below the plot
).encode(
    text='Label',
    color=alt.Color('Color:N', scale=None),
).facet(
    column=alt.Column('Genus:N', header=alt.Header(labelOrient='bottom', labelPadding=10, title=None))
)
main_plot = alt.Chart(df_long).mark_circle(size=100, opacity=0.7).encode(
    alt.X('Antibiotic:N', title=None, axis=alt.Axis(labels=False, ticks=False)),
    alt.Y('MIC:Q', scale=alt.Scale(type='log', domain=[0.001, 2000]), title='MIC (log scale)'),
    alt.Color('Antibiotic:N',
        scale=alt.Scale(
            domain=['Penicillin', 'Streptomycin', 'Neomycin'],
            range=['#D95F02', '#6A994E', '#F2C14E']
        ),
        title='Antibiotic'
    ),
    tooltip=[
        'Bacteria:N', 'Genus:N', 'Gram_Staining:N', 'Antibiotic:N', 'MIC:Q'
    ]
).properties(
    width=150,
    height=300
).facet(
    column=alt.Column('Genus:N', header=alt.Header(labelOrient='bottom', labelPadding=10, title=None))
)

# Combine vertically
final_chart = alt.vconcat(main_plot, labels).configure_view(stroke=None).configure_axis(grid=False)

st.altair_chart(main_plot, use_container_width=True)
# st.altair_chart(labels, use_container_width=True)