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