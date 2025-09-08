import streamlit as st
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title='E-commerce Analytics Dashboard',
    page_icon='📊',
    layout='wide'
)

# Title and introduction
st.title('📊 E-commerce Analytics Dashboard')
st.markdown("""
This dashboard presents various insights from our e-commerce data analysis including:
- Price distributions
- Category analysis
- Rating patterns
- Clustering analysis
""")

# Sidebar for navigation
analysis_type = st.sidebar.selectbox(
    "Choose Analysis Type",
    ["Price Analysis", "Category Analysis", "Ratings Analysis", "Clustering Analysis"]
)

# Function to get image path
def get_image_path(image_name):
    base_path = Path(__file__).parent / 'Images'
    return str(base_path / image_name)

if analysis_type == "Price Analysis":
    st.header("Price Distribution Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(get_image_path("price_distribution.png"), 
                caption="Overall Price Distribution",
                use_column_width=True)
        
    with col2:
        st.image(get_image_path("correlation_matrix.png"), 
                caption="Correlation Matrix",
                use_column_width=True)

elif analysis_type == "Category Analysis":
    st.header("Category-Based Analysis")
    
    view_option = st.radio(
        "Select View",
        ["Category Distribution", "Price Distribution", "3D Analysis"]
    )
    
    if view_option == "Category Distribution":
        st.image(get_image_path("product_distribution_main_category.png"),
                caption="Product Distribution by Main Category",
                use_column_width=True)
    
    elif view_option == "Price Distribution":
        col1, col2 = st.columns(2)
        with col1:
            st.image(get_image_path("category_price_distribution.png"),
                    caption="Price Distribution by Category",
                    use_column_width=True)
        with col2:
            st.image(get_image_path("main_category_price_distribution.png"),
                    caption="Price Distribution by Main Category",
                    use_column_width=True)
    
    else:
        st.image(get_image_path("main_category_3d_scatter.png"),
                caption="3D Scatter Plot by Main Category",
                use_column_width=True)

elif analysis_type == "Ratings Analysis":
    st.header("Ratings Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(get_image_path("rating_count_by_average_rating.png"),
                caption="Rating Count Distribution",
                use_column_width=True)
    
    with col2:
        st.image(get_image_path("ratings_vs_discount_percentage.png"),
                caption="Ratings vs Discount Percentage",
                use_column_width=True)

else:  # Clustering Analysis
    st.header("KMeans Clustering Analysis")
    
    cluster_option = st.selectbox(
        "Select Clustering View",
        ["Cluster Set 1", "Cluster Set 2", "Cluster Set 3"]
    )
    
    col1, col2 = st.columns(2)
    
    if cluster_option == "Cluster Set 1":
        with col1:
            st.image(get_image_path("Kmeans/3d_clusters_kmeans_1.png"),
                    caption="3D Clusters - Set 1",
                    use_column_width=True)
        with col2:
            st.image(get_image_path("Kmeans/elbow_method_kmeans_1.png"),
                    caption="Elbow Method - Set 1",
                    use_column_width=True)
    
    elif cluster_option == "Cluster Set 2":
        with col1:
            st.image(get_image_path("Kmeans/3d_clusters_kmeans_2.png"),
                    caption="3D Clusters - Set 2",
                    use_column_width=True)
        with col2:
            st.image(get_image_path("Kmeans/elbow_method_kmeans_2.png"),
                    caption="Elbow Method - Set 2",
                    use_column_width=True)
    
    else:
        with col1:
            st.image(get_image_path("Kmeans/3d_clusters_kmeans_3.png"),
                    caption="3D Clusters - Set 3",
                    use_column_width=True)
        with col2:
            st.image(get_image_path("Kmeans/elbow_method_kmeans_3.png"),
                    caption="Elbow Method - Set 3",
                    use_column_width=True)

# Add footer
st.markdown("---")
st.markdown("### 📝 Note")
st.markdown("""
This dashboard visualizes various aspects of our e-commerce dataset including price distributions,
category analysis, rating patterns, and clustering results. Use the sidebar to navigate between
different types of analysis.
""")