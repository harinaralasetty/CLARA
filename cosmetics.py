import streamlit as st
import random

def apply_cosmetics():
    st.markdown(
    """
    <style>
    /* Main container styling */

    /* Increase text size for all elements */
    html {
        font-size: 20px; 
    }

    .main {
        display: block;
        padding: 2rem;
    }

    /* Sidebar styling */
    .css-1d391kg {
        display: block;
        padding: 2rem 1rem;
    }

    .stVerticalBlock {
        display: block
    }

    /* Chat message styling */
    .stChatMessage {
        border-radius: 15px;
        padding: 1rem;
        margin: 0.5rem 0;
    }

    /* Light mode styles */
    :root {
        --user-message-bg: #e3f2fd;
        --assistant-message-bg: #f5f5f5;
        --text-color: black;
        --selected-thread-bg: #d6d6d6;
        --thread-hover-bg: #e1e1e1;
        --thread-text-color: black;
    }

    /* Dark mode styles */
    @media (prefers-color-scheme: dark) {
        :root {
            --user-message-bg: #1e88e5;
            --assistant-message-bg: #424242;
            --text-color: white;
            --selected-thread-bg: #444444;
            --thread-hover-bg: #555555;
            --thread-text-color: white;
        }
    }

    /* Apply styles to chat messages */
    .stChatMessage[data-testid="user-message"] {
        background-color: var(--user-message-bg);
        color: var(--text-color);
    }

    .stChatMessage[data-testid="assistant-message"] {
        background-color: var(--assistant-message-bg);
        color: var(--text-color);
    }

    /* Thread selector styling */
.thread-box {
    margin: 0 !important; 
    padding: 10px;
    background-color: transparent;
    border: none;
    border-radius: 12px;
    cursor: pointer;
    box-sizing: border-box;
    display: block;
    transition: background-color 0.2s, color 0.2s;
    color: var(--thread-text-color);
    margin-bottom: 0.5rem;
    max-height: 45px !important;
    overflow: hidden;
    text-overflow: ellipsis;
    
}

    .thread-box:hover {
        background-color: var(--thread-hover-bg);
        color: var(--thread-text-color); /* Keep text color consistent */
        margin: 0 !important;
    }

    .thread-box.selected {
        background-color: var(--selected-thread-bg);
        color: var(--thread-text-color); /* Keep text color consistent */
        margin: 0 !important;
        display: block;
        margin-bottom: 18px !important;

    padding: 10px;
    }

    /* Button styling */
    .stButton button {
        border-radius: 15px;
        margin: 0 !important; 
        display: block;
        overflow: hidden;
    
    }

    .stButton button:hover {
        box-shadow: 0 2px px rgba(0,0,0,0.1);
        transition: none;
    }

    /* File uploader styling */
    .stFileUploader {
        padding: 1rem;
        border: 2px dashed #ccc;
        border-radius: 10px;
        margin: 1rem 0;
    }

    /* Header styling */
    .fixed-header {
        background-color: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(5px);
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        padding: 1rem 0;
    }

    /* Button styling */
.stButton > button {
    height: 45px; 
    margin: 0 !important;
    padding: 10px;
    background-color: transparent;
    border: none; 
    text-align: left !important;
    width: 100%;
    cursor: pointer;
    font-size: 16px;
    display: block;
    border-radius: 12px;
    box-sizing: border-box;
    transition: background-color 0.2s, color 0.2s;
    
    /* Add some spacing at the bottom if needed */
    margin-bottom: 0.5rem;
}

    .stButton > button:hover {
        background-color: var(--thread-hover-bg);
    }

    .stButton > button.selected {
        background-color: var(--selected-thread-bg);
    margin: 0 !important;
    padding: 10px;
    }

    .stButton > button.on-click {
    }
    """,
    unsafe_allow_html=True
    )

def get_random_greeting():
    messages = [
    "Back for a check-up with your digital health buddy? 🩺",
    "Questions about your health? Let’s get to the heart of it. ❤️",
    "Wellness starts with a question—what’s yours today? 🌿",
    "Your symptoms have my full attention. Let’s unpack them. 🩻",
    "Doctor Google’s confusing—I’ll keep it clear. 🧠💬",
    "Let’s translate the medical jargon together. 📖🩺",
    "Feeling off? Let’s figure out why. 🧭",
    "Welcome back. Your health questions are always worth asking. 🌟",
    "Nothing too weird or too small—ask away. 🧬",
    "Your body’s talking—let’s listen closely. 👂🫀",
    "Got a new ache or worry? I’m all ears. 👂💡",
    "Better questions mean better health. Let’s start there. 🔍",
    "One step closer to peace of mind. 🧠☁️",
    "Health can be confusing—I’ll help you sort it out. 🧩",
    "You’ve got the symptoms, I’ve got the science. 🧪",
    "Let’s make sense of what your body’s trying to say. 🩻🧠",
    "Feeling under the weather? Let’s look into it. 🌧️➡️☀️",
    "What’s bothering you today? Let’s figure it out. 🧠🩺",
    "Pain, fatigue, weird rash? I'm not judging. Just helping. 🩹",
    "Whether it’s sleep, stress, or sneezes—I’m here for it. 😴😷",
    "Got questions after your last appointment? Let’s review. 📋",
    "Looking up symptoms again? Let’s do it the smart way. 💡📱",
    "Your health isn’t a puzzle—unless we solve it. 🧩❤️",
    "Let’s turn worry into knowledge. 🧠➡️📘",
    "Don’t just Google it—let’s understand it. 🔍🖥️",
    "The body’s complex, but your questions don’t have to be. 🧬📘",
    "Ask anything—symptoms, side effects, or just strange stuff. 🤔🧪",
    "Let’s get to the root of what you’re feeling. 🌱",
    "Your health story matters. I’m listening. 📖🫀",
    "Every ache has a reason. Let’s explore yours. 🌡️",
    "From flu to fatigue—nothing’s too basic or too complex. 🌬️😴",
    "The more you ask, the more you understand. 💬🩺",
    "Here to decode your diagnosis—or help avoid one. 🔎🧠",
    "Feeling fine or freaking out—I’ve got you either way. 🫂",
    "Questions before the doctor visit? Let’s prep. 📋🩺",
    "Let’s untangle symptoms, not tie new knots. 🧶",
    "Even small symptoms can matter. Let’s look closer. 🔬",
    "Trust your gut—but I’ll explain what it might be saying. 🤰🧠",
    "Headaches? Heart rate? Health plans? Bring it on. 🧠❤️📄",
    "Body changes can be scary. Let’s talk through them. 🫣🩺",
    "No white coats here—just straight talk. 🧥❌🩺✅",
    "Start with curiosity, leave with confidence. 🧠💪",
    "You’re not overreacting. You’re being smart. 👏🧬",
    ]
    
    return random.choice(messages)
