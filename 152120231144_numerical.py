
# PYTHON IMPLEMENTATION - Figure 21.9 Pseudocode


import numpy as np

# Define the function from Table 21.1
def f(x):
    return 0.2 + 25*x - 200*x**2 + 675*x**3 - 900*x**4 + 400*x**5

# Integration limits
a = 0
b = 0.8
exact_value = 1.640533

print("=" * 60)
print("TRAPEZOIDAL RULE - Examples 21.1, 21.2, and 21.3")
print("=" * 60)
print(f"Function: f(x) = 0.2 + 25x - 200x² + 675x³ - 900x⁴ + 400x⁵")
print(f"Interval: [{a}, {b}]")
print(f"Exact value: {exact_value:.6f}\n")

# ============================================================
# (a) Single-segment Trapezoidal Rule - Figure 21.9(a)
# ============================================================
print("-" * 60)
print("EXAMPLE 21.1: Single-Segment Trapezoidal Rule")
print("-" * 60)

def Trap(h, f0, f1):
    """Single-segment trapezoidal rule"""
    return h * (f0 + f1) / 2

print("Pseudocode: Trap = h * (f0 + f1) / 2\n")

h = b - a
f0 = f(a)
f1 = f(b)

print("Step 1: Calculate h")
print(f"   h = b - a = {b} - {a} = {h:.4f}\n")
print("Step 2: Evaluate function at endpoints")
print(f"   f({a}) = {f0:.4f}")
print(f"   f({b}) = {f1:.4f}\n")
print("Step 3: Apply trapezoidal rule")
print(f"   I = h * (f0 + f1) / 2")
print(f"   I = {h:.4f} * ({f0:.4f} + {f1:.4f}) / 2")

I_single = Trap(h, f0, f1)
print(f"   I = {I_single:.4f}\n")

et_single = abs((exact_value - I_single) / exact_value) * 100
print("Step 4: Calculate error")
print(f"   εt = |({exact_value:.6f} - {I_single:.4f}) / {exact_value:.6f}| * 100%")
print(f"   εt = {et_single:.1f}%\n")

# ============================================================
# (b) Multiple-segment Trapezoidal Rule - Figure 21.9(b)
# ============================================================
print("-" * 60)
print("EXAMPLE 21.2: Multiple-Segment Trapezoidal Rule (n=2)")
print("-" * 60)

def Trapm(h, n, f_vals):
    """Multiple-segment trapezoidal rule"""
    sum_val = f_vals[0]  # sum = f0
    for i in range(1, n):  # DOFOR i = 1, n-1
        sum_val = sum_val + 2 * f_vals[i]  # sum = sum + 2 * fi
    sum_val = sum_val + f_vals[n]  # sum = sum + fn
    return h * sum_val / 2  # Trapm = h * sum / 2

print("Pseudocode:")
print("   sum = f0")
print("   DOFOR i = 1, n-1")
print("      sum = sum + 2 * fi")
print("   END DO")
print("   sum = sum + fn")
print("   Trapm = h * sum / 2\n")

n = 2
h2 = (b - a) / n
x = np.linspace(a, b, n+1)
fx = f(x)

print("Step 1: Calculate h and x values")
print(f"   n = {n} segments")
print(f"   h = (b - a) / n = ({b} - {a}) / {n} = {h2:.4f}\n")
print("Step 2: Generate x values and evaluate function")
print(f"   x values: {x}")
print(f"   f(x) values: {fx}\n")

print("Step 3: Apply multiple-segment formula")
sum_val = fx[0]
print(f"   sum = f({x[0]}) = {fx[0]:.4f}")
for i in range(1, n):
    sum_val = sum_val + 2 * fx[i]
    print(f"   sum = sum + 2 * f({x[i]:.2f}) = {sum_val:.4f}")
sum_val = sum_val + fx[n]
print(f"   sum = sum + f({x[n]}) = {sum_val:.4f}\n")

I_n2 = Trapm(h2, n, fx)
print("Step 4: Calculate integral")
print(f"   I = h * sum / 2 = {h2:.4f} * {sum_val:.4f} / 2 = {I_n2:.4f}\n")

et_n2 = abs((exact_value - I_n2) / exact_value) * 100
print("Step 5: Calculate error")
print(f"   εt = {et_n2:.1f}%\n")

# ============================================================
# EXAMPLE 21.3: Convergence Analysis (Table 21.1)
# ============================================================
print("-" * 60)
print("EXAMPLE 21.3: Convergence Analysis (Table 21.1)")
print("-" * 60)
print("Testing multiple values of n to show convergence:\n")
print(f"{'n':>4} {'h':>10} {'I':>12} {'εt (%)':>10}")
print("-" * 60)

n_values = [2, 3, 4, 5, 6, 7, 8, 9, 10]

for n in n_values:
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    fx = f(x)
    
    I = Trapm(h, n, fx)
    et = abs((exact_value - I) / exact_value) * 100
    
    print(f"{n:4d} {h:10.4f} {I:12.4f} {et:9.1f}")

print("-" * 60)
print("\nObservations:")
print("• As n increases, h decreases")
print(f"• As n increases, the integral estimate approaches {exact_value:.6f}")
print("• As n increases, the error decreases")
print(f"• From n=2 to n=10, error reduces from {et_n2:.1f}% to {et:.1f}%")
print("=" * 60)
