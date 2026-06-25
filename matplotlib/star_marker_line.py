import matplotlib.pyplot as plt


x = [2010, 2015, 2020, 2025]
y = [100, 200, 250, 300]


plt.figure(figsize=(8, 5))


plt.plot(
    x, y,
    color='green',
    marker='*',
    linestyle='dashed',
    linewidth=2,
    markersize=12,
    label='Sales'
)


for i, j in zip(x, y):
    plt.text(i, j + 5, str(j), ha='center')


plt.title("Sales Report", fontsize=16, fontweight='bold')
plt.xlabel("Year", fontsize=12)
plt.ylabel("Sales", fontsize=12)


plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()


plt.tight_layout()

plt.show()