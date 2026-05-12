## AI Container Tracker - LangGraph Edition

An AI agent that tracks shipping containers and provides demurrage risk recommendations for EU ports.

## Why is this built?

I have worked in logistics and supply chain operation for several years and this project is out of firsthand experience of traclking container status manually. It takes many hours to track statuses.

## Features

- 2 node LangGraph pipeline
- Supports OpenAI and HuggingFace with the help of config switch
- Secure API key management via .env

## Tech Stack

- Python
- LangChain, LangGraph
- OpenAI GPT-4o-mini/ HuggingFace Inference (for privacy)
- LangGraph StateGraph
- Python-dotenv

## How to Run

1. Clone the repo
   git clone https://github.com/MZ1503/container-tracker

2. Install dependencies
   pip install -r requirements.txt

3. Add your API key
   Create .env file:
   OPENAI_API_KEY=your_key_here

4. Run
   python tracker.py


## Architecture

-Node 1 - fetch status
-Node 2 - Take AI recommendation


## Why support of two LLM's?
German enterprise companies require data to stay in EU and this container tracker agent has been designed for EU based logistics companies. HuggingFace  ensures privacy-first deployment.
