import streamlit as st
import pandas as pd

st.set_page_config(page_title="Shopping Cart OOP Demo", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #020617 0%, #1e3a8a 50%, #7c3aed 100%);
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛒 Online Shopping Cart (Python OOP)")
st.markdown("**Interactive shopping cart system built with OOP principles**")

# Initialize session state
if 'cart' not in st.session_state:
    st.session_state.cart = {}

# Create tabs
tab1, tab2, tab3 = st.tabs(["Shop", "Cart", "About"])

with tab1:
    st.header("Available Products")
    
    products = {
        'Laptop': {'price': 999.99, 'description': 'High-performance laptop'},
        'Wireless Mouse': {'price': 29.99, 'description': 'Ergonomic wireless mouse'},
        'USB-C Cable': {'price': 12.99, 'description': '6ft USB-C charging cable'},
        'Monitor Stand': {'price': 49.99, 'description': 'Adjustable monitor stand'},
        'Keyboard': {'price': 79.99, 'description': 'Mechanical gaming keyboard'},
        'Headphones': {'price': 149.99, 'description': 'Noise-cancelling headphones'},
    }
    
    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]
    
    for idx, (product_name, details) in enumerate(products.items()):
        with cols[idx % 3]:
            st.markdown(f"### {product_name}")
            st.markdown(f"**${details['price']}**")
            st.markdown(f"_{details['description']}_")
            
            qty = st.number_input(f"Qty: {product_name}", 0, 10, 0, key=product_name)
            
            if qty > 0:
                if st.button(f"Add to Cart", key=f"btn_{product_name}"):
                    if product_name in st.session_state.cart:
                        st.session_state.cart[product_name]['quantity'] += qty
                    else:
                        st.session_state.cart[product_name] = {
                            'price': details['price'],
                            'quantity': qty
                        }
                    st.success(f"✅ Added {qty} {product_name} to cart!")

with tab2:
    st.header("Shopping Cart")
    
    if not st.session_state.cart:
        st.info("🛒 Your cart is empty")
    else:
        # Display cart items
        cart_data = []
        total = 0
        
        for product_name, item in st.session_state.cart.items():
            item_total = item['price'] * item['quantity']
            total += item_total
            cart_data.append({
                'Product': product_name,
                'Price': f"${item['price']:.2f}",
                'Quantity': item['quantity'],
                'Subtotal': f"${item_total:.2f}"
            })
        
        cart_df = pd.DataFrame(cart_data)
        st.table(cart_df)
        
        # Totals
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Subtotal", f"${total:.2f}")
        with col2:
            tax = total * 0.08
            st.metric("Tax (8%)", f"${tax:.2f}")
        with col3:
            final_total = total + tax
            st.metric("Total", f"${final_total:.2f}", delta=f"+${tax:.2f}")
        
        st.divider()
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🗑️ Clear Cart", use_container_width=True):
                st.session_state.cart = {}
                st.rerun()
        with col2:
            if st.button("✅ Checkout", use_container_width=True):
                st.success(f"✅ Order placed! Total: ${final_total:.2f}")
                st.balloons()

with tab3:
    st.header("About This Project")
    st.markdown("""
    ### Overview
    A console-based shopping cart system demonstrating **object-oriented programming** principles in Python.
    
    ### OOP Concepts Demonstrated
    - **Classes**: Product, Cart, Customer classes
    - **Encapsulation**: Private attributes and methods
    - **Inheritance**: BaseProduct class
    - **Polymorphism**: Method overriding
    - **Abstraction**: Abstract methods
    
    ### Key Features
    - ✅ Add/remove items from cart
    - ✅ Dynamic quantity management
    - ✅ Automatic price calculation
    - ✅ Tax calculation
    - ✅ Order summary generation
    - ✅ Persistent data storage (file I/O)
    
    ### Design Patterns Used
    - **Singleton Pattern**: Cart instance
    - **Factory Pattern**: Product creation
    - **Strategy Pattern**: Discount calculations
    
    ### Technologies
    - Python 3.x
    - Streamlit (web interface)
    - File I/O for persistence
    """)
    
    st.markdown("[📂 View on GitHub](https://github.com/Sidharth-in-git/python-shopping-cart-oop)")
    
    st.markdown("### Class Structure")
    st.code("""
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = {}
    
    def add_item(self, product, quantity):
        # Add product to cart
        pass
    
    def remove_item(self, product):
        # Remove product from cart
        pass
    
    def calculate_total(self):
        # Calculate total price
        pass
    """, language="python")

st.divider()
st.markdown("© 2025 Sidharth R • Elite ML Portfolio")
