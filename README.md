# FWI Prediction using Machine Learning

This project predicts the **Fire Weather Index (FWI)** based on various meteorological inputs using a Ridge Regression model. It features a user-friendly web interface built using Flask and Bootstrap with support for dark mode.

---

## 🔧 Features

- Predicts FWI based on temperature, humidity, wind speed, rain, FFMC, DMC, ISI, classes, and region
- Machine learning model trained using `scikit-learn`
- Responsive frontend using Bootstrap 5
- Dark mode toggle for user comfort
- Clean two-page structure: welcome screen and prediction page

---

## 🧪 Input Parameters

- **Temperature** (°C)
- **RH** (Relative Humidity %)
- **Ws** (Wind Speed)
- **Rain** (mm)
- **FFMC** (Fine Fuel Moisture Code)
- **DMC** (Duff Moisture Code)
- **ISI** (Initial Spread Index)
- **Classes** (Fire weather classification)
- **Region** (Geographical region ID)

---

## 🚀 How to Run the App

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/fwi-prediction.git
   cd fwi-prediction
