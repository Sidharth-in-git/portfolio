# Deploying to Hugging Face Spaces

## Steps to Deploy Each App

### 1. Create Account on Hugging Face
- Go to [huggingface.co](https://huggingface.co)
- Sign up and create a free account

### 2. For Each Streamlit App

#### Wine Quality Prediction
1. Go to [huggingface.co/spaces](https://huggingface.co/spaces)
2. Click **"Create new Space"**
   - Space name: `wine-quality-prediction`
   - Space SDK: **Streamlit**
3. Upload `wine_app.py` as `app.py`
4. Add `requirements.txt`:
   ```
   streamlit>=1.28
   scikit-learn>=1.3
   pandas>=2.0
   numpy>=1.24
   ```
5. Rename or create `app.py` from `wine_app.py`

#### House Price Prediction
Same process with:
- Space name: `house-price-prediction`
- Upload `house_app.py` as `app.py`

#### Shopping Cart OOP
Same process with:
- Space name: `shopping-cart-oop`
- Upload `cart_app.py` as `app.py`

### 3. Access Your Spaces
Your space will be live at:
- `https://huggingface.co/spaces/yourusername/wine-quality-prediction`
- `https://huggingface.co/spaces/yourusername/house-price-prediction`
- `https://huggingface.co/spaces/yourusername/shopping-cart-oop`

### 4. Update Portfolio Links
Update the demo URLs in `index.html` with your actual Hugging Face Space URLs.

## Local Testing
```bash
# Install Streamlit
pip install streamlit

# Run apps locally
streamlit run wine_app.py
streamlit run house_app.py
streamlit run cart_app.py
```

Visit `http://localhost:8501` in your browser.
