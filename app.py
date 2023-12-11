import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    st.title('Data Visualization and Analysis App')

    file_path = "data.xlsx"
    
    if file_path:
        try:
            data = pd.read_excel(file_path)
            st.write("Data from Excel file:")
        except Exception as e:
            st.error(f"Error reading file: {e}")
            return

        if st.checkbox("Filter Data"):
            columns_to_filter = st.multiselect("Select columns to filter", data.columns)
            for col in columns_to_filter:
                unique_values = data[col].unique()
                selected_value = st.selectbox(f"Filter by {col}", unique_values)
                data = data[data[col] == selected_value]

        if st.checkbox("Show Data / Filtred Data"):
            st.write(data)

        if st.checkbox("Visualize Data / Filtred Data"):
            chart_type = st.selectbox("Select Chart Type", ["Bar Chart", "Pie Chart", "Area Chart", "Line Chart"])

            st.subheader("Column Selection for Visualization")
            columns_to_plot = st.multiselect("Select columns to plot", data.columns)

            if len(columns_to_plot) > 1:
                st.warning("Please select only one column for visualization. If u want to add more u can use filter data.")
            elif columns_to_plot:
                col = columns_to_plot[0]
                st.subheader(f"Chart for {col}")
                if chart_type == "Bar Chart":
                    counts = data[col].value_counts()
                    st.bar_chart(counts)
                elif chart_type == "Pie Chart":
                    counts = data[col].value_counts()
                    fig, ax = plt.subplots()
                    ax.pie(counts, labels=counts.index, autopct='%1.1f%%')
                    st.pyplot(fig)
                elif chart_type == "Area Chart":
                    st.area_chart(data[col].value_counts())
                elif chart_type == "Line Chart":
                    st.line_chart(data[col].value_counts())

        if st.button("Download Data / Filtred Data"):
            st.download_button(label='Download Data as CSV', data=data.to_csv(index=False), file_name='processed_data.csv', mime='text/csv')

if __name__ == "__main__":
    main()
