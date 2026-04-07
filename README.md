# Modeling Unspoken Emotions using NLP
## Unsent Project 💌
“Sometimes the words you never send tell more than the ones you do.”

Unsent Project is a sleek, interactive Streamlit app that helps users capture, organize, and explore thoughts, messages, or emotions they’ve never sent. Perfect for journaling, emotional clarity, or personal reflection.

## Features
Save & manage unsent messages in one place
Tag & categorize emotions (love, anger, longing, nostalgia)
Search & filter by keywords, dates, or emotion
Export your thoughts as text or CSV
Minimalist UI optimized for focus & reflection
Built with Streamlit, Python, and pandas

## Overview
This project analyzes unspoken emotions in text data using state-of-the-art NLP techniques. The pipeline includes data preprocessing, feature engineering, model training, evaluation, and a Streamlit app for inference.

## Project Structure
```
unsent_project/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── evaluate.py
│   └── utils.py
├── models/
├── app/
│   └── app.py
├── outputs/
│   ├── figures/
│   └── reports/
├── tests/
├── README.md
├── requirements.txt
└── .gitignore
```

## Setup Instructions
1. Clone the repository or navigate to the project directory.
2. Create a virtual environment:
   ```
   python -m venv venv
   ```
3. Activate the virtual environment:
   - Windows: `venv\\Scripts\\activate`
   - macOS/Linux: `source venv/bin/activate`
4. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
5. Run the Streamlit app:
   ```
   streamlit run app/app.py
   ```

## Usage
- Place raw data in `data/raw/`.
- Run preprocessing: `python -m src.data_preprocessing`
- Train model: `python -m src.train_model`
- Evaluate: `python -m src.evaluate`
- Launch app: `streamlit run app/app.py`

