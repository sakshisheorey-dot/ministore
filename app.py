
import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# --------------------------------------------------
# Product Data
# --------------------------------------------------
products = [
    {
        "name": "Wireless Bluetooth Headphones",
        "price": 79.99,
        "category": "Electronics",
        "description": "Premium sound quality with active noise cancellation and 30-hour battery life."
    },
    {
        "name": "Smart Fitness Watch",
        "price": 129.99,
        "category": "Electronics",
        "description": "Track heart rate, sleep, workouts, and receive smartphone notifications."
    },
    {
        "name": "Ergonomic Office Chair",
        "price": 249.99,
        "category": "Furniture",
        "description": "Comfortable mesh chair with lumbar support for long work sessions."
    },
    {
        "name": "Organic Coffee Beans",
        "price": 18.99,
        "category": "Groceries",
        "description": "Freshly roasted premium Arabica beans sourced from sustainable farms."
    },
    {
        "name": "Running Shoes",
        "price": 89.99,
        "category": "Fashion",
        "description": "Lightweight athletic shoes designed for comfort and performance."
    },
    {
        "name": "Portable Laptop Stand",
        "price": 34.99,
        "category": "Accessories",
        "description": "Adjustable aluminum stand compatible with most laptops and tablets."
    }
]

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------
st.markdown("""
<style>

.hero {
    background: linear-gradient(135deg,#2563eb,#7c3aed);
    padding:40px;
    border-radius:15px;
    color:white;
    text-align:center;
    margin-bottom:30px;
}

.support-btn {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #2563eb;
    color: white !important;
    padding: 14px 22px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    z-index: 9999;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
}

.support-btn:hover {
    background-color: #1d4ed8;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.title("🛍️ MiniStore")

categories = ["All"] + sorted(
    list(set([p["category"] for p in products]))
)

selected_category = st.sidebar.selectbox(
    "Browse Categories",
    categories
)

st.sidebar.markdown("---")

st.sidebar.subheader("🛒 Shopping Cart")

st.sidebar.metric("Items", 3)
st.sidebar.metric("Total", "$228.97")

# --------------------------------------------------
# Hero Section
# --------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>🛍️ MiniStore</h1>
    <p>Your One-Stop Destination for Quality Products</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Welcome Section
# --------------------------------------------------
st.header("Welcome to MiniStore")

st.write("""
Discover premium products across electronics, fashion,
furniture, groceries and accessories.

Browse our featured products and enjoy a modern shopping experience.
""")

# --------------------------------------------------
# Product Filtering
# --------------------------------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

# --------------------------------------------------
# Featured Products
# --------------------------------------------------
st.header("Featured Products")

for i in range(0, len(filtered_products), 3):

    cols = st.columns(3)

    for col, product in zip(cols, filtered_products[i:i+3]):

        with col:

            with st.container(border=True):

                st.subheader(product["name"])

                st.caption(product["category"])

                st.write(product["description"])

                st.markdown(
                    f"### 💲{product['price']}"
                )

                st.button(
                    "Add to Cart",
                    key=product["name"]
                )

# --------------------------------------------------
# Support Chatbot Navigation
# --------------------------------------------------
st.markdown("<br><br>", unsafe_allow_html=True)

st.page_link(
    "pages/1_Support_Chatbot.py",
    label="💬 Open Support Chatbot"
)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")

st.caption(
    "© 2026 MiniStore | Streamlit E-Commerce Demo"
)
