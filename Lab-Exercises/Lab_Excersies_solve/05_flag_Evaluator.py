# --- LAB 5: SYSTEM ALERT FLAG EVALUATOR ---

# Change these values to verify different execution paths!
is_active = True
cpu_percent = 94.5
is_production = True

# Compound logical condition checking system flags
should_alert = (not is_active) or (cpu_percent > 90.0 and is_production)

# Control execution state based on the evaluations
if should_alert:
    print("[ALERT] Urgent dispatch! System needs manual intervention.")
else:
    print("[OK] System operating within safe margin bounds.")