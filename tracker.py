from openai import OpenAI
from dotenv import load_dotenv
from pydantic import BaseModel
import requests
import json


load_dotenv(override=True)
client=OpenAI()

container= input("Enter Container number:")

shipping_rules="""
EU PORTS DEMURRAGE & DETENTION RULES 2026:

MAIN PORTS FOR GERMAN COMPANIES:
- Hamburg (DEHAM) — Germany biggest
- Bremerhaven (DEBRV) — Germany second
- Rotterdam (NLRTM) — Europe biggest!
- Antwerp (BEANR) — Belgium, very close to Germany
- Duisburg (DEDUI) — Inland Rhine port

FREE DAYS — Standard Per Port:
All ports: 5-7 free days standard
Public holidays = Calendar days (count!)
Currency: EUR

DEMURRAGE RATES — North European Ports:
Hamburg Export:
- Day 1-10: FREE
- Day 11-12: EUR 55 (20ft) / EUR 70 (40ft)
- Day 13-19: EUR 80 (20ft) / EUR 105 (40ft)
- Day 20+:   EUR 100 (20ft) / EUR 130 (40ft)

Rotterdam/Antwerp/Bremerhaven:
- Similar tier structure to Hamburg
- Slightly different rates per carrier

IMPORTANT NOTE:
North European ports (Germany, Netherlands)
= HIGHER D&D charges than South Europe!
Average EU D&D cost = EUR 449 over 14 days!

WAIVER GROUNDS EU:
- Force majeure
- Port/terminal congestion
- Rhine low water (common in Germany!)
- Customs examination hold
- Terminal strike
- Carrier equipment failure

EU CUSTOMS RULES:
- ENS filing required 24h before arrival
- Customs clearance before pickup
- Temporary storage after discharge
- Agency fee: EUR 150-400

CONTAINER PREFIXES:
- MSCU/MAEU = Maersk
- CMAU/CGMU = CMA CGM
- MSDU/MEDU = MSC
- HLXU/HLCU = Hapag Lloyd
- OOLU = OOCL

CALCULATION RULES:
- Import demurrage: Starts day after vessel discharge
- Export demurrage: Starts day of full gate-in
- Each day or part thereof = Full day charged!
- First chargeable day = Day after free time ends
"""


messages=[
         { "role": "system",
           "content": f"""Hi LLM!. You are a logistics expert.You have to tell the user when it enters container number about the 
                      status of the container in order to save demurrage and detention charges based on the 
                      shipping rules {shipping_rules}. Basically help the user to avoid the demurrage and detention risk."""},

                      {"role" : "user",
                        "content" : f"""User enters the container number {container}"""}]

class ContainerStatus(BaseModel):
    container_number: str
    shipping_line: str
    location: str
    status: str
    demurrage_rate: float
    detention_rate: float
    total_charge: float
    days_at_port: int
    free_days_remaining: int
    free_days_used: int
    recommendation: str
    risk_level: str
    


         



