# run_demo.py
import json
DATA = [
  {"model":"GPT-4","success":90,"partial":95,"latency":2.1,"tokens":450},
  {"model":"GPT-3.5","success":75,"partial":82,"latency":1.8,"tokens":420},
  {"model":"LLM X","success":60,"partial":70,"latency":3.5,"tokens":400}
]
with open('../data/results.json','w') as f:
    json.dump(DATA,f,indent=2)
print("Wrote data to ../data/results.json")
