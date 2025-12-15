# NMAE:YOUSIF HUSSSEIN JABBAR AL-GBURI
# ID  :152120231144

import numpy as np
import matplotlib.pyplot as plt

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

# (a) Single-segment Trapezoidal Rule - Figure 21.9(a)
def Trap(h, f0, f1):
    """Single-segment trapezoidal rule"""
    return h * (f0 + f1) / 2

print("-" * 60)
print("EXAMPLE 21.1: Single-Segment Trapezoidal Rule")
print("-" * 60)

h = b - a
f0 = f(a)
f1 = f(b)

I_single = Trap(h, f0, f1)
et_single = abs((exact_value - I_single) / exact_value) * 100

print(f"Using: Trap = h * (f0 + f1) / 2")
print(f"h = {h:.4f}")
print(f"f({a}) = {f0:.4f}")
print(f"f({b}) = {f1:.4f}")
print(f"I = {I_single:.4f}")
print(f"True error εt = {et_single:.1f}%\n")

# (b) Multiple-segment Trapezoidal Rule - Figure 21.9(b)
def Trapm(h, n, f_vals):
    """Multiple-segment trapezoidal rule"""
    sum_val = f_vals[0]  # sum = f0
    for i in range(1, n):  # DOFOR i = 1, n-1
        sum_val = sum_val + 2 * f_vals[i]  # sum = sum + 2 * fi
    sum_val = sum_val + f_vals[n]  # sum = sum + fn
    return h * sum_val / 2  # Trapm = h * sum / 2

print("-" * 60)
print("EXAMPLE 21.2: Multiple-Segment Trapezoidal Rule (n=2)")
print("-" * 60)

n = 2
h2 = (b - a) / n
x = np.linspace(a, b, n+1)
fx = f(x)

I_n2 = Trapm(h2, n, fx)
et_n2 = abs((exact_value - I_n2) / exact_value) * 100

print(f"Using: sum = f0")
print(f"       DOFOR i = 1, n-1: sum = sum + 2*fi")
print(f"       sum = sum + fn")
print(f"       Trapm = h * sum / 2\n")
print(f"n = {n} segments")
print(f"h = {h2:.4f}")
print(f"x values: {x}")
print(f"f(x) values: {fx}")
print(f"I = {I_n2:.4f}")
print(f"True error εt = {et_n2:.1f}%\n")

# EXAMPLE 21.3: Convergence Analysis (Table 21.1)
print("-" * 60)
print("EXAMPLE 21.3: Convergence Analysis (Table 21.1)")
print("-" * 60)
print(f"{'n':>4} {'h':>10} {'I':>12} {'εt (%)':>10}")
print("-" * 60)

n_values = [2, 3, 4, 5, 6, 7, 8, 9, 10]
results = []

for n in n_values:
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    fx = f(x)
    
    I = Trapm(h, n, fx)
    et = abs((exact_value - I) / exact_value) * 100
    
    results.append([n, h, I, et])
    print(f"{n:4d} {h:10.4f} {I:12.4f} {et:9.1f}")

print("=" * 60 + "\n")

# Visualization
results = np.array(results)
fig, axes = plt.subplots(2, 3, figsize=(15, 10))

# Plot 1: Single-segment
x_plot = np.linspace(a, b, 1000)
axes[0, 0].plot(x_plot, f(x_plot), 'b-', linewidth=2, label='f(x)')
x1 = np.array([a, b])
y1 = f(x1)
axes[0, 0].plot(x1, y1, 'ro-', markersize=8, linewidth=2, label='Trapezoid')
axes[0, 0].fill_between(x1, 0, y1, alpha=0.3, color='r')
axes[0, 0].grid(True)
axes[0, 0].set_xlabel('x')
axes[0, 0].set_ylabel('f(x)')
axes[0, 0].set_title('Example 21.1: Single Segment (n=1)')
axes[0, 0].legend()

# Plot 2: Two segments
axes[0, 1].plot(x_plot, f(x_plot), 'b-', linewidth=2, label='f(x)')
n_demo = 2
x_demo = np.linspace(a, b, n_demo+1)
y_demo = f(x_demo)
axes[0, 1].plot(x_demo, y_demo, 'ro-', markersize=8, linewidth=2)
for j in range(n_demo):
    axes[0, 1].fill_between([x_demo[j], x_demo[j+1]], 0, 
                            [y_demo[j], y_demo[j+1]], alpha=0.3, color='r')
axes[0, 1].grid(True)
axes[0, 1].set_xlabel('x')
axes[0, 1].set_ylabel('f(x)')
axes[0, 1].set_title('Example 21.2: Two Segments (n=2)')

# Plot 3: Four segments
axes[0, 2].plot(x_plot, f(x_plot), 'b-', linewidth=2)
n_demo = 4
x_demo = np.linspace(a, b, n_demo+1)
y_demo = f(x_demo)
axes[0, 2].plot(x_demo, y_demo, 'ro-', markersize=8, linewidth=2)
for j in range(n_demo):
    axes[0, 2].fill_between([x_demo[j], x_demo[j+1]], 0, 
                            [y_demo[j], y_demo[j+1]], alpha=0.3, color='r')
axes[0, 2].grid(True)
axes[0, 2].set_xlabel('x')
axes[0, 2].set_ylabel('f(x)')
axes[0, 2].set_title('Four Segments (n=4)')

# Plot 4: Error convergence
axes[1, 0].semilogy(results[:, 0], results[:, 3], 'bo-', markersize=8, linewidth=2)
axes[1, 0].grid(True)
axes[1, 0].set_xlabel('Number of Segments (n)')
axes[1, 0].set_ylabel('True Percent Relative Error (%)')
axes[1, 0].set_title('Example 21.3: Error Convergence')

# Plot 5: Integral estimate convergence
axes[1, 1].plot(results[:, 0], results[:, 2], 'ro-', markersize=8, linewidth=2, label='Trapezoidal Rule')
axes[1, 1].axhline(y=exact_value, color='b', linestyle='--', linewidth=2, label='Exact = 1.640533')
axes[1, 1].grid(True)
axes[1, 1].set_xlabel('Number of Segments (n)')
axes[1, 1].set_ylabel('Integral Estimate')
axes[1, 1].set_title('Convergence to Exact Value')
axes[1, 1].legend()

# Plot 6: Step size vs error
axes[1, 2].loglog(results[:, 1], results[:, 3], 'go-', markersize=8, linewidth=2)
axes[1, 2].grid(True)
axes[1, 2].set_xlabel('Step Size (h)')
axes[1, 2].set_ylabel('True Percent Relative Error (%)')
axes[1, 2].set_title('Error vs Step Size')

plt.suptitle('Trapezoidal Rule Analysis - Examples 21.1, 21.2, and 21.3', 
             fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()
