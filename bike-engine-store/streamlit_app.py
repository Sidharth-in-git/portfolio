import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Bike Engine Store",
    page_icon="🏍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    body {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .stApp {
        background-color: #1a1a1a;
    }
    .engine-card {
        border: 2px solid #FF6B35;
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
        background-color: #2a2a2a;
        color: #ffffff;
    }
    .total-price {
        font-size: 24px;
        font-weight: bold;
        color: #FF6B35;
        margin-top: 20px;
    }
    .checkout-btn {
        background-color: #FF6B35;
        color: black;
        padding: 10px 20px;
        border-radius: 5px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Engine class
class Engine:
    def __init__(self, engine_id, name, price, horsepower):
        self.engine_id = engine_id
        self.name = name
        self.price = price
        self.horsepower = horsepower

    def __str__(self):
        return f"{self.name} ({self.horsepower} HP) - ₹{self.price:,.0f}"

# CartItem class
class CartItem:
    def __init__(self, engine, quantity=1):
        self.engine = engine
        self.quantity = quantity

    def total_price(self):
        return self.engine.price * self.quantity

# ShoppingCart class
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, engine, quantity=1):
        for item in self.items:
            if item.engine.engine_id == engine.engine_id:
                item.quantity += quantity
                return
        self.items.append(CartItem(engine, quantity))

    def remove_item(self, engine_id):
        self.items = [item for item in self.items if item.engine.engine_id != engine_id]

    def get_total(self):
        return sum(item.total_price() for item in self.items)

    def clear_cart(self):
        self.items = []

# Initialize session state
if "cart" not in st.session_state:
    st.session_state.cart = ShoppingCart()

if "checkout_complete" not in st.session_state:
    st.session_state.checkout_complete = False

# Available engines
engines = [
    Engine(1, "Yamaha 150cc Engine", 55000, 150),
    Engine(2, "KTM 200cc Engine", 85000, 200),
    Engine(3, "Royal Enfield 350cc Engine", 120000, 350),
    Engine(4, "Honda 500cc Engine", 200000, 500)
]

# Main app
st.title("🏍️ Online Bike Engine Store")
st.markdown("**Welcome to the ultimate destination for premium bike engines!**")

# Tabs for different sections
tab1, tab2, tab3 = st.tabs(["🛍️ Shop", "🛒 Cart", "📋 Checkout"])

# TAB 1: SHOP
with tab1:
    st.header("Available Bike Engines")
    
    col1, col2 = st.columns(2)
    
    for idx, engine in enumerate(engines):
        with col1 if idx % 2 == 0 else col2:
            st.markdown(f"""
            <div class="engine-card">
            <h4>{engine.name}</h4>
            <p><strong>Horsepower:</strong> {engine.horsepower} HP</p>
            <p><strong>Price:</strong> ₹{engine.price:,.0f}</p>
            </div>
            """, unsafe_allow_html=True)
            
            cols = st.columns(2)
            with cols[0]:
                quantity = st.number_input(
                    f"Quantity for {engine.name}",
                    min_value=1,
                    max_value=10,
                    value=1,
                    key=f"qty_{engine.engine_id}",
                    label_visibility="collapsed"
                )
            
            with cols[1]:
                if st.button(f"Add to Cart", key=f"add_{engine.engine_id}"):
                    st.session_state.cart.add_item(engine, quantity)
                    st.success(f"✅ {engine.name} added to cart!")

# TAB 2: SHOPPING CART
with tab2:
    st.header("Your Shopping Cart")
    
    if not st.session_state.cart.items:
        st.info("🛒 Your cart is empty. Start shopping!")
    else:
        st.markdown("---")
        
        # Display cart items
        for item in st.session_state.cart.items:
            col1, col2, col3, col4 = st.columns([3, 1, 1, 1])
            
            with col1:
                st.write(f"**{item.engine.name}**")
                st.caption(f"₹{item.engine.price:,.0f} per unit")
            
            with col2:
                new_qty = st.number_input(
                    "Qty",
                    min_value=1,
                    max_value=10,
                    value=item.quantity,
                    key=f"cart_qty_{item.engine.engine_id}",
                    label_visibility="collapsed"
                )
                item.quantity = new_qty
            
            with col3:
                st.write(f"₹{item.total_price():,.0f}")
            
            with col4:
                if st.button("❌", key=f"remove_{item.engine.engine_id}"):
                    st.session_state.cart.remove_item(item.engine.engine_id)
                    st.rerun()
        
        st.markdown("---")
        
        # Total price
        total = st.session_state.cart.get_total()
        st.markdown(f"<p class='total-price'>Total: ₹{total:,.0f}</p>", unsafe_allow_html=True)
        
        # Actions
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🗑️ Clear Cart", use_container_width=True):
                st.session_state.cart.clear_cart()
                st.rerun()
        
        with col2:
            if st.button("Proceed to Checkout →", use_container_width=True, type="primary"):
                st.session_state.checkout_complete = True

# TAB 3: CHECKOUT
with tab3:
    st.header("Checkout")
    
    if not st.session_state.cart.items:
        st.warning("Your cart is empty. Add items before checking out!")
    else:
        st.subheader("Order Summary")
        
        # Display order details
        for item in st.session_state.cart.items:
            st.write(f"• {item.engine.name} × {item.quantity} = ₹{item.total_price():,.0f}")
        
        st.markdown("---")
        st.markdown(f"### Total Amount: ₹{st.session_state.cart.get_total():,.0f}")
        
        # Customer information
        st.subheader("Delivery Information")
        
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name")
        with col2:
            email = st.text_input("Email Address")
        
        col1, col2 = st.columns(2)
        with col1:
            phone = st.text_input("Phone Number")
        with col2:
            address = st.text_input("Delivery Address")
        
        # Payment method
        st.subheader("Payment Method")
        payment_method = st.radio("Select Payment Method:", 
                                 ["Credit Card", "Debit Card", "UPI", "Net Banking"])
        
        # Terms and conditions
        terms = st.checkbox("I agree to the terms and conditions")
        
        # Checkout button
        if st.button("✅ Complete Purchase", type="primary", use_container_width=True):
            if not all([name, email, phone, address, terms]):
                st.error("Please fill all required fields and agree to terms!")
            else:
                # Simulate successful checkout
                st.success("🎉 Order Placed Successfully!")
                st.balloons()
                
                # Order confirmation
                st.subheader("Order Confirmation")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**Order ID:** #OSC{datetime.now().strftime('%Y%m%d%H%M%S')}")
                    st.write(f"**Customer:** {name}")
                    st.write(f"**Email:** {email}")
                
                with col2:
                    st.write(f"**Phone:** {phone}")
                    st.write(f"**Address:** {address}")
                
                st.write(f"**Total Amount:** ₹{st.session_state.cart.get_total():,.0f}")
                st.write(f"**Payment Method:** {payment_method}")
                
                st.info("📧 A confirmation email has been sent to your email address.")
                
                # Reset cart
                st.session_state.cart.clear_cart()
                st.session_state.checkout_complete = False

# Sidebar
with st.sidebar:
    st.header("📊 Cart Summary")
    if st.session_state.cart.items:
        st.metric("Items in Cart", len(st.session_state.cart.items))
        st.metric("Total Value", f"₹{st.session_state.cart.get_total():,.0f}")
    else:
        st.info("Cart is empty")
    
    st.markdown("---")
    st.subheader("About")
    st.write("This is an Online Bike Engine Shopping Application built with **Streamlit**.")
    st.write("Explore our premium collection of bike engines from leading brands.")
    
    st.markdown("---")
    st.write("**Contact Us:**")
    st.write("📧 Email: support@bikeengines.com")
    st.write("📞 Phone: +91-9876543210")
