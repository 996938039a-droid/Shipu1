# For My Favorite Person — Streamlit version

Same site, wrapped so it runs on Streamlit. `app.py` loads `index.html`, `style.css`,
`script.js`, and everything in `images/` at startup, inlines them into one
self-contained HTML page (images become base64 data — no broken links), and
renders it with `st.components.v1.html`.

## Option A — Streamlit Community Cloud (free, easiest)

1. **Push this folder to GitHub.** Create a repo (e.g. `for-shipu`), upload
   `app.py`, `requirements.txt`, `index.html`, `style.css`, `script.js`, and the
   whole `images/` folder.
2. Go to **share.streamlit.io** → sign in with GitHub → **New app**.
3. Pick your repo, branch `main`, and set **Main file path** to `app.py`.
4. Click **Deploy**. In ~1–2 minutes you'll get a live link like
   `https://for-shipu.streamlit.app`.

## Option B — run it locally first (optional, to preview)

```bash
pip install -r requirements.txt
streamlit run app.py
```

This opens it at `http://localhost:8501`.

## Notes

- If anything looks cut off, adjust the `height=1000` value near the bottom of
  `app.py` — that's the visible frame height in pixels; the page scrolls inside it.
- If you edit `index.html`, `style.css`, or `script.js`, no changes to `app.py`
  are needed — it re-reads and re-inlines those files every time the app runs.
- This app has no backend logic and doesn't need secrets, a database, or
  environment variables — it's just serving a static page through Streamlit.
