# 🧮 Memory Converter Project

A Python tool and Jupyter notebook designed to **convert between memory units** (bits, bytes, KB, MB, GB, TB) with precision. It demonstrates **unit handling, abstraction, and conversion pipelines** while serving as a practical reference for computing fundamentals.

---

**📌 Project Overview**  
The project simplifies working with digital storage units. It allows the user to input a value and unit, then automatically outputs equivalent values across all other units.  

---

**📝 Code Walkthrough**  
- **Unit Definitions** →  
  - `b` = bit (smallest unit)  
  - `B` = byte (8 bits)  
  - `KB`, `MB`, `GB`, `TB` use base 1024 conversions.  
- **Conversion Logic** →  
  - Convert input to bytes as the base.  
  - Divide by appropriate factor for each target unit.  
- **Outputs** →  
  - Dictionary of results showing the same memory in **all units**, rounded to 2 decimals.  

** Example:**    
```python
print(memory_converter(1, "B"))
# {'b': 8.0, 'B': 1.0, 'KB': 0.0, 'MB': 0.0, 'GB': 0.0, 'TB': 0.0}

---

**⚡Purpose**  

Reinforces core computing fundamentals (bits vs bytes).

Useful as a reference utility when working with data sizes.

Demonstrates how to design clean, reusable functions in Python.

---
**🚀 How to Run**

Clone the repo:

git clone https://github.com/your-username/Memory-Converter.git
cd Memory-Converter


Run the script:

python memory_converter.py

---

**🎯Key Takeaway**
This project shows how small Python utilities can double as learning aids and workflow accelerators. By encoding simple conversions into reusable functions, you remove repetitive work and build stronger intuition for computing systems.
