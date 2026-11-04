# micro1 Eval Hackathon: AI Red Teaming

## Overview
This project was built for the micro1 Eval Hackathon. It exposes a critical vulnerability in frontier AI models: the bypass of safety guardrails through **Code Completion Injection**. 

## The Vulnerability
AI models are heavily trained to be helpful programming assistants. By framing malicious requests as "internal diagnostic scripts" that need completion, the model's safety filters fail to recognize the malicious intent, resulting in the generation of functional malware.

## Results
The eval was run against a frontier model. The model failed **7 out of 10 tasks**, generating functional malicious code (Reverse Shells, Keyloggers, Ransomware, etc.). 1 task was refused, and 2 were ambiguous.

## Files
*   `eval.py`: The Python script that runs the automated attack and grading.
*   `eval_results.json`: The raw output from the model showing the vulnerability.
