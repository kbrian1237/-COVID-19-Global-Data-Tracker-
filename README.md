# 🦠 COVID-19 Global Data Tracker

Welcome to the **COVID-19 Global Data Tracker**, a data analysis project that explores the global impact of the COVID-19 pandemic using real-world data from the [Our World in Data](https://ourworldindata.org/coronavirus) repository. 🌍📊

This project analyzes trends in confirmed cases, deaths, and vaccination progress across different countries and over time. It is designed to help learners practice data wrangling, exploratory analysis, and data storytelling using Python.

---

## 🎯 Project Objectives

This project aims to:

- ✅ Collect COVID-19 data from a trusted source (Our World in Data)
- ✅ Clean and prepare the dataset for analysis
- ✅ Explore time-based trends in cases, deaths, and vaccinations
- ✅ Compare metrics across countries such as Kenya, India, and the USA
- ✅ Create visualizations (line charts, bar charts, optional choropleths) to highlight patterns
- ✅ Summarize key findings through code, visuals, and narrative commentary
- ✅ Optionally, build an interactive dashboard with Streamlit for deeper exploration

---

## 🧰 Tools and Libraries Used

This project was built using the following tools and libraries in the Python ecosystem:

- 💻 **Python 3**
- 🧪 **Jupyter Notebook** (for code + narrative reporting)
- 📦 `pandas` – for data manipulation and analysis
- 📊 `matplotlib` & `seaborn` – for plotting line graphs, bar charts, and heatmaps
- 🗺️ `plotly.express` – for creating interactive choropleth maps (optional)
- 🚀 `streamlit` – to build a simple, user-friendly dashboard interface (optional)

---

## 📂 How to Run the Project

1.  **Clone this repository** or download the files manually:
    ```bash
    git clone [https://github.com/yourusername/covid19-global-tracker.git](https://github.com/yourusername/covid19-global-tracker.git)
    cd covid19-global-tracker
    ```
2.  **Install required Python libraries** (create a virtual environment if needed):
    ```bash
    pip install pandas matplotlib seaborn plotly streamlit
    ```
3.  **Download the dataset** from Our World in Data:
    * Save it in the root folder as: `owid-covid-data.csv`
4.  **Launch the Jupyter Notebook** and run each cell:
    ```bash
    jupyter notebook covid_analysis.ipynb
    ```
5.  **(Optional) Run the Streamlit app** for an interactive dashboard:
    ```bash
    streamlit run app.py
    ```

---

## 🔍 Key Insights

📌 Here are some key insights derived from analyzing the dataset:

- 🇺🇸 The United States consistently recorded the highest number of total COVID-19 cases throughout the pandemic. It also reported high vaccination numbers but saw several wave peaks in cases and deaths.
- 🇮🇳 India experienced a severe second wave in 2021, characterized by a sharp spike in cases and daily deaths. However, the vaccination effort significantly improved in the latter part of the year.
- 🇰🇪 Kenya's vaccination rollout was slower compared to other countries, but the country maintained relatively lower total cases and death counts. This may be due to early containment efforts or demographic factors.
- 📉 Death rates decreased over time in many countries, potentially due to the effect of vaccines and better treatment strategies.
- ⚠️ Some countries had data inconsistencies, likely caused by gaps in reporting or lack of testing infrastructure. This highlights the importance of reliable data for managing global health crises.

---

## 📸 Sample Visualizations

The notebook includes the following visual outputs:

- 📈 Line charts for daily and cumulative case trends
- 📊 Bar charts showing top countries by total cases and deaths
- 🌡️ Heatmaps for correlation analysis (optional)
- 🗺️ Choropleth maps visualizing total cases or vaccinations by country
- 📆 Interactive date filters (via Streamlit dashboard)

---

## 💡 Reflections

This project demonstrates how real-world data can be analyzed to gain insights into global events. It also showcases the power of Python for cleaning, analyzing, and visualizing datasets in a structured and reproducible way. Learners can expand this project by:

- Adding more countries or regions
- Including ICU and hospitalization trends
- Making the dashboard more dynamic (country/date dropdowns)
- Automating updates with live API data

---

## 📄 Deliverables

- ✅ A Jupyter Notebook report (`covid_analysis.ipynb`) with code, charts, and markdown commentary
- ✅ An optional interactive dashboard (`app.py`) using Streamlit
- ✅ A complete `README.md` to guide users through the project

---

## 📘 Note

This project is for educational purposes only and reflects data trends up to the time of dataset download.

---

## 📬 Contact

For questions or contributions, feel free to open an issue or fork the repo!

🔗 Stay safe. Stay informed.
