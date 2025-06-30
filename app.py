import streamlit as st
from PIL import Image
import os

st.set_page_config(page_title="Çiğli Fen Lisesi - Sanal Tur", layout="centered")

# Oda bağlantıları
baglantilar = {
    "fizik": {"dogu": "rehberlik", "guney": "yeniteknoloji"},
    "rehberlik": {"bati": "fizik", "dogu": "kimya", "guney": "yeniteknoloji"},
    "mudur": {"dogu": "yeniteknoloji"},
    "kimya": {"bati": "rehberlik", "guney": "biyoloji"},
    "yeniteknoloji": {"kuzey": "fizik", "bati": "mudur", "dogu": "biyoloji"},
    "biyoloji": {"kuzey": "yeniteknoloji", "dogu": "resim", "bati": "yeniteknoloji"},
    "resim": {"bati": "biyoloji"}
}

# Görsel dosyaları (kendi görsellerinle aynı isimde yükle)
gorseller = {
    "fizik": "fizik.jpg",
    "rehberlik": "rehberlik.jpg",
    "mudur": "mudur.jpg",
    "kimya": "kimya.jpg",
    "yeniteknoloji": "yeniteknoloji.jpg",
    "biyoloji": "biyoloji.jpg",
    "resim": "resim.jpg"
}

# Oturum durumu (kaldığı konumu ve geçmiş yolu saklar)
if "konum" not in st.session_state:
    st.session_state.konum = "fizik"
    st.session_state.gecmis = ["fizik"]

# Başlık
st.title("🏫 Çiğli Fen Lisesi - Sanal Tur")
st.subheader(f"📍 Şu anda: {st.session_state.konum}")
st.text(f"🧭 Yol: {' → '.join(st.session_state.gecmis)}")

# Görsel göster
gorsel_yolu = gorseller.get(st.session_state.konum, None)
if gorsel_yolu and os.path.exists(gorsel_yolu):
    img = Image.open(gorsel_yolu).resize((400, 300))
    st.image(img)
else:
    st.warning("Bu oda için görsel bulunamadı.")

# Hareket butonları
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("↑", key="kuzey"):
        if "kuzey" in baglantilar[st.session_state.konum]:
            yeni = baglantilar[st.session_state.konum]["kuzey"]
            st.session_state.konum = yeni
            st.session_state.gecmis.append(yeni)

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    if st.button("←", key="bati"):
        if "bati" in baglantilar[st.session_state.konum]:
            yeni = baglantilar[st.session_state.konum]["bati"]
            st.session_state.konum = yeni
            st.session_state.gecmis.append(yeni)

with col3:
    if st.button("→", key="dogu"):
        if "dogu" in baglantilar[st.session_state.konum]:
            yeni = baglantilar[st.session_state.konum]["dogu"]
            st.session_state.konum = yeni
            st.session_state.gecmis.append(yeni)

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("↓", key="guney"):
        if "guney" in baglantilar[st.session_state.konum]:
            yeni = baglantilar[st.session_state.konum]["guney"]
            st.session_state.konum = yeni
            st.session_state.gecmis.append(yeni)
