# Modeling Unspoken Emotions using NLP

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

