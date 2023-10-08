import os
import time
import openai
#模型微调
#pip3 install --upgrade openai

openai.api_key = "sk-******"
model_id = "ft:gpt-3.5-turbo-0613:personal::86bqxZ3v"

completion = openai.ChatCompletion.create(
  model=model_id,
  messages=[
    {"role": "system", "content": "this is a Cadence coder"},
    {"role": "user", "content": "Write a Cadence code to get how many Items with itemDataID are minted"}
  ]
)
print(completion.choices[0].message)