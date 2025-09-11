import streamlit as st
from pathlib import Path

# Page setup
st.set_page_config(page_title="E-commerce Data Analysis", page_icon="📊", layout="wide")

# Function to get image path
def get_image_path(image_name):
    base_path = Path(__file__).parent / 'Images'
    full_path = str(base_path / image_name)
    # Add debug print
    st.write(f"Trying to load image from: {full_path}")
    # Check if file exists
    if not Path(full_path).exists():
        st.error(f"Image not found: {image_name}")
    return full_path

# Title and introduction
st.title("E-commerce Data Analysis Of amazon")
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
    ["Product Analysis", "Customer Analysis"]
)

if section == "Product Analysis":
    # Category Overview
    st.header("Product Category Analysis")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Product Distribution by Main Category")
        st.image(get_image_path("product_distribution_main_category.png"))
        st.markdown("""
        **Key Insights:**
        - The one with the most products is Electronics at 34.5%
        - Computers & Accessories follows at 31.3%
        - Home & Kitchen represents 30.6%
        - Other categories make up small portions as they are not bought as frequently
        - The distribution is fairly balanced among the top three categories
        """)
    
    with col2:
        st.subheader("Price Distribution by Categories")
        st.image(get_image_path("main_category_price_distribution.png"))

    # Price Analysis
    st.header("Price Analysis")
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Overall Price Distribution")
        st.image(get_image_path("price_distribution.png"))
        st.markdown("""
        **Price Distribution Insights:**
        - Most products are concentrated in the price range of 0- 200 dollars
        - Few products have very high prices
        """)
    
    with col4:
        st.subheader("Feature Correlations")
        st.image(get_image_path("correlation_matrix.png"))
        st.markdown("""
        **Correlation Insights:**
        - Strong correlation (0.96) between actual and discounted prices
        - Weak correlation (0.12) between price and ratings
        - Minimal correlation between discount percentage and other features
        """)
    st.header("Feture engerning")
    st.image(get_image_path("Screenshot 2025-09-11 112021.png"))
    st.markdown("""
    - New features created: discount_percentage,number, discounted_price_number, acutal_price_number, first catgroy, last catgroy
    - Fetures edited: catgroy(made the difffrent tags into a list)
    """)

    # Category Clusters
    st.header("Category Clustering Analysis")
    col5, col6 = st.columns(2)
    
    with col5:
        st.image(get_image_path("3d_clusters_kmeans_2.png"))
    with col6:
        st.image(get_image_path("elbow_method_kmeans_2.png"))
        st.markdown("""
        **Cluster Analysis 2:**
        - optmial amount of clusters: 4
        """)
    st.markdown("""
    **Overall Clustering analysis and Insights:**
    - Cluster 1 (green): Relativly large discount percantage, low review count, reletvaly high ratings. These prouducts are the ones going for a bargin and are at a lower cost tha what they should be. These prouducts should be in ads more often so that they are bought more fequrency.
    - Cluster 2 (red): Small discount percantages, low review count, high ratings. These prouducts are the prouducts that are priced correctly, and are of good quality. These prouducts should have deals on them to make them more pouplar.
    - Cluster 3 (purple): Small discount, low review count, bad ratings. These ar ethe prouducts which are of low quality. These prouducts should not be recomended to coustomers. 
    - Cluster 4 (blue): Low discount, high review count , high ratings. these prouducts are very poupular, of good quality, and have good ratings. These prouducts should be paired with each other to gain more sales.
    """)
    st.header("Clusters addde to the main dataframe")
    st.image(get_image_path("Screenshot 2025-09-11 112354.png"))

else:  # Customer Analysis
    # Rating Analysis
    st.header("Customer Ratings Analysis")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Rating Count Distribution")
        st.image(get_image_path("rating_count_by_average_rating.png"))
        st.markdown("""
        **Rating Distribution Insights:**
        - Most products have ratings between 3.8-4.5
        - Peak rating count around 4.0-4.2
        - Few products with rating below 3.5
        """)
    
    with col2:
        st.subheader("Ratings vs Discount")
        st.image(get_image_path("ratings_vs_discount_percentage.png"))
        st.markdown("""
        **Rating-Discount Relationship:**
        - No strong correlation between ratings and discounts
        - Discounts range from 0-80%
        - Most products maintain good ratings regardless of discount
        - Ratings are more influenced by product quality than price cuts
        - Price cuts happen to lower rated prouducts shown with most prouducts under a 3 rating having a higher discount percentage
        """)
    st.header("Feture engerning")
    st.image(get_image_path("Screenshot 2025-09-11 112957.png"))
    st.markdown("""
    - New features created: review count indivudal, average_rating_indivudal, fequrency, monetary value
    - Fetures edited: user_id, review_id, review_title, review_content(made the difffrent tags into a list, and then made indivudal coloums for everyone)
    """)

    # Rating Clusters
    st.header("Customer Behavior Clustering")
    col3, col4 = st.columns(2)
    
    with col3:
        st.image(get_image_path("3d_clusters_kmeans_1.png"))
    with col4:
        st.image(get_image_path("elbow_method_kmeans_1.png"))
        st.markdown("""
        **Cluster Analysis 1:**
        - Optimal number of clusters: 4
        """)
    st.markdown("""
    **Overall Clustering analysis and Insightsfor coustomer behavior:**
    - Cluster 1 (green): Very high feqrency, moderate price, reletvaly high ratings. These people are buying prouducts frequently and are with low cost. These people should have loyality programs to make them buy more expensive things. 
    - Cluster 2 (red): Low feqruency, low monatery value, high ratings. These people usualy bought one of things and are happy with them. My insights is that these people should be targeted with ads of cheaper things to make them buy more often.   
    - Cluster 3 (purple): Low feqruency, low monatery value, bad ratings. Thes people hav bought one of things and are not happy with the quality of purchas.These people should be targeted with ads of Bigger brands for better quality. 
    - Cluster 4 (blue): Modrate feqruency, high monatery value, high ratings. Theese people are buying expensive things and are happy with them. These people should be targeted with loyalitiy programs to make them buy more often.
    """)
    st.header("Clusters addde to the main dataframe")
    st.image(get_image_path("Screenshot 2025-09-11 113757.png"))

# Footer
st.markdown("---")
st.markdown("""
*This analysis is based on historical e-commerce data. The insights provided can help in:*
- Product pricing strategies
- Category management
- Customer satisfaction understanding
- Market segmentation
""")