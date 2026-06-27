import streamlit as st
import pandas as pd

from main import main

SHEET_URL = "https://docs.google.com/spreadsheets/d/1wnOUrBaKVD1z03tzgc7MFpNVntzQ9XYoUOxor5ATJeI/edit"

st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Research Agent")

query = st.text_input(
    "Enter Research Query"
)

if st.button("Run Research"):

    if not query:
        st.warning("Please enter a research query.")

    else:

        st.info("Running research... Please wait.")

        try:

            main(query)

            df = pd.read_csv("data/results.csv")

            st.success("✅ Research completed successfully!")

            st.markdown(f"### 🎯 Found **{len(df)} AI startups**")

            st.success("📊 Results uploaded to Google Sheets.")

            st.link_button(
                "📊 Open Results in Google Sheets",
                SHEET_URL
            )

            st.divider()

            st.subheader("Preview")

            st.dataframe(
                df,
                width="stretch"
            )

        except Exception as e:

            st.error(f"Error: {e}")