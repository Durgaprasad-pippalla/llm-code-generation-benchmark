# make_plots.py
import json, os
import matplotlib.pyplot as plt

os.makedirs('../plots', exist_ok=True)
with open('../data/results.json') as f:
    data = json.load(f)

models = [d['model'] for d in data]
success = [d['success'] for d in data]
partial = [d['partial'] for d in data]
latency = [d['latency'] for d in data]
tokens = [d['tokens'] for d in data]

# success / partial
plt.figure(figsize=(9,5))
x = range(len(models))
plt.bar([p-0.2 for p in x], success, width=0.35, label='Success')
plt.bar([p+0.2 for p in x], partial, width=0.35, label='Partial')
plt.xticks(x, models)
plt.ylabel('Percent')
plt.legend()
plt.savefig('../plots/success_partial.png', bbox_inches='tight')

# latency
plt.figure(figsize=(9,5))
plt.bar(models, latency)
plt.ylabel('Seconds')
plt.savefig('../plots/latency.png', bbox_inches='tight')

# tokens
plt.figure(figsize=(9,5))
plt.bar(models, tokens)
plt.ylabel('Tokens')
plt.savefig('../plots/tokens.png', bbox_inches='tight')

print("Saved plots to ../plots/")
