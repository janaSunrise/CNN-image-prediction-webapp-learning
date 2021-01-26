mkdir -p ~/.streamlit/

echo "[general]
email = \"example@example.com\"
" > ~/.streamlit/credentials.toml

echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
