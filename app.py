import streamlit as st
import pandas as pd
import plotly.express as px
from Experiments import Benchmarking

st.set_page_config(page_title="Sorting Benchmark", page_icon="📊", layout="wide")

st.title("📊 Sorting Algorithm Benchmark")
st.markdown("Upload a CSV file and benchmark different sorting algorithms")

# File upload
uploaded_file = st.file_uploader("Upload CSV File", type=['csv'])

if uploaded_file:
    # Read CSV
    df = pd.read_csv(uploaded_file)
    st.success(f"File uploaded! Rows: {len(df)}, Columns: {len(df.columns)}")
    
    # Show preview
    with st.expander("Preview Data"):
        st.dataframe(df.head())
    
    # Select column
    numeric_cols = df.select_dtypes(include=['number']).columns.tolist()
    
    if not numeric_cols:
        st.error("No numeric columns found!")
        st.stop()
    
    col = st.selectbox("Select column to sort:", numeric_cols)
    
    # Get data
    data = df[col].dropna().tolist()
    
    st.metric("Total Elements", len(data))
    
    # Run benchmark
    if st.button("Run Benchmark", type="primary"):
        with st.spinner("Running benchmarks..."):
            benchmark = Benchmarking(data)
            results = benchmark.run_all_benchmarks()
        
        st.success("Benchmark complete!")
        
        # Show results table
        st.subheader("Results")
        results_df = pd.DataFrame([
            {'Algorithm': name, 'Time (seconds)': f"{time:.6f}"}
            for name, time in sorted(results.items(), key=lambda x: x[1])
        ])
        st.dataframe(results_df, use_container_width=True, hide_index=True)
        
        # Winner
        winner = min(results.items(), key=lambda x: x[1])
        st.success(f"🏆 Fastest: {winner[0]} ({winner[1]:.6f}s)")
        
        # Bar chart
        fig = px.bar(
            x=list(results.keys()),
            y=list(results.values()),
            labels={'x': 'Algorithm', 'y': 'Time (seconds)'},
            title='Execution Time Comparison'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Download button
        csv = results_df.to_csv(index=False)
        st.download_button("Download Results", csv, "results.csv", "text/csv")

else:
    st.info("Upload a CSV file to start")