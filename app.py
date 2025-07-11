import streamlit as st
import pandas as pd
from datetime import datetime

st.title("🧹 Local Sales ETL Interface")

uploaded_file = st.file_uploader("📤 Upload a CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("📄 Original Data", df.head())

    filtered = df[df["sales"] > 600]
    st.write(f"✅ Filtered {len(filtered)} of {len(df)} rows with sales > 600")
    st.dataframe(filtered)

    if st.button("💾 Save filtered CSV"):
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        filtered.to_csv(f"output/filtered_ui_{ts}.csv", index=False)
        st.success(f"Saved to output/filtered_ui_{ts}.csv")
