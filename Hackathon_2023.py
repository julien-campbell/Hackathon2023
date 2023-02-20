# Hackathon Project 2023 
# Created by: Julien Campbell, Seth Campbell, James Hwang, Kyle Wu
#
# Code sources/references/inspiration from:
# https://towardsdatascience.com/how-to-step-up-your-folium-choropleth-map-skills-17cf6de7c6fe
# https://realpython.com/python-folium-web-maps-from-data/
# https://python-visualization.github.io/folium/quickstart.html#Markers
#
# Source Data from:
# https://campd.epa.gov/data/custom-data-download


from branca.element import Template, MacroElement
import pandas as pd
import folium 
from folium.plugins import StripePattern
from folium import IFrame
import geopandas as gpd
import numpy as np
import webbrowser
import base64

df = pd.read_csv("State-Avgs.csv")

df = df[["CO2 Avg","popup_image"]]
url = ("https://raw.githubusercontent.com/python-visualization/folium/master/examples/data")
state_geo = f"{url}/us-states.json"

geoJSON_df = gpd.read_file(state_geo)
geoJSON_df = geoJSON_df.rename(columns = {"id":"state"})
geoJSON_df["CO2 Avg"] = df["CO2 Avg"]
geoJSON_df["popup_image"] = df["popup_image"]
print(geoJSON_df.head(51))

sample_map = folium.Map(location=[40.19855235180509, -96.48253075757617], zoom_start=5, tiles="cartodb positron")

folium.Choropleth(
    geo_data=geoJSON_df,
    data=geoJSON_df,
    columns=['state',"CO2 Avg"],
    key_on="feature.properties.state",
    fill_color='YlGnBu',
    fill_opacity=1,
    line_opacity=0.5,
    legend_name="CO2 Avg",
    smooth_factor=0,
    Highlight= True,
    line_color = "#0000",
    name = "CO2 Avg",
    show=False,
    overlay=True,
    nan_fill_color = "White"
).add_to(sample_map)

folium.Choropleth(
    geo_data=geoJSON_df,
    data=geoJSON_df,
    columns=['state',"CO2 Avg"],
    key_on="feature.properties.state",
    fill_color='RdBu_r',
    fill_opacity=1,
    line_opacity=0.5,
    legend_name="CO2 Avg",
    smooth_factor=0,
    Highlight= True,
    line_color = "#0000",
    name = "Colorblind",
    show=False,
    overlay=True,
    nan_fill_color = "White"
).add_to(sample_map)

encoded = base64.b64encode(open("AK_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
AK_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("AR_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
AR_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("AZ_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
AZ_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("CA_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
CA_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("CO_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
CO_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("CT_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
CT_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("DC_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
DC_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("DE_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
DE_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("FL_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
FL_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("GA_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
GA_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("HI_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
HI_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("IA_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
IA_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("ID_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
ID_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("IL_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
IL_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("IN_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
IN_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("KS_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
KS_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("KY_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
KY_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("LA_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
LA_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("MA_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
MA_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("MD_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
MD_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("ME_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
ME_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("MI_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
MI_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("MN_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
MN_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("MO_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
MO_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("MS_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
MS_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("MT_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
MT_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("NC_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
NC_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("ND_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
ND_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("NE_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
NE_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("NH_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
NH_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("NJ_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
NJ_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("NM_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
NM_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("NV_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
NV_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("NY_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
NY_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("OH_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
OH_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("OK_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
OK_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("OR_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
OR_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("PA_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
PA_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("RI_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
RI_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("SC_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
SC_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("SD_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
SD_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("TN_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
TN_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("TX_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
TX_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("UT_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
UT_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("VA_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
VA_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("VT_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
VT_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("WA_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
WA_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("WI_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
WI_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("WV_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
WV_pop = folium.Popup(iframe, max_width=800, max_height=800)

encoded = base64.b64encode(open("WY_emissions.png", 'rb').read())
html = '<img src="data:image/png;base64,{}">'.format
iframe = IFrame(html(encoded.decode('UTF-8')), width=1100, height=700)
WY_pop = folium.Popup(iframe, max_width=800, max_height=800)

folium.Marker(
    location=[65.34634046362916, -151.64924525273085],
    popup=AK_pop,
).add_to(sample_map)

folium.Marker(
    location=[34.87311401262829, -92.51257413594553],
    popup=AR_pop,
).add_to(sample_map)

folium.Marker(
    location=[34.57234962327487, -111.4952293872549],
    popup=AZ_pop,
).add_to(sample_map)

folium.Marker(
    location=[36.286704163135845, -118.63087810822904],
    popup=CA_pop,
).add_to(sample_map)

folium.Marker(
    location=[39.03808261285209, -105.32014876333497],
    popup=CO_pop,
).add_to(sample_map)

folium.Marker(
    location=[41.618003175881334, -72.75231613940177],
    popup=CT_pop,
).add_to(sample_map)

folium.Marker(
    location=[38.824589896545774, -77.05200190716823],
    popup=DC_pop,
).add_to(sample_map)

folium.Marker(
    location=[39.00254512725318, -75.49679641669951],
    popup=DE_pop,
).add_to(sample_map)

folium.Marker(
    location=[28.334493522034947, -81.62613570266447],
    popup=FL_pop,
).add_to(sample_map)

folium.Marker(
    location=[32.62950028295758, -83.54727189677288],
    popup=GA_pop,
).add_to(sample_map)

folium.Marker(
    location=[21.33153317807552, -157.9409842929646],
    popup=HI_pop,
).add_to(sample_map)

folium.Marker(
    location=[42.00890821191964, -93.50877891290712],
    popup=IA_pop,
).add_to(sample_map)

folium.Marker(
    location=[44.063005035945444, -114.7827283335059],
    popup=ID_pop,
).add_to(sample_map)

folium.Marker(
    location=[40.55232417853693, -89.24429702449551],
    popup=IL_pop,
).add_to(sample_map)

folium.Marker(
    location=[40.2571123774166, -86.14285565110525],
    popup=IN_pop,
).add_to(sample_map)

folium.Marker(
    location=[38.76169725477919, -98.11248095153327],
    popup=KS_pop,
).add_to(sample_map)

folium.Marker(
    location=[37.65748443218669, -84.64059498586936],
    popup=KY_pop,
).add_to(sample_map)

folium.Marker(
    location=[31.39541650657282, -92.44265844080422],
    popup=LA_pop,
).add_to(sample_map)

folium.Marker(
    location=[42.33215237167671, -72.28328951376756],
    popup=MA_pop,
).add_to(sample_map)

folium.Marker(
    location=[39.21369921740206, -76.74161148801605],
    popup=MD_pop,
).add_to(sample_map)

folium.Marker(
    location=[45.13264799660933, -69.23030816183652],
    popup=ME_pop,
).add_to(sample_map)

folium.Marker(
    location=[43.9584463209743, -84.64059498586936],
    popup=MI_pop,
).add_to(sample_map)

folium.Marker(
    location=[46.31664300240644, -94.91411953522456],
    popup=MN_pop,
).add_to(sample_map)

folium.Marker(
    location=[38.382827526934285, -92.58803850518187],
    popup=MO_pop,
).add_to(sample_map)

folium.Marker(
    location=[32.87264801970132, -89.48659713179164],
    popup=MS_pop,
).add_to(sample_map)

folium.Marker(
    location=[47.114029971136524, -109.35520593007296],
    popup=MT_pop,
).add_to(sample_map)

folium.Marker(
    location=[35.75396195697446, -78.87385243222184],
    popup=NC_pop,
).add_to(sample_map)

folium.Marker(
    location=[47.63908006326148, -100.58394204595363],
    popup=ND_pop,
).add_to(sample_map)

folium.Marker(
    location=[41.53908594556418, -99.37244150947306],
    popup=NE_pop,
).add_to(sample_map)

folium.Marker(
    location=[43.43288851786029, -71.70176925625688],
    popup=NH_pop,
).add_to(sample_map)

folium.Marker(
    location=[40.071947935494705, -74.12477032921801],
    popup=NJ_pop,
).add_to(sample_map)

folium.Marker(
    location=[34.56544961129399, -106.05992447084581],
    popup=NM_pop,
).add_to(sample_map)

folium.Marker(
    location=[39.96060694321065, -116.96342929917093],
    popup=NV_pop,
).add_to(sample_map)

folium.Marker(
    location=[43.00912716417006, -75.72395103737236],
    popup=NY_pop,
).add_to(sample_map)

folium.Marker(
    location=[40.62592474243745, -82.84757419187812],
    popup=OH_pop,
).add_to(sample_map)

folium.Marker(
    location=[35.75396195697446, -96.94944043651192],
    popup=OK_pop,
).add_to(sample_map)

folium.Marker(
    location=[43.81874798736374, -120.5494708871534],
    popup=OR_pop,
).add_to(sample_map)

folium.Marker(
    location=[40.84624018775671, -77.85619198157816],
    popup=PA_pop,
).add_to(sample_map)


folium.Marker(
    location=[41.57534826867831, -71.60484921333844],
    popup=RI_pop,
).add_to(sample_map)

folium.Marker(
    location=[33.76351782644945, -80.66687322621308],
    popup=SC_pop,
).add_to(sample_map)

folium.Marker(
    location=[44.58303310323222, -100.0508818099022],
    popup=SD_pop,
).add_to(sample_map)

folium.Marker(
    location=[35.871855258756405, -86.2397756940237],
    popup=TN_pop,
).add_to(sample_map)

folium.Marker(
    location=[31.643278609870546, -98.93630131634006],
    popup=TX_pop,
).add_to(sample_map)

folium.Marker(
    location=[39.21369921740206, -111.48744687427876],
    popup=UT_pop,
).add_to(sample_map)

folium.Marker(
    location=[37.54230119261668, -78.05003206741506],
    popup=VA_pop,
).add_to(sample_map)

folium.Marker(
    location=[44.13260843505065, -72.62250966398211],
    popup=VT_pop,
).add_to(sample_map)

folium.Marker(
    location=[47.47556348170693, -120.21025073693885],
    popup=WA_pop,
).add_to(sample_map)

folium.Marker(
    location=[44.78975347605253, -89.63197719616929],
    popup=WI_pop,
).add_to(sample_map)

folium.Marker(
    location=[38.68608319486367, -80.66687322621308],
    popup=WV_pop,
).add_to(sample_map)

folium.Marker(
    location=[43.07995857357123, -107.46526509316327],
    popup=WY_pop,
).add_to(sample_map)

folium.LayerControl(collapsed=False).add_to(sample_map)

style_function = lambda x: {'fillColor': '#ffffff', 
                            'color':'#000000', 
                            'fillOpacity': 0.1, 
                            'weight': 0.1}
highlight_function = lambda x: {'fillColor': '#000000', 
                                'color':'#000000', 
                                'fillOpacity': 0.50, 
                                'weight': 0.1}
NIL = folium.features.GeoJson(
    data = geoJSON_df,
    style_function=style_function, 
    control=False,
    highlight_function=highlight_function,
    popup=folium.features.GeoJsonPopup(['popup_image']),
    tooltip=folium.features.GeoJsonTooltip(
        fields=['state','CO2 Avg'],
        aliases=['state','CO2 Avg'],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;") 
    )
)

sample_map.add_child(NIL)
sample_map.keep_in_front(NIL)

sample_map.save("map.html")
webbrowser.open_new_tab('map.html')

