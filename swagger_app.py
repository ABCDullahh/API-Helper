import streamlit as st
import requests
import json

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="🔍 OpenAPI/Swagger Explorer",
    page_icon="🗺️",
    layout="wide",
)

# --- FUNGSI BANTU ---
def load_api_spec(url):
    """Mengunduh dan mem-parse file spesifikasi OpenAPI/Swagger dari URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Memunculkan error jika status code bukan 2xx
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Gagal mengambil data dari URL: {e}")
        return None
    except json.JSONDecodeError:
        st.error("Gagal mem-parse respons. Pastikan URL mengarah ke file JSON yang valid.")
        return None

def display_api_details(spec):
    """Menampilkan detail API berdasarkan spesifikasi yang sudah di-load."""
    # 1. Tampilkan Informasi Umum API
    info = spec.get('info', {})
    st.header(info.get('title', 'Judul API Tidak Ditemukan'))
    st.caption(f"Versi: {info.get('version', 'N/A')}")
    st.markdown(info.get('description', ''))

    # Coba tampilkan Base URL jika ada
    servers = spec.get('servers', [])
    if servers:
        st.subheader("Server / Base URL")
        for server in servers:
            st.code(server.get('url', 'URL tidak tersedia'))

    st.markdown("---")
    st.header("🗺️ Peta Endpoint")

    # 2. Tampilkan Semua Path/Endpoint
    paths = spec.get('paths', {})
    if not paths:
        st.warning("Tidak ada path/endpoint yang ditemukan dalam spesifikasi ini.")
        return

    # Urutkan path berdasarkan abjad untuk kerapian
    sorted_paths = sorted(paths.keys())

    for path in sorted_paths:
        methods = paths[path]
        for method, details in methods.items():
            # Gunakan warna berbeda untuk setiap metode HTTP
            if method.upper() == 'GET':
                method_color = "blue"
            elif method.upper() == 'POST':
                method_color = "green"
            elif method.upper() == 'PUT':
                method_color = "orange"
            elif method.upper() == 'DELETE':
                method_color = "red"
            else:
                method_color = "gray"

            summary = details.get('summary', 'Tidak ada ringkasan.')
            
            # Buat expander yang bisa diklik untuk setiap endpoint
            with st.expander(f"**`{path}`** - {summary}"):
                
                # Tampilkan tag metode dengan warna
                st.markdown(f"### <span style='color:{method_color};'>{method.upper()}</span> `{path}`", unsafe_allow_html=True)
                st.markdown(f"_{details.get('description', '')}_")

                # Tampilkan Parameter
                st.markdown("##### **Parameter**")
                parameters = details.get('parameters', [])
                if not parameters:
                    st.text("Tidak ada parameter untuk endpoint ini.")
                else:
                    for param in parameters:
                        required_tag = "Wajib" if param.get('required') else "Opsional"
                        st.markdown(f"- **`{param.get('name')}`** (`{param.get('in')}`) - `{required_tag}`")
                        st.caption(f"  {param.get('description', '')}")

                # Tampilkan Request Body (untuk POST, PUT, dll.)
                if 'requestBody' in details:
                    st.markdown("##### **Request Body**")
                    rb_content = details['requestBody'].get('content', {})
                    for media_type, schema_info in rb_content.items():
                        st.markdown(f"Tipe Konten: `{media_type}`")
                        # Anda bisa menambahkan logika lebih lanjut untuk menampilkan contoh schema
                        st.code(json.dumps(schema_info.get('schema', {}), indent=2), language="json")

                # Tampilkan Kemungkinan Respons
                st.markdown("##### **Respons**")
                responses = details.get('responses', {})
                for status_code, resp_details in responses.items():
                    st.markdown(f"- **`{status_code}`**: {resp_details.get('description', '')}")
                    

# --- ANTARMUKA UTAMA APLIKASI ---
st.title("🔍 OpenAPI / Swagger Explorer")
st.markdown("""
Aplikasi ini membaca file `openapi.json` atau `swagger.json` dari sebuah URL 
dan secara otomatis menampilkan semua *endpoint* yang tersedia, beserta detailnya. 
Ini adalah cara modern untuk "mengetahui isi" sebuah API.
""")

# Contoh URL yang bisa dicoba
st.info("💡 **Tips:** Coba gunakan URL contoh berikut dari Swagger Petstore: `https://petstore.swagger.io/v2/swagger.json`", icon="🤖")

# Input URL dari pengguna
url = st.text_input("Masukkan URL ke file openapi.json atau swagger.json:", placeholder="https://contoh.com/api/swagger.json")

if st.button("Analisis API", type="primary", use_container_width=True):
    if url:
        with st.spinner("Menganalisis spesifikasi API..."):
            # Muat spesifikasi dan simpan di session_state agar tidak hilang
            st.session_state.api_spec = load_api_spec(url)
    else:
        st.warning("Harap masukkan URL terlebih dahulu.")

# Tampilkan detail jika spesifikasi sudah berhasil di-load dan disimpan di session_state
if 'api_spec' in st.session_state and st.session_state.api_spec:
    display_api_details(st.session_state.api_spec)