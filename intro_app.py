# ======= 1️⃣ 必須最前面 =======
import streamlit as st
st.set_page_config(page_title="Kimmy 自我介紹", page_icon="🎹", layout="centered")

# ======= 2️⃣ 套件 =======
import numpy as np
import soundfile as sf
import tempfile
import random
import time

# ======= 3️⃣ 背景主題與漸層 =======
themes = [
    ["#FFD700", "#FFFACD"],   # 古典風
    ["#FFB6C1", "#87CEFA"],   # 輕快風
    ["#8A2BE2", "#00CED1"],   # 創新風
    ["#FF7F50", "#FF6347"],   # 熱情風
]

def set_background(grad=None):
    if grad is None:
        grad = random.choice(themes)
    st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(135deg,{grad[0]},{grad[1]});
        transition: background 0.8s ease;
        overflow-x:hidden;
    }}
    .note {{
        position: absolute;
        top: -50px;
        font-size: 25px;
        animation: fall linear infinite;
        opacity:0.8;
    }}
    @keyframes fall {{
        0% {{ transform: translateY(-50px); }}
        100% {{ transform: translateY(100vh); }}
    }}
    </style>
    """, unsafe_allow_html=True)

# ======= 4️⃣ 音符動畫 =======
def add_falling_notes(note_count=20):
    notes = ["🎵","🎶","🎹","🎼"]
    html=""
    for _ in range(note_count):
        left=random.randint(0,95)
        note=random.choice(notes)
        dur=random.randint(5,12)
        html+=f'<div class="note" style="left:{left}%; animation-duration:{dur}s;">{note}</div>'
    st.markdown(html,unsafe_allow_html=True)

# ======= 5️⃣ CSS 美化 & 文字動畫 =======
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display&family=Roboto&display=swap" rel="stylesheet">
<style>
h1,h2,h3 { font-family: "Playfair Display", serif; text-align:center; color:#2c2c2c; text-shadow:1px 1px 2px #fff;}
div.stButton > button {
    background: linear-gradient(90deg,#6a82fb,#fc5c7d);
    color:white;font-size:18px;font-weight:bold;
    border-radius:12px;padding:10px 20px;margin:10px;
    box-shadow:2px 2px 5px rgba(0,0,0,0.3);
    transition: transform 0.3s ease, background 0.5s ease;
}
div.stButton > button:hover {
    background: linear-gradient(90deg,#fc5c7d,#6a82fb);
    transform:scale(1.05);
}
.fade-in{animation:fadeIn 0.8s ease forwards; opacity:0;}
@keyframes fadeIn{to{opacity:1; transform:translateY(0px);}}
</style>
""", unsafe_allow_html=True)

# ======= 6️⃣ 鋼琴旋律生成 =======
def generate_piano_like_wav(note_count=8):
    sr = 44100
    duration = 0.5
    t = np.linspace(0,duration,int(sr*duration),endpoint=False)
    notes_hz=[261.63,293.66,329.63,349.23,392.00,440.00,493.88,523.25]
    melody=[]
    for _ in range(note_count):
        f = random.choice(notes_hz)
        wave = np.sin(2*np.pi*f*t)*np.exp(-3*t)
        melody.append(wave)
    audio = np.concatenate(melody)
    audio = audio/np.max(np.abs(audio))
    temp_wav = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    sf.write(temp_wav.name, audio, sr)
    return temp_wav.name

# ======= 7️⃣ 顯示區塊函數 =======
def display_section(title, content, note_count=20):
    theme=random.choice(themes)
    set_background(theme)
    add_falling_notes(note_count)
    placeholder=st.empty()
    with placeholder.container():
        st.markdown(f"""
        <div class='fade-in' style="background-color:white; padding:20px;
        border-radius:15px; box-shadow:2px 2px 10px rgba(0,0,0,0.2);">
        <h3>{title}</h3>
        {content}
        </div>
        """,unsafe_allow_html=True)
        wav_file = generate_piano_like_wav()
        st.audio(wav_file, format="audio/wav")
        time.sleep(0.3)

# ======= 8️⃣ 標題 =======
st.title("🎶 Hi, I’m Kimmy – Your Future Music Teacher 🎶")
st.markdown("### 讓我們在音樂的世界中相遇，一起用聲音創造無限可能。")
st.write("👇 點擊下方按鈕，互動認識我：")

# ======= 9️⃣ 按鈕互動 =======
if st.button("📖 關於我"):
    display_section("📖 關於我",
        """
        <p>🎹 大家好，我是 <b>Kimmy</b>，一位熱愛音樂、充滿創意的音樂教師。</p>
        <p>我專注於鋼琴演奏與聲樂指導，喜歡將古典與現代音樂融合，讓學生找到自己的音樂風格。</p>
        <p>在課堂上，我鼓勵學生用音樂表達情感，培養創造力與合作精神。每一次音符的跳動，都是與學生心靈的交流。</p>
        <p>我的教學理念是「用音樂啟發心靈，用創意引導學習」，希望每位學生都能愛上音樂。🎶</p>
        """
    )

if st.button("🎹 我的音樂技能"):
    display_section("🎹 我的音樂技能",
        """
        <ul>
        <li>🎼 <b>鋼琴演奏</b>: 古典 & 現代跨界作品</li>
        <li>🎤 <b>聲樂與合唱</b>: 合唱指導與聲部訓練</li>
        <li>✍️ <b>作曲與編曲</b>: 教學用合奏曲 & 短鋼琴曲創作</li>
        <li>🎧 <b>音樂科技</b>: Logic Pro, GarageBand, MuseScore</li>
        <li>📚 <b>音樂教育設計</b>: 創造有趣且有效的課程</li>
        </ul>
        """
    )

if st.button("💡 我的教學理念"):
    display_section("💡 我的教學理念",
        """
        <ul>
        <li>🌟 <b>啟發創造力</b>: 鼓勵學生表達情感與故事</li>
        <li>💻 <b>結合科技</b>: 數位工具與AI互動學習</li>
        <li>🤝 <b>促進合作</b>: 合唱、合奏與即興活動</li>
        <li>🎵 <b>個人化學習</b>: 讓學生找到自己的音樂風格</li>
        </ul>
        """
    )

if st.button("🎨 我的音樂靈感來源"):
    display_section("🎨 我的音樂靈感來源",
        """
        <p>我喜歡從自然、人文、生活經驗中汲取靈感，將情感轉化為旋律。<br>
        旅行、書籍、影像、甚至街頭的聲音都能啟發我創作新的音樂故事。</p>
        """
    )

if st.button("🎼 我最喜歡的作曲家與曲目"):
    display_section("🎼 我最喜歡的作曲家與曲目",
        """
        <ul>
        <li>🎹 <b>貝多芬</b>: 月光奏鳴曲</li>
        <li>🎹 <b>蕭邦</b>: 夜曲作品集</li>
        <li>🎹 <b>久石讓</b>: 天空之城主題曲</li>
        <li>🎹 <b>德布西</b>: 月光</li>
        </ul>
        """
    )

# ======= 10️⃣ 結尾 =======
st.markdown("""
<hr>
<h3 style='text-align:center;'>🙏 感謝大家認識我！</h3>
<p style='text-align:center;'>希望未來能與各位一起用音樂啟發心靈，共同創造更美好的教育旅程。 🎹✨</p>
""", unsafe_allow_html=True)
