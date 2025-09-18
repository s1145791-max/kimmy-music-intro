# Streamlit application for Kimmy's music teacher self-introduction
import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="Kimmy's Self-Introduction", page_icon="🎹", layout="centered")

# Background themes
themes = [
    ["#FFD700", "#FFFACD"],  # Classical style
    ["#FFB6C1", "#87CEFA"],  # Playful style
    ["#8A2BE2", "#00CED1"],  # Innovative style
    ["#FF7F50", "#FF6347"],  # Passionate style
]

# Set background (applied once on load)
def set_background():
    grad = random.choice(themes)
    st.markdown(f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background: linear-gradient(135deg, {grad[0]}, {grad[1]});
        overflow-x: hidden;
    }}
    .note {{
        position: absolute;
        top: -50px;
        font-size: 20px;
        animation: fall linear infinite;
        opacity: 0.7;
    }}
    @keyframes fall {{
        0% {{ transform: translateY(-50px); }}
        100% {{ transform: translateY(100vh); }}
    }}
    </style>
    """, unsafe_allow_html=True)

# Falling note animation (optimized for performance)
def add_falling_notes(note_count=10):
    notes = ["🎵", "🎶", "🎹", "🎼"]
    html = ""
    for _ in range(note_count):
        left = random.randint(0, 95)
        note = random.choice(notes)
        dur = random.randint(6, 10)
        html += f'<div class="note" style="left:{left}%; animation-duration:{dur}s;">{note}</div>'
    st.markdown(html, unsafe_allow_html=True)

# CSS styling with improved contrast
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display&family=Roboto&display=swap" rel="stylesheet">
<style>
h1, h2, h3 {{
    font-family: "Playfair Display", serif;
    text-align: center;
    color: #1a1a1a;
}}
p, ul, label {{
    font-family: "Roboto", sans-serif;
    color: #333;
}}
div.stButton > button {{
    background: linear-gradient(90deg, #6a82fb, #fc5c7d);
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 12px;
    padding: 10px 20px;
    margin: 10px;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    transition: transform 0.3s ease;
}}
div.stButton > button:hover {{
    background: linear-gradient(90deg, #fc5c7d, #6a82fb);
    transform: scale(1.05);
}}
.fade-in {{
    animation: fadeIn 0.8s ease forwards;
    opacity: 0;
}}
@keyframes fadeIn {{
    to {{ opacity: 1; transform: translateY(0px); }}
}}
input[type="radio"], input[type="text"], textarea {{
    margin: 10px;
}}
</style>
""", unsafe_allow_html=True)

# PWA support
st.markdown("""
<link rel="manifest" href="/static/manifest.json">
<meta name="theme-color" content="#FFD700">
<script>
if ('serviceWorker' in navigator) {{
    navigator.serviceWorker.register('/static/service-worker.js')
        .then(() => console.log('Service Worker registered successfully'))
        .catch(err => console.log('Service Worker registration failed:', err));
}}
</script>
""", unsafe_allow_html=True)

# Set background and falling notes
set_background()
add_falling_notes()

# Title and introduction
st.title("🎶 Hi, I’m Kimmy – Your Future Music Teacher 🎶")
st.markdown("### Let’s connect through the world of music and create endless possibilities with sound.")
st.write("👇 Click the buttons below to get to know me better:")

# Display section function
def display_section(title, content):
    placeholder = st.empty()
    with placeholder.container():
        st.markdown(f"""
        <div class='fade-in' style="background-color: white; padding: 20px;
        border-radius: 15px; box-shadow: 2px 2px 10px rgba(0,0,0,0.2);">
        <h3>{title}</h3>
        {content}
        </div>
        """, unsafe_allow_html=True)

# Session state for quiz
if 'quiz_submitted' not in st.session_state:
    st.session_state.quiz_submitted = False
    st.session_state.quiz_answer = ""

# Self-introduction sections
if st.button("📖 About Me"):
    display_section("📖 About Me",
        """
        <p>🎹 Hi, I’m <b>Kimmy</b>, a passionate and creative music teacher from Hong Kong, studying AI & EdTech at The Education University of Hong Kong.</p>
        <p>My love for music began at age 6 when I first touched a piano, sparking a lifelong journey of exploration and expression. I’m an outgoing and patient educator who thrives on connecting with students and fostering their creativity. Beyond music, I enjoy blending technology with art, drawing inspiration from my interdisciplinary studies in AI, which I use to design innovative teaching methods. My goal is to make every lesson a joyful and transformative experience!</p>
        """
    )

if st.button("🎹 My Music Skills"):
    display_section("🎹 My Music Skills",
        """
        <ul>
        <li>🎼 <b>Piano Performance</b>: Proficient contemporary pieces, from Baroque, classical, romantic to modern pop arrangements.</li>
        <li>✍️ <b>Composition & Arrangement</b>: Experienced in crafting educational ensemble pieces and short piano works.</li>
        <li>📚 <b>Curriculum Design</b>: Adept at designing engaging, student-centered music lessons that spark creativity.</li>
        </ul>
        """
    )

if st.button("💡 My Teaching Philosophy"):
    display_section("💡 My Teaching Philosophy",
        """
        <ul>
        <li>🌟 <b>Inspire Creativity</b>: Encourage students to express their emotions and stories through music, fostering a personal connection.</li>
        <li>💻 <b>Integrate Technology</b>: Use digital tools and AI to create interactive, modern learning experiences.</li>
        <li>🎵 <b>Personalized Learning</b>: Tailor lessons to each student’s unique style, helping them discover their musical voice.</li>
        </ul>
        """
    )

if st.button("🎨 My Music Inspiration"):
    display_section("🎨 My Music Inspiration",
        """
        <p>My music is inspired by a vibrant blend of influences that shape my teaching and creativity:</p>
        <ul>
        <li>💻 <b>Technology-Driven Creativity</b>: My AI & EdTech studies inspire me to experiment with tools like algorithmic composition, creating music that blends human emotion with digital innovation, much like the dynamic soundscapes in sci-fi films.</li>
        <li>🌏 <b>Cultural Storytelling</b>: Draw from diverse traditions, like the delicate melodies of Japanese koto or the rhythmic energy of Cantonese pop, to craft lessons that resonate with students’ cultural identities.</li>
        <li>🌸 <b>Everyday Moments</b>: Find melodies in daily life, encouraging students to discover music in their own surroundings.</li>
        </ul>
        """
    )

if st.button("🎼 Favorite Composers & Works"):
    display_section("🎼 Favorite Composers & Works",
        """
        <ul>
        <li>🎹 <b>Beethoven</b>: Moonlight Sonata – Its emotive depth inspires my teaching.</li>
        <li>🎹 <b>Chopin</b>: Nocturnes – Their lyrical beauty captivates my heart.</li>
        <li>🎹 <b>Mozart</b>: Eine Kleine Nachtmusik – Its lively and joyful melodies make music fun and accessible for all my students.</li>
        <li>🎹 <b>Debussy</b>: Clair de Lune – Its dreamy quality sparks creativity.</li>
        </ul>
        """
    )

# Enhanced quiz section with submit button
# Quiz section with submit button
if st.button("❓ Test Your Music Knowledge"):
    display_section("❓ Test Your Music Knowledge",
        """
        <p>Try this quick quiz to explore music concepts I love teaching!</p>
        <p><b>Question:</b> Which composer wrote the famous <i>Moonlight Sonata</i>?</p>
        <form>
        <input type="radio" name="q1" value="Beethoven"> Beethoven<br>
        <input type="radio" name="q1" value="Mozart"> Mozart<br>
        <input type="radio" name="q1" value="Chopin"> Chopin<br>
        </form>
        """
    )
    st.session_state.quiz_answer = st.radio("Select your answer:", ["Beethoven", "Mozart", "Chopin"], key="quiz")
    if st.button("Submit Answer"):
        st.session_state.quiz_submitted = True
        if st.session_state.quiz_answer == "Beethoven":
            st.markdown("<p style='color: green; text-align: center;'>Correct! Beethoven composed the Moonlight Sonata, a piece I love teaching for its emotional depth.</p>", unsafe_allow_html=True)
        else:
            st.markdown(f"<p style='color: red; text-align: center;'>Incorrect. The correct answer is Beethoven. Try again or discuss with me in class!</p>", unsafe_allow_html=True)

# Contact form section
if st.button("📬 Connect With Me"):
    display_section("📬 Connect With Me",
        """
        <p>Interested in music lessons or collaboration? Please fill out the form below and email your message to me!</p>
        <form>
        <label>Name: </label><input type="text" style="width: 200px; margin: 10px;" id="name"><br>
        <label>Message: </label><textarea style="width: 200px; height: 100px; margin: 10px;" id="message"></textarea><br>
        </form>
        <p>Copy your name and message, then email them to <a href="mailto:s1145791@s.eduhk.hk">s1145791@s.eduhk.hk</a>. I’ll get back to you soon!</p>
        """
    )

# Footer with PWA download prompt
st.markdown("""
<hr>
<h3 style='text-align: center;'>🙏 Thank You for Getting to Know Me!</h3>
<p style='text-align: center;'>I look forward to inspiring students with music and creating a joyful learning journey together. 🎹✨</p>
<p style='text-align: center;'>💾 <a href="YOUR_GITHUB_PAGES_URL" target="_blank">Click to Download This App</a></p>
<p style='text-align: center;'>For the best experience, visit the link above in Chrome or Safari and select “Add to Home Screen” to install it on your device.</p>
""", unsafe_allow_html=True)
