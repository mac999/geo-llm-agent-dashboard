# Geo Map AI Agent Dashboard Example Code

## 📌 Overview
Geo Map AI Agent Dashboard Example Code is a web-based **interactive mapping solution** powered by **Open-source LLMs (Gemma, LLaMA, etc.)**. It provides **real-time geospatial data visualization** and **AI-driven insights** for infrastructure monitoring. The system is built using **Django**, **Leaflet.js**, and **LLM APIs**, offering an intuitive dashboard with **map-based analytics**. This project has the purpose of demonstration how to use LLM and apply it to map handling. This has simple mechanism with prompt template and algorithm to understand it easily. You can improve the performance after understanding it. 
</br><img src="https://github.com/mac999/geo-llm-agent-dashboard/blob/main/doc/geo_llm_demo.gif" width=600 />

## ✨ Features
- **AI-driven Geo Visualization**: Uses **LLM AI models** for geo-data processing.
- **Interactive Mapping**: Powered by **Leaflet.js** for real-time infrastructure monitoring.
- **LLM-based Query Processing**: Supports **natural language queries** for location insights.

## 🚀 Installation

### Prerequisites
- **Python** (3.8+)
- **Web Browser** (Chrome, Firefox, Edge, etc.)
- **Django and LLM API Key** (Gemma, LLaMA, etc.)
- **JavaScript Runtime** (for local testing)

### Steps
1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-repo/geo-map-ai-agent.git
   cd geo-map-ai-agent
   ```

2. **Create Virtual Environment & Install Dependencies**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install django-cors-headers Django pandas numpy gunicorn whitenoise django-environ
   run
   ```

3. **Open in Browser**
   - Simply open `index.html` in your web browser.
   - No need for a database or server setup.

4. **Customize API Configuration**
   - Modify `config.js` to set your LLM API key and preferences.
   
## 🔧 Configuration
- **API Settings**: Set up API endpoints and credentials in `settings.py`.
- **Customization**: Modify CSS and JavaScript files for UI/UX improvements.
- **Static Files**: Hosted on any web server or used locally.

## 📂 Project Structure
```
geo-llm-agent-dashboard/
│── charts/static/                    # CSS, JavaScript, images
│── charts/templates/index.html       # Main UI file
│── dashbaord                         # asgi, settings
│── static                            # resource files
│── manage.py                         # Django entry point
```

## 📜 License
This project is licensed under the **MIT License**.
- Taewook Kang, laputa99999@gmail.com
