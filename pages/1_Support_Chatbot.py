import streamlit as st
from openai import OpenAI

# --------------------------------------------------

# Page Configuration

# --------------------------------------------------

st.set_page_config(
page_title="MiniStore Support",
page_icon="💬",
layout="wide"
)

# --------------------------------------------------

# OpenAI Client

# --------------------------------------------------

client = OpenAI(
api_key=st.secrets["OPENAI_API_KEY"]
)

# --------------------------------------------------

# Product Catalog

# --------------------------------------------------

PRODUCT_CATALOG = """
MiniStore Products:

1. Wireless Bluetooth Headphones
   Price: $79.99
   Category: Electronics
   Description: Premium sound quality with active noise cancellation and 30-hour battery life.

2. Smart Fitness Watch
   Price: $129.99
   Category: Electronics
   Description: Track heart rate, sleep, workouts, and smartphone notifications.

3. Ergonomic Office Chair
   Price: $249.99
   Category: Furniture
   Description: Comfortable mesh chair with lumbar support.

4. Organic Coffee Beans
   Price: $18.99
   Category: Groceries
   Description: Freshly roasted premium Arabica beans.

5. Running Shoes
   Price: $89.99
   Category: Fashion
   Description: Lightweight athletic shoes designed for performance.

6. Portable Laptop Stand
   Price: $34.99
   Category: Accessories
   Description: Adjustable aluminum stand for laptops and tablets.
   """

# --------------------------------------------------

# System Prompt

# --------------------------------------------------

SYSTEM_PROMPT = f"""
You are MiniStore's professional customer support assistant.

Your responsibilities:

* Answer questions about MiniStore products.
* Help with orders.
* Help with shipping and delivery.
* Help with refunds.
* Help with returns.
* Help with payment methods.

Product Catalog:
{PRODUCT_CATALOG}

Rules:

1. Only answer questions related to MiniStore.
2. If a question is unrelated, politely explain that you can only assist with MiniStore products, orders, delivery, refunds, returns, and payments.
3. Be friendly, professional, and concise.
4. Never invent products that are not listed in the catalog.
5. If the user asks about an order, request their order number if needed.
   """

# --------------------------------------------------

# Session State

# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------------------------

# Page Header

# --------------------------------------------------

st.title("💬 MiniStore Support Chatbot")

st.write("""
Welcome to MiniStore Customer Support!

I can help with:

* Product information
* Orders
* Delivery & shipping
* Refunds
* Returns
* Payment methods
  """)

# --------------------------------------------------

# Display Chat History

# --------------------------------------------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------

# Chat Input

# --------------------------------------------------

user_prompt = st.chat_input(
"Ask a MiniStore support question..."
)

if user_prompt:


# Store user message
    st.session_state.messages.append(
    {
        "role": "user",
        "content": user_prompt
    }
)

with st.chat_message("user"):
    st.markdown(user_prompt)

# Build conversation history
messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

messages.extend(st.session_state.messages)

# OpenAI API Call
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    temperature=0.3
)

assistant_reply = response.choices[0].message.content

# Save assistant response
st.session_state.messages.append(
    {
        "role": "assistant",
        "content": assistant_reply
    }
)

# Display assistant response
with st.chat_message("assistant"):
    st.markdown(assistant_reply)



