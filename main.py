import os
from dotenv import load_dotenv
import ollama
from langchain_community.llms import Ollama
from langchain_ollama import OllamaLLM

load_dotenv()
"""
res = ollama.generate(
    model="hf.co/bartowski/Llama-3.2-3B-Instruct-uncensored-GGUF:Q5_K_S",
    # model="qwen2.5:3b",
    prompt="what was our previous conversation?",
    system="only funny responses",
    # options={'num_predict': 50}
)

print("\n",res['response'],"\n")
"""

model = OllamaLLM(
    model=os.getenv('OLLAMA_MODEL_1', ''),
    # metadata={"num_predict": 50},
    num_predict=50,
    # num_ctx=50 
)

prompt_input = "Why did the tomato cry?"
response = model.invoke(prompt_input)

print("\n",response,"\n")

# git remote set-url hf https://TITAN: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@huggingface.co/spaces/faizal-doc/Project-TITAN

""" .env
__pycache__/
*.pyc
"""