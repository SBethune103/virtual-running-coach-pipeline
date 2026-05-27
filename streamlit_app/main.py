import streamlit as st
from pathlib import Path
import sys

# Add src to path so we can import our modules
sys.path.append(str(Path(__file__).parent.parent))

from src.config.settings import settings

# Page configuration
st.set_page_config(
    page_title=settings.config["ui"]["app_title"],
    page_icon="🏃‍♂️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Navigation
st.sidebar.title("🏃‍♂️ Virtual Running Coach")
st.sidebar.markdown("### Your AI Running Companion")

page = st.sidebar.radio(
    "Go to",
    ["🏠 Dashboard", "🤖 Coach Chat", "📊 My Training", "📚 Knowledge Base", "⚙️ Settings"]
)

# Main Content
if page == "🏠 Dashboard":
    st.title("Welcome to Your Virtual Running Coach")
    st.markdown("### How can I help you train smarter today?")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Weekly Volume", "42 km", "↑ 8%")
    with col2:
        st.metric("Longest Run", "18.5 km", "↑ 2.3 km")
    with col3:
        st.metric("Est. Marathon Time", "3:45", "-4 min")
    
    st.info("Connect your Strava account to get personalized insights!")

elif page == "🤖 Coach Chat":
    st.title("🤖 Ask Your Running Coach")
    st.markdown("Ask me anything about training, race strategy, physiology, etc.")
    
    # Chat interface placeholder
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # User input
    if prompt := st.chat_input("Ask me a running question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = "This is a placeholder response. The full RAG + Strava integration will go here."
                st.markdown(response)
        
        st.session_state.messages.append({"role": "assistant", "content": response})

elif page == "📊 My Training":
    st.title("📊 My Training Analysis")
    st.warning("Connect your Strava account to see your training data here.")

elif page == "📚 Knowledge Base":
    st.title("📚 Knowledge Base")
    st.info("Search through academic papers, training philosophies, and historical results.")

elif page == "⚙️ Settings":
    st.title("⚙️ Settings")
    st.subheader("Strava Integration")
    if st.button("🔗 Connect Strava Account"):
        st.success("Strava connection flow will be implemented here.")

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Virtual Running Coach v0.1")
