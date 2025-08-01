import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="MLB Home Run Predictor", layout="wide")

st.title("🔥 MLB Home Run Predictions – Hot Shot Props")
st.markdown("Daily live predictions for home run props, updated at 11AM EST")

# Load sample or real predictions
try:
    df = pd.read_csv('predictions.csv')
except FileNotFoundError:
    st.warning("Prediction data not found. Please run the prediction script or upload a CSV.")
    df = pd.DataFrame()

# Display full data if available
if not df.empty:
    st.dataframe(df)

    # Download button for CSV
    csv = df.to_csv(index=False).encode()
    st.download_button("📥 Download CSV", csv, "home_run_predictions.csv", "text/csv")

    # Edge-based filtering
    edge_cutoff = st.slider("Minimum Model Edge (%)", 0, 100, 10)
    filtered_df = df[df['model_edge'] > edge_cutoff]

    st.subheader("📈 Top Value Plays")
    st.dataframe(filtered_df)
else:
    st.info("Awaiting prediction data...")

# Optional: Upload manual CSV if needed
uploaded_file = st.file_uploader("Or upload your own predictions.csv", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)  # Show uploaded data
    csv = df.to_csv(index=False).encode()
    st.download_button("📥 Download Uploaded CSV", csv, "home_run_predictions.csv", "text/csv")
