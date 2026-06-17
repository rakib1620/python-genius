# --- LAB 3: THE DEPLOYMENT BUDGET OPTIMIZER ---

def estimate_deployment_cost(instance_count, hourly_rate, budget_cap):
    # 1. Calculate total monthly cost (assuming 30 days * 24 hours = 720 hours)
    monthly_cost = instance_count * hourly_rate * 720
    
    # 2. Implement if/else conditional check against budget_cap
    if monthly_cost > budget_cap:
        # Calculate the exceeded amount dynamically
        over_budget = monthly_cost - budget_cap
        return f"REJECTED: Budget Exceeded by ${over_budget:.2f}!"
    else:
        # Return approval message with the total estimated cost
        return f"APPROVED: Total Estimated Cost is ${monthly_cost:.2f}."

# --- Test Cases to verify your execution ---
print(estimate_deployment_cost(instance_count=5, hourly_rate=0.45, budget_cap=1500.00))
print(estimate_deployment_cost(instance_count=12, hourly_rate=0.85, budget_cap=5000.00))