# 🏍️ Online Bike Engine Store - Web Application

A modern, interactive shopping cart web application built with **Streamlit**. This project demonstrates core e-commerce functionality with a clean, user-friendly interface.

## Project Overview

This program demonstrates how online shopping works:

**Step 1:** Created an `Engine` class to represent products (engine_id, name, price, horsepower)

**Step 2:** Created a `CartItem` class where customers select quantity and choose engines, with automatic total price calculation

**Step 3:** Created a `ShoppingCart` class to manage adding/removing engines and calculating totals

**Step 4:** Converted the console application into a modern web interface using **Streamlit**

## Features

✨ **Shop Tab**
- Browse available bike engines with specifications
- View pricing and horsepower details
- Add items to cart with custom quantities

🛒 **Cart Tab**
- View all items in your shopping cart
- Adjust quantities on the fly
- Remove items individually
- Clear entire cart
- Real-time total calculation

📋 **Checkout Tab**
- Customer information collection
- Multiple payment method options (Credit/Debit Card, UPI, Net Banking)
- Order summary and confirmation
- Auto-generated order IDs
- Terms and conditions agreement

## Installation & Setup

1. **Install Streamlit:**
   ```bash
   pip install streamlit
   ```

2. **Run the application:**
   ```bash
   streamlit run streamlit_app.py
   ```

3. **Open your browser:**
   The app will automatically open at `http://localhost:8501`

## Files in This Project

- `streamlit_app.py` - Main web application (Streamlit)
- `shoppingcart.py` - Original console version
- `requirements.txt` - Python dependencies
- `readme.md` - This file

## Technical Implementation

- **Session State Management:** Persists cart data across user interactions
- **Responsive UI:** Multi-column layouts for different screen sizes
- **Custom Styling:** CSS-enhanced interface with branded colors
- **Object-Oriented Design:** Clean separation of concerns
- **Form Validation:** Input validation and error handling

## Technologies Used

- Python 3.x
- Streamlit
- HTML/CSS

## Portfolio Value

This project showcases:
- ✅ Web application development
- ✅ Interactive UI/UX design
- ✅ State management in web apps
- ✅ Object-oriented programming
- ✅ Form handling and validation
- ✅ Clean, professional code structure

## How to Use

1. Browse bike engines in the "Shop" tab
2. Select quantity and add items to cart
3. Review and manage cart items
4. Complete checkout with your details
5. Receive order confirmation

---

**Built for Portfolio | December 2025**
