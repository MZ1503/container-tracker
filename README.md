## AI Container Tracker

An AI powered container tracking agent built for EU logistics companies. The agent helps in providing demurrage status of the container across major shipping lines like Maersk, CMA CGM, MSC, Hapag Lloyd, OOCL to help logistics teams avoid demurrage charged.

## Why is this built?
I have worked in logistics and supply chain operation for several years and this project is out of firsthand experience of traclking container status manually. It takes many hours to track statuses.

## Features

- Real-time container status via track-trace.com API
- EU demurrage & detention risk calculation (Hamburg, Rotterdam, Antwerp)
- Waiver grounds identification (Rhine low water, port congestion etc.)
- EUR-based charge estimates
- Shipping line identification from container prefix

## Tech Stack

- Python
- OpenAI GPT-4o-mini
- Pydantic (data validation)
- track-trace.com API
- Docker (containerized)

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

## Example

Enter Container number: MSCU1234567

Container is at Hamburg port.
Days at port: 6
Free days remaining: 0
Risk Level: HIGH
Estimated charge: EUR 70/day
Recommendation: Pick up immediately!

## Architecture

-User Input 
-Identify Shipping Line 
-API Call (track-trace)
-AI Analysis
-Demurrage Calculation 
-Recommendation

## Ports Covered

- Hamburg (DEHAM)
- Bremerhaven (DEBRV)
- Rotterdam (NLRTM)
- Antwerp (BEANR)
- Duisburg (DEDUI)

## API Setup

This project uses track-trace.com API for live container data.

For live tracking:
1. Sign up at track-trace.com
2. Get API key
3. Add to .env:
   TRACKTRACE_API_KEY=your_key

Agent uses shipping rules to provide general guidance

