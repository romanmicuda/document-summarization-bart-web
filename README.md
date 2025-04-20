# AI Text Summarizer

## About
This project is an AI-powered text summarization application using a fine-tuned BART model to generate concise summaries.  
It features a **React** frontend for user interaction and a **Flask** backend for processing summarization requests.  
The trained model (`best_model.pt`) is downloaded from Google Drive and supports **CUDA acceleration** if a compatible GPU is available.

---

## Installation

### Prerequisites
- Python 3.8+
- Node.js and npm
- (Optional) GPU with CUDA for faster processing

### Steps

#### 1. Create Project Directory
```bash
mkdir ai-summarizer
cd ai-summarizer
```

#### 2. Download Trained Model
- Download `best_model.pt` from: **https://drive.google.com/file/d/11Im2W0D7BVFftrm5l5Qlx5gDPBJ4lsU5/view?usp=sharing**
- Place the downloaded `best_model.pt` file in the `ai-summarizer/` directory.

#### 3. Set Up Flask Backend

Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:
```bash
pip install flask flask-cors torch transformers
```

#### 4. Set Up React Frontend

Create the React app:
```bash
npx create-react-app frontend
cd frontend
```

Install Axios:
```bash
npm install axios
```

---

## Usage

### Start Flask Backend
```bash
cd ai-summarizer
source venv/bin/activate
python app.py
```
- The backend runs on **http://localhost:5000**.

### Start React Frontend
```bash
cd ai-summarizer/frontend
npm start
```
- The frontend opens at **http://localhost:3000**.

### Summarize Text
- Visit **http://localhost:3000** in your browser.
- Enter text in the textarea.
- Click **"Summarize"** to view the generated summary.

---

## Troubleshooting
- **CORS Issues**: Ensure `flask-cors` is installed.
- **Model Not Found**: Verify `best_model.pt` is in the `ai-summarizer/` directory.
- **CUDA Errors**: Check GPU compatibility or configure the project to use CPU.

---

## License
This project is licensed under the **MIT License**.
