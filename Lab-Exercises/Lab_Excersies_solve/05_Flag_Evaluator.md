# How I Solved It: System Alert Flag Evaluator

This documentation explains how I built an automated server monitoring logic using Python's complex boolean operators (`and`, `or`, `not`).

---

## 🧭 The Problem
We needed to create a system that decides whether to send an urgent alert (`should_alert = True`) to an engineer based on three server conditions:
1. If the server is **not active** (`is_active` is False).
2. If the CPU usage is **critically high** (`cpu_percent > 90.0`) **AND** it is a **production** environment (`is_production` is True).

---

## 🛠️ Step-by-Step Solution

### Step 1: Handling "NOT" Logic
To check if the server is down, I used the `not` operator. It turns a `False` status into `True` so the alert triggers when the server stops:
```python
not is_active
cpu_percent > 90.0 and is_production
should_alert = (not is_active) or (cpu_percent > 90.0 and is_production)

# System metrics
is_active = True
cpu_percent = 94.5
is_production = True

# Complex boolean evaluation
should_alert = (not is_active) or (cpu_percent > 90.0 and is_production)

# Final decision output
if should_alert:
    print("[ALERT] Urgent dispatch! System needs manual intervention.")
else:
    print("[OK] System operating within safe margin bounds.")

[ALERT] Urgent dispatch! System needs manual intervention.