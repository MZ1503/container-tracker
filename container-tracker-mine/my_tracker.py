"""
Container Tracker v2 — LangGraph Edition

Author: Mariyam Zaidi
Upgraded from: single OpenAI tool-calling script
Upgraded to:   LangGraph StateGraph with 2 nodes 

Architecture:
  [fetch_status] → [classify_risk] → [calculate_charges] → [recommend_action]

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
USE_HUGGINGFACE = True

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
    recommendation: str

# Node 1
def fetch_status(state):
    print(f"Container fetch ho raha hai: {state['container_number']}")
    return {"recommendation": ""}

# Node 2
def recommend(state):
    print("AI se recommendation le raha hai...")
    
    if USE_HUGGINGFACE:
        response = ai_client.chat_completion(
            model="meta-llama/Llama-3.2-3B-Instruct",
            messages=[{
                "role": "user",
                "content": f"Container {state['container_number']} Hamburg port pe hai. Demurrage risk ek line mein batao."
            }],
            max_tokens=100
        )
        answer = response.choices[0].message.content
    else:
        response = ai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{
                "role": "user",
                "content": f"Container {state['container_number']} Hamburg port pe hai. Demurrage risk ek line mein batao."
            }]
        )
        answer = response.choices[0].message.content
    
    return {"recommendation": answer}

# Graph
graph = StateGraph(ContainerState)
graph.add_node("fetch_status", fetch_status)
graph.add_node("recommend", recommend)
graph.set_entry_point("fetch_status")
graph.add_edge("fetch_status", "recommend")
graph.add_edge("recommend", END)

app = graph.compile()

if __name__ == "__main__":
    result = app.invoke({
        "container_number": "HLCU1234567",
        "recommendation": ""
    })
    print("\nFinal recommendation:")
    print(result["recommendation"])