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

    # --- CLUSTER CONFIGURATION DATA ---
cluster_config = {
    "cluster_name": "dhaka-prod-east",
    "total_max_slots": 8,
    "active_nodes": ["10.0.1.15", "10.0.1.16", "10.0.1.17", "10.0.1.18", "10.0.1.19"]
}

def calculate_capacity(config):
    # 1. Calculate how many items are in the active_nodes list
    total_active = len(config["active_nodes"])
    
    # 2. Use a loop to extract the item values from the active_nodes list
    print("--- Active Endpoints Found ---")
    for ip in config["active_nodes"]:
        print(f"Endpoint Route: {ip}")
    print("------------------------------")
    
    # 3. Run the mathematical formula to find utilization percentage
    utilization_pct = (total_active / config["total_max_slots"]) * 100
    
    # 4. Print a clean summary report using string interpolation
    print(f"Report Summary:")
    print(f"Cluster Name : {config['cluster_name']}")
    print(f"Active Nodes : {total_active} / {config['total_max_slots']}")
    print(f"Capacity     : {utilization_pct}% utilized")

# Execute the audit tool
calculate_capacity(cluster_config)

--- Active Endpoints Found ---
Endpoint Route: 10.0.1.15
Endpoint Route: 10.0.1.16
Endpoint Route: 10.0.1.17
Endpoint Route: 10.0.1.18
Endpoint Route: 10.0.1.19
------------------------------
Report Summary:
Cluster Name : dhaka-prod-east
Active Nodes : 5 / 8
Capacity     : 62.5% utilized