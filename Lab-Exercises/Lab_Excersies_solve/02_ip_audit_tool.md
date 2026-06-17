# How I Solved It: Building the Cluster IP Audit Tool

This documentation details my step-by-step process, troubleshooting journey, and the core programming concepts applied to solve the Cluster Capacity Assignment.

---

## 🧭 The Problem Statement
The goal was to create a reusable Python function named `calculate_capacity` that takes a cluster configuration dictionary, extracts the active nodes, runs a capacity utilization formula, and prints an audit report.

---

## 🛠️ Step-by-Step Implementation & Troubleshooting

### Step 1: Handling Function Parameters & Arguments
I started by analyzing how the function interacts with external data. Instead of hardcoding the cluster metrics inside the function, I utilized a placeholder parameter named `config`. 
* **Concept Learned:** When calling `calculate_capacity(cluster_config)`, the real dictionary data (`cluster_config`) is passed as an **argument** into the `config` **parameter** container. This ensures the function remains modular and reusable for multiple cluster sites.

### Step 2: Extracting Nested Data via Loops
To audit each node individually, I implemented a sequential `for` loop targeted specifically at the list of IPs nested within the dictionary structure:
```python
for ip in config["active_nodes"]:
    print(f"Endpoint Route: {ip}")