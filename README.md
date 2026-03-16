python -m venv env
pip install streamlit textblob
python -m textblob.download_corpora
streamlit run sentiment_ui.py
