import streamlit as st
import requests
import json

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="🛰️ API Explorer",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- FUNGSI UTAMA ---
def make_api_request(method, url, headers, params, body):
    """Fungsi untuk melakukan request API dan mengembalikan respons."""
    try:
        # Mengonversi body dari string JSON ke dictionary jika metodenya POST/PUT
        json_body = None
        if method in ["POST", "PUT"] and body:
            try:
                json_body = json.loads(body)
            except json.JSONDecodeError:
                return None, "Error: Request Body bukan format JSON yang valid."

        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            params=params,
            json=json_body,
            timeout=15
        )
        return response, None
    except requests.exceptions.RequestException as e:
        return None, f"Terjadi kesalahan koneksi: {e}"

# --- TAMPILAN ANTARMUKA (UI) ---

# Judul dan Deskripsi
st.title("🛰️ API Explorer Sederhana")
st.markdown("""
Aplikasi ini membantu Anda untuk berinteraksi dan mengeksplorasi REST API. 
Cukup masukkan **Base URL**, **Endpoint**, dan **API Key** Anda, lalu kirim permintaan.
""")
st.markdown("---")


# Layout Kolom: Kolom Kiri untuk Input, Kolom Kanan untuk Output
col1, col2 = st.columns((1, 1), gap="large")

with col1:
    st.header("⚙️ Konfigurasi Permintaan")
    
    base_url = st.text_input("1. Base URL API", "https://api.github.com", help="URL dasar dari API yang ingin diakses, tanpa endpoint.")
    
    api_key = st.text_input("2. API Key / Bearer Token", type="password", help="Masukkan API Key atau Token Anda. Akan disembunyikan.")
    
    auth_method = st.selectbox(
        "3. Metode Otentikasi", 
        ("Bearer Token", "Custom Header", "Query Parameter"),
        help="Pilih cara API Key dikirimkan. 'Bearer Token' adalah yang paling umum."
    )
    
    # Input tambahan berdasarkan metode otentikasi
    custom_header_name = ""
    query_param_name = ""
    if auth_method == "Custom Header":
        custom_header_name = st.text_input("Nama Header", "x-api-key")
    elif auth_method == "Query Parameter":
        query_param_name = st.text_input("Nama Parameter Query", "api_key")

    # Kolom untuk Metode HTTP dan Endpoint agar sejajar
    c1, c2 = st.columns(2)
    with c1:
        http_method = st.selectbox("4. Metode HTTP", ["GET", "POST", "PUT", "DELETE"])
    with c2:
        endpoint = st.text_input("5. Endpoint", "/user", help="Contoh: /users/1 atau /products")

    # Area untuk Request Body jika metode POST atau PUT
    request_body = ""
    if http_method in ["POST", "PUT"]:
        st.subheader("6. Request Body (JSON)")
        request_body = st.text_area(
            "Masukkan konten body dalam format JSON", 
            '{\n  "key": "value",\n  "name": "contoh"\n}',
            height=150
        )
    
    # Tombol untuk mengirim permintaan
    st.markdown("") # Spasi
    send_button = st.button("🚀 Kirim Permintaan", type="primary", use_container_width=True)


with col2:
    st.header("📝 Hasil Respons")
    
    if send_button:
        # Validasi input dasar
        if not base_url or not endpoint:
            st.error("Harap isi Base URL dan Endpoint terlebih dahulu.")
        else:
            with st.spinner("Mengirim permintaan ke server..."):
                # Membangun URL lengkap
                full_url = base_url.rstrip('/') + '/' + endpoint.lstrip('/')
                
                # Menyiapkan headers dan params
                headers = {"Accept": "application/json"}
                params = {}

                if api_key:
                    if auth_method == "Bearer Token":
                        headers["Authorization"] = f"Bearer {api_key}"
                    elif auth_method == "Custom Header" and custom_header_name:
                        headers[custom_header_name] = api_key
                    elif auth_method == "Query Parameter" and query_param_name:
                        params[query_param_name] = api_key
                
                # Melakukan panggilan API
                response, error_message = make_api_request(
                    method=http_method,
                    url=full_url,
                    headers=headers,
                    params=params,
                    body=request_body
                )

                if error_message:
                    st.error(error_message)
                
                elif response is not None:
                    # Menampilkan Status Code dengan warna
                    status_code = response.status_code
                    if 200 <= status_code < 300:
                        st.success(f"**Status Code: {status_code}**")
                    elif 400 <= status_code < 500:
                        st.warning(f"**Status Code: {status_code}** (Client Error)")
                    elif status_code >= 500:
                        st.error(f"**Status Code: {status_code}** (Server Error)")
                    else:
                        st.info(f"**Status Code: {status_code}**")

                    # Menampilkan Response Body (JSON)
                    st.subheader("Response Body")
                    try:
                        # Tampilkan sebagai JSON jika memungkinkan
                        response_json = response.json()
                        st.json(response_json)
                    except json.JSONDecodeError:
                        # Tampilkan sebagai teks mentah jika bukan JSON
                        st.code(response.text, language="text")

                    # Menampilkan Response Headers di dalam expander
                    with st.expander("Lihat Response Headers"):
                        st.json(dict(response.headers))
    else:
        st.info("Hasil respons dari API akan ditampilkan di sini setelah Anda menekan tombol 'Kirim Permintaan'.")

# Footer
st.markdown("---")
st.markdown("Dibuat dengan ❤️ menggunakan **Python & Streamlit**.")