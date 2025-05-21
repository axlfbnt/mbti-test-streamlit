import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Tes MBTI", layout="centered")
st.title("🧠 Tes MBTI")

# Reset tombol
if "reset" not in st.session_state:
    st.session_state.reset = False

# Inisialisasi state jika belum ada
if "nama" not in st.session_state:
    st.session_state.nama = ""
if "tes_dimulai" not in st.session_state:
    st.session_state.tes_dimulai = False
if "jawaban" not in st.session_state or st.session_state.reset:
    st.session_state.jawaban = [""] * 20
if "halaman" not in st.session_state or st.session_state.reset:
    st.session_state.halaman = 1

# Reset state
if st.session_state.reset:
    st.session_state.reset = False
    st.rerun()

# Input nama
if not st.session_state.tes_dimulai:
    st.session_state.nama = st.text_input("Masukkan nama kamu:", st.session_state.nama)
    if st.session_state.nama:
        if st.button("▶️ Mulai Tes MBTI"):
            st.session_state.tes_dimulai = True
            st.rerun()
    st.stop()

# Pertanyaan MBTI
pertanyaan = [
    ("Ketika menghadiri pesta atau acara besar, kamu lebih suka:",
     ["(E) Berinteraksi dan mengobrol dengan banyak orang, bahkan orang baru yang belum dikenal.",
      "(I) Berbicara hanya dengan beberapa orang terdekat dan lebih memilih suasana yang tenang."]),
    
    ("Dalam mengambil keputusan penting, kamu cenderung mengandalkan:",
     ["(T) Pemikiran logis, analisis fakta, dan objektivitas tanpa dipengaruhi emosi.",
      "(F) Perasaan pribadi dan dampaknya terhadap orang lain, lebih mempertimbangkan empati."]),
    
    ("Kamu merasa lebih nyaman dalam lingkungan kerja atau hidup yang:",
     ["(J) Terstruktur, penuh perencanaan, dan ada rutinitas yang jelas.",
      "(P) Fleksibel, spontan, dan memberi ruang untuk perubahan mendadak."]),
    
    ("Saat belajar sesuatu yang baru, kamu lebih menyukai pendekatan:",
     ["(S) Konkret dan nyata, fokus pada fakta dan pengalaman langsung.",
      "(N) Abstrak dan teoretis, fokus pada konsep dan kemungkinan yang belum terjadi."]),
    
    ("Ketika bertemu orang baru, kamu biasanya:",
     ["(E) Merasa bersemangat dan langsung terlibat dalam percakapan.",
      "(I) Perlu waktu untuk merasa nyaman dan cenderung mengamati dulu."]),
    
    ("Saat menghadapi konflik atau perbedaan pendapat, kamu akan:",
     ["(T) Menilai secara objektif dan mencari solusi logis yang paling efisien.",
      "(F) Memahami perasaan orang lain dan berusaha menjaga keharmonisan."]),
    
    ("Dalam mengerjakan tugas atau proyek, kamu biasanya:",
     ["(J) Membuat rencana sejak awal dan menyelesaikannya jauh sebelum tenggat waktu.",
      "(P) Mengandalkan inspirasi di saat terakhir dan bekerja secara spontan."]),
    
    ("Ketika mempelajari hal baru, kamu lebih suka:",
     ["(S) Penjelasan langkah demi langkah dengan contoh nyata.",
      "(N) Gambaran besar terlebih dahulu dan kemudian menyusun maknanya sendiri."]),
    
    ("Aktivitas yang membuatmu merasa hidup dan bersemangat adalah:",
     ["(E) Kegiatan yang ramai, sosial, dan penuh interaksi dengan banyak orang.",
      "(I) Kegiatan yang tenang, pribadi, dan memberi waktu untuk refleksi."]),
    
    ("Saat berada di situasi penuh tekanan atau panik, kamu akan:",
     ["(T) Mengambil langkah rasional dan mencari solusi logis sesegera mungkin.",
      "(F) Mengandalkan intuisi dan perasaan untuk menentukan langkah terbaik."]),
    
    ("Ketika memiliki ide yang ingin dibagikan, kamu lebih suka:",
     ["(E) Menyampaikannya secara terbuka dan spontan, langsung di forum umum.",
      "(I) Memikirkan matang-matang dulu lalu membagikannya secara pribadi."]),
    
    ("Dalam menghadapi peraturan atau sistem yang ada, kamu biasanya:",
     ["(J) Mengikuti aturan dan prosedur yang berlaku dengan konsisten.",
      "(P) Menyesuaikan aturan sesuai situasi dan kebutuhan saat itu."]),
    
    ("Jenis pekerjaan yang kamu rasa paling cocok adalah:",
     ["(T) Pekerjaan yang menantang secara logika seperti analisis data atau pemrograman.",
      "(F) Pekerjaan yang melibatkan interaksi dan membantu kesejahteraan orang lain."]),
    
    ("Ketika membayangkan masa depan, kamu lebih fokus pada:",
     ["(S) Hal-hal yang bisa diprediksi, realistik, dan dapat direncanakan dengan jelas.",
      "(N) Kemungkinan-kemungkinan kreatif dan visi besar yang mungkin terjadi."]),
    
    ("Ketika akhir pekan tiba, kamu lebih memilih untuk:",
     ["(E) Menghabiskan waktu dengan teman-teman dan melakukan aktivitas sosial.",
      "(I) Menikmati waktu sendiri untuk membaca, menonton, atau istirahat."]),
    
    ("Dalam menghadapi deadline atau tenggat waktu, kamu:",
     ["(J) Menyelesaikannya jauh-jauh hari agar tenang dan terhindar dari stres.",
      "(P) Sering merasa lebih produktif saat dikejar waktu di menit-menit akhir."]),
    
    ("Jika harus memilih jenis acara pengembangan diri, kamu lebih tertarik pada:",
     ["(E) Seminar atau workshop besar dengan banyak peserta dan peluang networking.",
      "(I) Sesi diskusi kecil atau mentoring pribadi dengan suasana akrab."]),
    
    ("Dalam hal berbelanja atau memilih sesuatu, kamu cenderung tertarik pada:",
     ["(S) Produk yang bisa langsung dilihat, disentuh, dan digunakan secara nyata.",
      "(N) Sesuatu yang memberikan pengalaman unik atau punya nilai simbolik."]),
    
    ("Ketika merencanakan liburan, kamu akan:",
     ["(J) Membuat itinerary lengkap dan detail sebelum berangkat.",
      "(P) Menentukan tujuan utama saja, sisanya mengalir sesuai situasi."]),
    
    ("Dalam kegiatan belajar kelompok, kamu lebih nyaman untuk:",
     ["(E) Aktif berdiskusi, bertanya, dan menjelaskan pendapatmu.",
      "(I) Mendengarkan lebih banyak, mencatat, dan menyimak terlebih dahulu."]),
]

# Pagination
jumlah_per_halaman = 5
total_soal = len(pertanyaan)
total_halaman = (total_soal + jumlah_per_halaman - 1) // jumlah_per_halaman

def next_page():
    if st.session_state.halaman < total_halaman:
        st.session_state.halaman += 1

def prev_page():
    if st.session_state.halaman > 1:
        st.session_state.halaman -= 1

# Soal per halaman
start = (st.session_state.halaman - 1) * jumlah_per_halaman
end = start + jumlah_per_halaman

for idx in range(start, min(end, total_soal)):
    q, options = pertanyaan[idx]
    st.markdown(f"**{idx+1}. {q}**")
    if st.session_state.jawaban[idx]:
        selected = st.radio(
            "", options, index=options.index(st.session_state.jawaban[idx]), key=f"q{idx}"
        )
    else:
        selected = st.radio("", options, key=f"q{idx}")
    st.session_state.jawaban[idx] = selected

# Navigasi
col1, col2, col3 = st.columns(3)
with col1:
    if st.session_state.halaman > 1:
        st.button("⬅️ Sebelumnya", on_click=prev_page)
with col2:
    st.button("🔄 Reset Tes", on_click=lambda: setattr(st.session_state, "reset", True))
with col3:
    if st.session_state.halaman < total_halaman:
        st.button("Selanjutnya ➡️", on_click=next_page)

# Hasil
if st.session_state.halaman == total_halaman:
    st.markdown("---")
    if st.button("🔮 Lihat Hasil"):
        df = pd.DataFrame(st.session_state.jawaban, columns=["jawaban"])
        for trait in ["E", "I", "S", "N", "T", "F", "J", "P"]:
            df[trait] = df["jawaban"].apply(lambda x: int(f"({trait})" in x))
        skor = df.drop(columns=["jawaban"]).sum().to_dict()

        hasil = ""
        hasil += "E" if skor["E"] >= skor["I"] else "I"
        hasil += "S" if skor["S"] >= skor["N"] else "N"
        hasil += "T" if skor["T"] >= skor["F"] else "F"
        hasil += "J" if skor["J"] >= skor["P"] else "P"

        deskripsi = {
            "INTJ": "Kamu adalah seorang perencana jangka panjang yang punya visi dan strategi. Kamu independen dan suka bekerja sendirian.",
            "INTP": "Kamu analitis, logis, dan senang memahami konsep yang kompleks. Kamu senang mengeksplorasi ide-ide baru dan sering berpikir mendalam.",
            "ENTJ": "Kamu pemimpin alami, berorientasi pada hasil, dan pandai mengambil keputusan logis.",
            "ENTP": "Kamu inovatif, cepat berpikir, dan menyukai debat sehat. Kamu selalu mencari tantangan baru.",
            "INFJ": "Kamu visioner dan memiliki nilai kuat. Kamu suka membantu orang lain berkembang.",
            "INFP": "Kamu idealis, penuh empati, dan tertarik pada makna hidup yang mendalam. Kamu kreatif dan suka membantu orang lain.",
            "ENFJ": "Kamu karismatik, empatik, dan mampu menginspirasi orang lain. Kamu hebat dalam memahami kebutuhan orang lain.",
            "ENFP": "Kamu antusias, penuh ide, dan sangat peduli pada orang lain. Kamu suka kebebasan dan tidak suka rutinitas.",
            "ISTJ": "Kamu bertanggung jawab, logis, dan menghargai tradisi. Kamu senang menyelesaikan tugas dengan teliti.",
            "ISFJ": "Kamu setia, penuh perhatian, dan suka membantu orang lain. Kamu senang menjaga harmoni di lingkungan sekitar.",
            "ESTJ": "Kamu tegas, terorganisir, dan suka memimpin. Kamu senang menjaga struktur dan efisiensi.",
            "ESFJ": "Kamu perhatian, loyal, dan suka membantu. Kamu senang membuat orang di sekitarmu merasa nyaman.",
            "ISTP": "Kamu praktis, logis, dan suka memecahkan masalah secara langsung. Kamu cenderung tenang di bawah tekanan.",
            "ISFP": "Kamu tenang, artistik, dan menyukai keindahan. Kamu lebih suka mengekspresikan diri secara pribadi.",
            "ESTP": "Kamu spontan, energik, dan suka tantangan nyata. Kamu sangat tanggap terhadap situasi sekitar.",
            "ESFP": "Kamu ceria, ramah, dan suka bersenang-senang. Kamu menikmati momen saat ini dan membuat orang lain tertawa.",
        }

        with st.expander("📌 Klik untuk melihat hasil MBTI kamu"):
            st.subheader(f"🧬 MBTI: {hasil}")
            st.success(f"Selamat {st.session_state.nama}, MBTI kamu adalah **{hasil}** 🎉")
            st.info(deskripsi.get(hasil, "Kamu unik dan sulit ditebak! 🎭"))

            chart_df = pd.DataFrame({
                "Dimensi": list(skor.keys()),
                "Skor": list(skor.values())
            })
            fig = px.bar(chart_df, x="Dimensi", y="Skor", color="Dimensi", title="Skor Dimensi MBTI", text="Skor")
            st.plotly_chart(fig)