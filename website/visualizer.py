import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
# GPS coordinates

df = pd.read_csv("../exif.csv")


df[["gps_latitude", "gps_longitude"]] = df[["gps_latitude", "gps_longitude"]].dropna()


df["lat"] = (
    df["gps_latitude"]
    .dropna()
    .apply(lambda x: [float(value) for value in x[1:-1].split(",")])
    .apply(lambda x: x[0] + x[1] / 60 + x[2] / 3600)
)
df["lon"] = (
    df["gps_longitude"]
    .dropna()
    .apply(lambda x: [float(value) for value in x[1:-1].split(",")])
    .apply(lambda x: x[0] + x[1] / 60 + x[2] / 3600)
)
df

st.map(
    df[["lat", "lon"]].dropna(),
    size=20,
)
