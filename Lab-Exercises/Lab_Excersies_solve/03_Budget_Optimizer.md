# How I Solved It: Building the Deployment Budget Optimizer

This documentation outlines my step-by-step engineering approach, troubleshooting analysis, and problem-solving workflow for the Deployment Budget Optimizer assignment.

---

## 🧭 The Problem Statement
The objective was to create a modular Python function named `estimate_deployment_cost` capable of calculating total cloud infrastructure spending over a standard 30-day billing cycle. The function must dynamically validate costs against an authorized budget ceiling (`budget_cap`) and return tailored string messages based on validation parameters.

---

## 🛠️ Step-by-Step Implementation & Troubleshooting

### Step 1: Breaking Down the Mathematical Constraints
I first isolated the explicit metrics provided in the system context. To calculate total monthly costs across varying footprints, I defined a standard uptime ceiling representing a 30-day month:

$$\text{Total Monthly Cost} = \text{Instance Count} \times \text{Hourly Rate} \times (30 \text{ Days} \times 24 \text{ Hours})$$

* **Key Solution:** Instead of hardcoding static variables (like fixing instance size to a set number), I maintained abstract parameter values (`instance_count` and `hourly_rate`). This allows the script to evaluate disparate scales dynamically during execution.

### Step 2: Designing the Conditional Decision Matrix
To enforce strict budget policies, I introduced an `if/else` control structure to act as a system gatekeeper. The primary conditional assessment checks whether estimated spending surpasses the threshold:
```python
if monthly_cost > budget_cap:

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

APPROVED: Total Estimated Cost is $1620.00.
REJECTED: Budget Exceeded by $2344.00!