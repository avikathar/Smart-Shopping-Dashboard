import streamlit as st
from abc import ABC, abstractmethod

# ------------------ ABSTRACT CLASS ------------------
class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_price(self):
        pass

    def show_discount_policy(self):
        return "🎉 Flat 10% discount on all products!"


# ------------------ PRODUCT CATEGORIES ------------------
class ElectronicProduct(Product):
    def get_price(self):
        return self.price


class ClothingProduct(Product):
    def get_price(self):
        return self.price


class GroceryProduct(Product):
    def get_price(self):
        return self.price


# ------------------ PRODUCT DATABASE ------------------
products = {
    "Electronics": [
        ElectronicProduct("Laptop 💻", 55000),
        ElectronicProduct("Smartphone 📱", 20000),
        ElectronicProduct("Headphones 🎧", 3000),
        ElectronicProduct("Smartwatch ⌚", 7000)
    ],
    "Clothing": [
        ClothingProduct("T-Shirt 👕", 800),
        ClothingProduct("Jeans 👖", 2000),
        ClothingProduct("Jacket 🧥", 3500),
        ClothingProduct("Sneakers 👟", 4000)
    ],
    "Groceries": [
        GroceryProduct("Rice (5kg) 🍚", 600),
        GroceryProduct("Milk (1L) 🥛", 60),
        GroceryProduct("Fruits Pack 🍎", 250),
        GroceryProduct("Vegetable Combo 🥦", 300)
    ]
}


# ------------------ STREAMLIT UI ------------------
st.set_page_config(page_title="Chose your choice", layout="centered")

st.title("🛒 Chose your choice")
st.subheader("Smart Shopping Dashboard")

st.markdown("---")

# Category Selection
category = st.selectbox("📂 Select Category", list(products.keys()))

# Product Selection
product_list = products[category]
product_names = [p.name for p in product_list]
selected_name = st.selectbox("🛍️ Select Product", product_names)

# Get Product Object
selected_product = next(p for p in product_list if p.name == selected_name)

# Display Product Info
st.markdown("### 📦 Product Details")
st.write(f"**Product:** {selected_product.name}")
st.write(f"**Price:** ₹{selected_product.get_price()}")

# Quantity Input
quantity = st.number_input("🔢 Enter Quantity", min_value=1, step=1)

# Pricing Logic
total_price = selected_product.get_price() * quantity
discount = total_price * 0.10
final_price = total_price - discount

# Discount Info
st.info(selected_product.show_discount_policy())

# Bill Generation
if st.button("🧾 Generate Bill"):
    st.markdown("### 💰 Bill Summary")
    st.write(f"🧮 Total Price: ₹{total_price}")
    st.write(f"💸 Discount (10%): ₹{discount}")
    st.success(f"✅ Final Price: ₹{final_price}")

# Footer
st.markdown("---")
st.caption("🚀 Chose your choice | Built with Python & Streamlit")

# Footer
st.markdown("---")
st.caption("🚀 Chose your choice | Built with Python & Streamlit")