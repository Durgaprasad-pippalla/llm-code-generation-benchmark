LLM Code Generation Benchmark Report
Performance Evaluation of GPT-4, GPT-3.5, and LLM X
Author: Venkata Sai Durga prasad Pippalla
Date: November 2025
1. Introduction
Large Language Models (LLMs) are increasingly used in software engineering workflows to automate
code generation, refactoring, debugging, and API development. However, not all LLMs perform equally
across different types of coding tasks.
This report benchmarks three models:
- GPT-4 – most accurate and capable
- GPT-3.5 – faster and cheaper
- LLM X – cost-optimized lightweight model
The goal of this study is to compare these models on accuracy, partial correctness, latency, and token
usage across 100 code-generation tasks.
2.Benchmark Design
The benchmark covers 100 coding tasks across:
Algorithmic Tasks
- Sorting, searching, dynamic programming, recursion
- BFS, DFS, graph problems
Data Structure Manipulation
- Linked lists, binary trees, stacks, queues
- Hash maps and array transformations
API & Web Development Tasks
- REST API handlers
- JSON parsing
- Error-handling logic
Edge Case & Robustness Tasks
- Invalid input handling
- Boundary tests
- Resource management
Each model receives the same prompt, same temperature (0), and same instructions.
3.Evaluation Methodology
Metrics:
Success Rate – % of tasks where all test cases passed
Partial Pass Rate – % of tasks with ≥50% test cases passed
Mean Latency – End-to-end time to generate response
Average Tokens – Token count of the model’s output (cost impact)
Execution Conditions:
- All models evaluated under identical prompt format
- Results collected over 14 days to reduce API noise
- All generated code tested using automated test suites
4.Results Summary
Performance Table:
GPT-4: 90% success, 95% partial, 2.1s latency, 450 tokens
GPT-3.5: 75% success, 82% partial, 1.8s latency, 420 tokens
LLM X: 60% success, 70% partial, 3.5s latency, 400 tokens
5.Analysis
Accuracy:
GPT-4 performs best with 90% success.
LLM X struggles with recursion and multi-step logic.
Partial Pass Behavior:
GPT-4: fewer near-correct attempts.
GPT-3.5: many “almost correct” outputs.
LLM X: syntax-correct but logically wrong outputs.
Latency:
GPT-3.5 is fastest (1.8s). GPT-4 slower but acceptable. LLM X is slowest.
Token Usage:
GPT-4 → most detailed; LLM X → most concise.
6.Recommendations
Use GPT-4 for:
- Production code
- Algorithms
Use GPT-3.5 for:
- Fast suggestions
- Mid-level tasks
Use LLM X for:
Simple, low-cost tasks
7.Conclusion
GPT-4 is the most capable model overall. GPT-3.5 balances speed and accuracy. LLM X is
cost-efficient but unreliable for complex logic.
8.Reproducibility
Run:
python run_demo.py
python make_plots.py
