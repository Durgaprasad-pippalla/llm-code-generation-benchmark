LLM Code Generation Benchmark
This project benchmarks the performance of three Large Language Models — GPT-4, GPT-3.5, and LLM X — across 100 code-generation tasks.
It includes a reproducible evaluation pipeline, experiment scripts, plots, and a detailed technical report.
llm-code-generation-benchmark/
│
├── article/
│   └── LLM_Benchmark_Report.md     ← Technical article (main deliverable)
│
├── experiments/
│   ├── run_demo.py                 ← Runs benchmark on sample prompts
│   ├── make_plots.py               ← Generates benchmark plots
│   └── requirements.txt            ← Dependencies
│
├── plots/                          ← Benchmark charts
│   ├── latency.png
│   ├── tokens.png
│   ├── success_partial.png
│   └── timeline.png
│
└── README.md                       ← Reproduction instructions
