"""
Container Tracker v2 — LangGraph Edition

Author: Mariyam Zaidi
Upgraded from: single OpenAI tool-calling script
Upgraded to: LangGraph StateGraph with 2 nodes 

Architecture:
  fetch_status-> classify_risk -> calculate_charges -> recommend_action

Why LangGraph over plain tool calling:
  - Each step has its own node which is easier to debug, test, extend
  - State is shared across all nodes
 """

from typing import TypedDict
from langgraph.graph import StateGraph, END
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Config switch -using HuggingFace
USE_HUGGINGFACE = False # Make it True to use HuggingFace Inference

if USE_HUGGINGFACE:
    from huggingface_hub import InferenceClient
    ai_client = InferenceClient(
        token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
    )
else:
    ai_client = OpenAI()

# State
class ContainerState(TypedDict):
    container_number: str
    risk_level: str
    days_at_port: int
    charge_eur: float
    recommendation: str

# Node 1
def fetch_status(state):
    print(f"Fetching Container: {state['container_number']}")
    return {"recommendation": ""}



# Node 2

def classify_risk(state):
    print(f"Classifying risk for: {state['container_number']}")
    
    if USE_HUGGINGFACE:
        response = ai_client.chat_completion(
            model="meta-llama/Llama-3.2-3B-Instruct",
            messages=[{
                "role": "user",
                "content": f"Container at Hamburg port for {state['days_at_port']} days. Classify risk as LOW, MEDIUM, HIGH, or CRITICAL. Return only one word."
            }],
            max_tokens=10
        )
        risk = response.choices[0].message.content.strip()
    else:
        response = ai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user", 
                "content": f"Container at Hamburg port for {state['days_at_port']} days. Classify risk as LOW, MEDIUM, HIGH, or CRITICAL. Return only one word."
            }]
        )
        risk = response.choices[0].message.content.strip()
    
    print(f"Risk level: {risk}")
    return {"risk_level": risk}


# Node 3
def calculate_charges(state):
    print("Calculating EUR charges...")
    
    days = state["days_at_port"]
    
    # Hamburg demurrage tiers
    if days <= 10:
        charge = 0.0
    elif days <= 12:
        charge = (days - 10) * 55.0
    elif days <= 19:
        charge = (2 * 55.0) + ((days - 12) * 80.0)
    else:
        charge = (2 * 55.0) + (7 * 80.0) + ((days - 19) * 100.0)
    
    print(f"Estimated charge: EUR {charge}")
    return {"charge_eur": charge}



# Node 4
def recommend(state):
    print("Getting recommendation from AI...")
    
    if USE_HUGGINGFACE:
        response = ai_client.chat_completion(
            model="meta-llama/Llama-3.2-3B-Instruct",
            messages=[{
                "role": "user",
                "content": f"Container {state['container_number']} Container is at Hamburg port.Provide recommendation in one line."
            }],
            max_tokens=100
        )
        answer = response.choices[0].message.content
    else:
        response = ai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"Container {state['container_number']} Container is at Hamburg port.Provide recommendation in one line."
            }]
        )
        answer = response.choices[0].message.content
    
    return {"recommendation": answer}

# Graph
graph = StateGraph(ContainerState)
graph.add_node("fetch_status", fetch_status)
graph.add_node("classify_risk", classify_risk)
graph.add_node("calculate_charges", calculate_charges)
graph.add_node("recommend", recommend)

graph.set_entry_point("fetch_status")
graph.add_edge("fetch_status", "classify_risk")
graph.add_edge("classify_risk", "calculate_charges")
graph.add_edge("calculate_charges", "recommend")
graph.add_edge("recommend", END)

app = graph.compile()

if __name__ == "__main__":
    result = app.invoke({
        "container_number": "HLCU1234567",
        "days_at_port": 15,
        "risk_level": "",
        "charge_eur": 0.0,
        "recommendation": ""
    })

    print(f"\nRisk Level: {result['risk_level']}")
    print(f"Estimated Charge: EUR{ result['charge_eur']}")
    print("\nFinal recommendation:")
    print(result["recommendation"])




  