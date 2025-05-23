# 🕸️ Web Scraper with AI-Powered Parsing

Welcome to the **Web Scraper With AI** project!  
This tool lets you **scrape website content**, view the cleaned HTML **DOM**, and use **AI to parse specific information** from the page — all from a simple Streamlit interface.

---

## 🚀 Features

- 🌐 Scrape any publicly available website using Selenium
- 🧹 Clean and extract meaningful content using BeautifulSoup
- 🤖 Ask AI (via LangChain + Ollama) to parse data from the HTML
- 🖥️ Interactive frontend powered by Streamlit

---

## 📦 Requirements

- Python 3.10+
- Chrome WebDriver (`chromedriver.exe`) in the project folder
- Chrome browser installed
- An Ollama model like `llama3` running locally

---

## 🔧 Installation

```bash
git clone https://github.com/rypeguero/WebScraperWithAI.git
cd WebScraperWithAI

# Create virtual environment
conda create -n WebScraperWithAI python=3.10
conda activate WebScraperWithAI

# Install dependencies
pip install -r requirements.txt
