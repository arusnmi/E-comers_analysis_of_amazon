import streamlit as st
from pathlib import Path

# Page setup
st.set_page_config(page_title="E-commerce Data Analysis", page_icon="📊", layout="wide")

# Function to get image path
def get_image_path(image_name):
    base_path = Path(__file__).parent / 'Images'
    return str(base_path / image_name)

# Title and introduction
st.title("E-commerce Data Analysis Dashboard")
st.markdown("""
This dashboard provides comprehensive insights into our e-commerce dataset, analyzing:
- Product Categories and Distributions
- Price Analysis and Correlations
- Rating Patterns and Customer Behavior
- Advanced Clustering Analysis
""")

# Sidebar navigation
section = st.sidebar.radio(
    "Choose Analysis Section",
    ["Category Overview", "Price Analysis", "Rating Analysis", "Clustering Insights"]
)

if section == "Category Overview":
    st.header("Product Category Analysis")
    
    # Main category distribution
    st.subheader("Product Distribution by Main Category")
    st.image(get_image_path("product_distribution_main_category.png"))
    st.markdown("""
    **Key Insights:**
    - Electronics dominates with 35.5% of products
    - Computers & Accessories follows at 31.3%
    - Home & Kitchen represents 30.6%
    - Other categories make up small portions
    """)
    
    # Category price distributions
    st.subheader("Price Distribution by Categories")
    col1, col2 = st.columns(2)
    with col1:
        st.image(get_image_path("category_price_distribution.png"))
    with col2:
        st.image(get_image_path("main_category_price_distribution.png"))

elif section == "Price Analysis":
    st.header("Price Analysis")
    
    # Overall price distribution
    st.subheader("Overall Price Distribution")
    st.image(get_image_path("price_distribution.png"))
    st.markdown("""
    **Price Distribution Insights:**
    - Most products are concentrated in lower price ranges
    - Few products have very high prices
    - Clear right-skewed distribution
    """)
    
    # Correlation matrix
    st.subheader("Feature Correlations")
    st.image(get_image_path("correlation_matrix.png"))
    st.markdown("""
    **Correlation Insights:**
    - Strong correlation (0.96) between actual and discounted prices
    - Weak correlation between price and ratings
    - Minimal correlation between discount percentage and other features
    """)

elif section == "Rating Analysis":
    st.header("Customer Ratings Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Rating Count Distribution")
        st.image(get_image_path("rating_count_by_average_rating.png"))
        st.markdown("""
        **Rating Distribution Insights:**
        - Most products have ratings between 3.8-4.5
        - Peak rating count around 4.0-4.2
        - Few products with very low ratings
        """)
    
    with col2:
        st.subheader("Ratings vs Discount")
        st.image(get_image_path("ratings_vs_discount_percentage.png"))
        st.markdown("""
        **Rating-Discount Relationship:**
        - No strong correlation between ratings and discounts
        - Discounts range from 0-80%
        - Most products maintain good ratings regardless of discount
        """)

else:  # Clustering Insights
    st.header("K-Means Clustering Analysis")
    
    cluster_view = st.selectbox(
        "Select Clustering Perspective",
        ["Price-Rating Clusters", "Category Clusters", "Review Clusters"]
    )
    
    col1, col2 = st.columns(2)
    
    if cluster_view == "Price-Rating Clusters":
        with col1:
            st.image(get_image_path("3d_clusters_kmeans_1.png"))
        with col2:
            st.image(get_image_path("elbow_method_kmeans_1.png"))
            st.markdown("""
            **Cluster Analysis 1:**
            - Optimal number of clusters: 4-5
            - Clear segmentation based on price ranges
            - Rating patterns visible in clusters
            """)
            
    elif cluster_view == "Category Clusters":
        with col1:
            st.image(get_image_path("3d_clusters_kmeans_2.png"))
        with col2:
            st.image(get_image_path("elbow_method_kmeans_2.png"))
            st.markdown("""
            **Cluster Analysis 2:**
            - Category-based segmentation
            - Price variation within categories
            - Distinct product groupings
            """)
    
    else:
        with col1:
            st.image(get_image_path("3d_clusters_kmeans_3.png"))
        with col2:
            st.image(get_image_path("elbow_method_kmeans_3.png"))
            st.markdown("""
            **Cluster Analysis 3:**
            - Review-based clustering
            - Rating frequency patterns
            - Customer behavior segments
            """)

# Footer
st.markdown("---")
st.markdown("""
*This analysis is based on historical e-commerce data. The insights provided can help in:*
- Product pricing strategies
- Category management
- Customer satisfaction understanding
- Market segmentation
""")