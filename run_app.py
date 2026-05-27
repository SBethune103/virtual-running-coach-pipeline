import os
import sys
from pathlib import Path

# Add src to Python path
sys.path.append(str(Path(__file__).parent))

import streamlit.web.cli as stcli

def main():
    """Launch the Streamlit app"""
    print("🚀 Starting Virtual Running Coach...")
    
    # Ensure directories exist
    Path("data/raw").mkdir(parents=True, exist_ok=True)
    Path("data/processed").mkdir(parents=True, exist_ok=True)
    Path("data/cache").mkdir(parents=True, exist_ok=True)
    Path("vector_db").mkdir(parents=True, exist_ok=True)
    
    # Run Streamlit
    sys.argv = ["streamlit", "run", "streamlit_app/main.py", 
                "--theme.base", "dark",
                "--theme.primaryColor", "#FF4B4B"]
    
    stcli.main()

if __name__ == "__main__":
    main()