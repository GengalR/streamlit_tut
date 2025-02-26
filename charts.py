import streamlit as st
import plotly.express as px

def show():
    st.subheader("📈 Interactive Chart")
    iris = px.data.iris()

    # --- 7. PLOTS & INTERACTIVITY ---
    # Scatter Plot with user-selected axes
    st.write("### Scatter Plot: Choose X and Y")
    x_axis = st.selectbox("Choose X-axis:", iris.columns[:-1], index=2)
    y_axis = st.selectbox("Choose Y-axis:", iris.columns[:-1], index=3)
    fig_scatter = px.scatter(iris, x=x_axis, y=y_axis, color="species", title=f"{x_axis} vs {y_axis}")
    st.plotly_chart(fig_scatter)

    # Histogram with adjustable bin size
    st.write("### Distribution of Selected Feature")
    hist_feature = st.selectbox("Choose feature for histogram:", iris.columns[:-1], index=2)
    bin_size = st.slider("Select number of bins:", 5, 50, 20)
    fig_hist = px.histogram(iris, x=hist_feature, color="species", nbins=bin_size, title=f"Distribution of {hist_feature} by Species")
    st.plotly_chart(fig_hist)

    # Box Plot with selectable feature
    st.write("### Box Plot of Selected Feature by Species")
    box_feature = st.selectbox("Choose feature for box plot:", iris.columns[:-1], index=3)
    fig_box = px.box(iris, x="species", y=box_feature, color="species", title=f"Box Plot of {box_feature} by Species")
    st.plotly_chart(fig_box)

    # Pair Plot (Scatter Matrix)
    st.write("### Pair Plot of All Features")
    fig_matrix = px.scatter_matrix(iris, dimensions=["sepal_length", "sepal_width", "petal_length", "petal_width"], color="species", title="Pair Plot of Iris Features")
    st.plotly_chart(fig_matrix)
