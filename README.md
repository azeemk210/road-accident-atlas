# 🗺 Road Deaths Map (React + FastAPI + GeoJSON)

An interactive map visualization of road traffic deaths in Europe (2014–2024).  
Frontend built with **React + Leaflet**, backend powered by **FastAPI** serving GeoJSON data.

---

## 🚀 Features

- Choropleth map by number of deaths  
- Dynamic popups with country/year stats  
- Year slider support (2014–2024)  
- Backend API: `/api/road-deaths/{year}` → returns filtered GeoJSON  

---

## 🛠 Prerequisites

- [Git](https://git-scm.com/)  
- [Node.js](https://nodejs.org/) (>= 16.x)  
- [Python 3.10+](https://www.python.org/)  
- [pip](https://pip.pypa.io/)  

---

## 📂 Project Structure

```
ROAD-SAFETY-ATLAS/
│
├── backend/
│   ├── app/
│   │   ├── data/
│   │   │   └── road_deaths.geojson      # GeoJSON dataset
│   │   ├── routes/
│   │   │   └── deaths.py                # API routes for road deaths
│   │   ├── db.py                        # (optional) Database connection
│   │   ├── main.py                      # FastAPI entry point
│   │   ├── models.py                    # Database models (if used)
│   │   ├── schemas.py                   # Pydantic schemas
│   │   └── utils.py                     # Helper functions
│   ├── .env                             # Environment variables
│   └── requirements.txt                 # Python dependencies
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.css
│   │   ├── App.js
│   │   ├── App.test.js
│   │   ├── index.css
│   │   ├── index.js
│   │   ├── logo.svg
│   │   ├── reportWebVitals.js
│   │   ├── RoadDeathsMap.js             # Map visualization component
│   │   └── setupTests.js
│   ├── .env.local                       # Local React env config
│   ├── package.json                     # Node dependencies
│   └── package-lock.json
│
├── .gitignore
└── README.md

```

---

## ⚙️ Local Setup

### 1. Clone the repo
```bash
git clone git@github.com:YOUR_USERNAME/road-deaths-map.git
cd road-deaths-map
```

### 2. Backend (FastAPI)
```bash
cd backend
python3 -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 3. Frontend (React + Leaflet)
```bash
cd frontend
npm install
npm start
```
Frontend runs on [http://localhost:3000](http://localhost:3000)

---

## 🌐 Deployment on AWS EC2

### 1. Launch EC2
- Ubuntu 22.04 LTS  
- t2.micro (free tier)  
- Open ports: **22, 80, 443**  

### 2. Connect via SSH
```bash
ssh -i your-key.pem ubuntu@YOUR_PUBLIC_IP
```

### 3. Install dependencies
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y git python3-pip python3-venv nodejs npm
```

### 4. Clone repo
```bash
git clone git@github.com:YOUR_USERNAME/road-deaths-map.git
cd road-deaths-map
```

### 5. Backend setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

### 6. Frontend build
```bash
cd frontend
npm install
npm run build
npm install -g serve
serve -s build -l 3000
```

Access in browser:  
- Backend → `http://YOUR_PUBLIC_IP:8000`  
- Frontend → `http://YOUR_PUBLIC_IP:3000`

---

## 📌 Next Steps

- Add **Nginx** reverse proxy for one domain (`/api` → FastAPI, `/` → React).  
- Add **Docker Compose** for easier deployment.  
- Configure **SSL (Let’s Encrypt)** for HTTPS.  
