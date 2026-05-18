## AI Container Tracker - LangGraph Edition

An AI agent that tracks shipping containers and provides demurrage risk recommendations for EU ports.Built by a logistics operations professional who spent years tracking containers manually.

## Problem this project addresses

Tracking container status manually takes hours per day.
Demurrage charges in EU ports average EUR 449 over 14 days.
One missed alert and thousands in unnecessary charges.

## What This Does
Automatically tracks a container number, classifies 
demurrage risk, calculates charges, and gives 
an AI-powered recommendation — in seconds.

## Architecture
4-node LangGraph pipeline:

Node 1 → Fetch live container status
Node 2 → Classify risk (LOW / MEDIUM / HIGH / CRITICAL)  
Node 3 → Calculate demurrage charges (Hamburg EU rules)
Node 4 → AI recommendation to avoid charges

## Tech Stack
- Python 3.11
- LangGraph — stateful 4-node workflow
- OpenAI GPT-4o-mini — risk classification + recommendations
- HuggingFace Inference API — EU privacy-first alternative
- python-dotenv — secure credential management

## Why Two LLM Options?
German enterprise companies require data to stay in EU.
HuggingFace option ensures GDPR-compliant, 
privacy-first deployment for EU logistics companies.

## How to Run

### 1. Clone the repo
git clone https://github.com/MZ1503/container-tracker
cd container-tracker

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

### 3. Install dependencies
pip install -r requirements.txt

### 4. Configure environment
cp .env.example .env
# Add your API key to .env

### 5. Run
python tracker.py

## Environment Variables
Create a '.env' file based on '.env.example':
OPENAI_API_KEY=your_key_here
USE_HUGGINGFACE=False  # Set True for EU privacy deployment

## Ports Covered
Hamburg (DEHAM) · Bremerhaven (DEBRV) · 
Rotterdam (NLRTM) · Antwerp (BEANR) · Duisburg (DEDUI)

