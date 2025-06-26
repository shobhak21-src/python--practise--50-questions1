
import numpy as np

# Q1
q1 = np.zeros(10)
q1[::2] = 5
print("Q1:", q1)

# Q2
q2 = np.eye(3)
print("\nQ2:", q2)

# Q3
q3 = np.linspace(1, 10, 20)
print("\nQ3:", q3)

# Q4
q4 = np.array([[1, 2], [3, 4]])
print("\nQ4:")
print("Array:", q4)
print("Shape:", q4.shape)
print("Dimensions:", q4.ndim)
print("Data type:", q4.dtype)

# Q5
q5 = np.array([1, 2, 3, 4]) * 3
print("\nQ5:", q5)

# Q6
q6 = np.arange(1, 16)[::3]
print("\nQ6:", q6)

# Q7
q7 = np.arange(1, 17).reshape(4, 4)
print("\nQ7:")
print("Matrix:\n", q7)
print("Second row:", q7[1])
print("Third column:", q7[:, 2])

# Q8
q8 = np.arange(1, 17).reshape(4, 4)
print("\nQ8:", q8)

# Q9
q9 = np.arange(1, 10).reshape(3, 3).flatten()
print("\nQ9:", q9)

# Q10
q10 = np.random.randint(5, 20, size=(5, 5))
q10[q10 > 10] = 10
print("\nQ10:", q10)

# Q11
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 4, 3, 2, 1])
print("\nQ11:")
print("Add:", a + b)
print("Subtract:", a - b)
print("Multiply:", a * b)
print("Divide:", a / b)

# Q12
q12 = np.arange(1, 10).reshape(3, 3) * 5
print("\nQ12:", q12)

# Q13
arr = np.array([[1, 2, 3], [4, 5, 6]])
row_mean = arr.mean(axis=1, keepdims=True)
q13 = arr - row_mean
print("\nQ13:", q13)

# Q14
q14 = np.random.rand(5, 3)
q14_norm = (q14 - q14.min()) / (q14.max() - q14.min())
print("\nQ14:", q14_norm)

# Q15
arr15 = np.arange(1, 11)
arr15[arr15 % 2 == 0] += 7
print("\nQ15:", arr15)

# Q16
scores = np.array([60, 70, 85, 90, 95])
print("\nQ16:")
print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Std Dev:", np.std(scores))

# Q17
x = np.array([1, 2, 3])
y = np.array([5, 10, 15])
print("\nQ17: Correlation Coefficient Matrix:\n", np.corrcoef(x, y))

# Q18
data = np.array([10, 20, 30, 40, 50])
print("\nQ18:")
print("25th percentile:", np.percentile(data, 25))
print("50th percentile:", np.percentile(data, 50))
print("75th percentile:", np.percentile(data, 75))

# Q19
arr19 = np.array([1, 3, 7, 8, 10, 15])
mean19 = arr19.mean()
count_above_mean = np.sum(arr19 > mean19)
print("\nQ19: Values above average:", count_above_mean)

# Q20
ages = np.array([12, 17, 18, 21, 16])
print("\nQ20: Minors count:", np.sum(ages < 18))

# Q21
arr21 = np.array([1, np.nan, 3, np.nan, 5])
mean21 = np.nanmean(arr21)
arr21[np.isnan(arr21)] = mean21
print("\nQ21:", arr21)

# Q22
arr22 = np.array([1, 2, np.nan, 4])
cleaned = arr22[~np.isnan(arr22)]
print("\nQ22 Mean:", np.mean(cleaned))

# Q23
arr23 = np.array([5, -3, 7, -1, 2])
arr23[arr23 < 0] = 0
print("\nQ23:", arr23)

# Q24
arr24 = np.array([1, 2, np.nan])
print("\nQ24 Contains NaN:", np.any(np.isnan(arr24)))

# Q25
arr25 = np.array([10, 12, 14, 100, 16])
mean25 = np.mean(arr25)
std25 = np.std(arr25)
arr25[arr25 > mean25 + 2 * std25] = mean25
print("\nQ25:", arr25)

# Q26 (Simulated CSV Load)
from io import StringIO
csv_data = "1,2,3\n4,5,6\n7,8,9"
data26 = np.loadtxt(StringIO(csv_data), delimiter=",")
print("\nQ26 Loaded CSV:\n", data26)

# Q27
np.savetxt("q27_saved.csv", np.array([[1, 2], [3, 4]]), delimiter=",", fmt='%d')
print("\nQ27: Saved a file named 'q27_saved.csv'")

# Q28
temp_data = np.array([28, 31, 26, 33, 30])
print("\nQ28:")
print("Max Temp:", np.max(temp_data))
print("Min Temp:", np.min(temp_data))
print("Average Temp:", np.mean(temp_data))

# Q29
data29 = np.array([80, 90, 150, 200, 95])
print("\nQ29 > 100:", np.sum(data29 > 100))

# Q30
csv_nan_data = "1,2,3\n4,NaN,6\n7,8,9"
data30 = np.genfromtxt(StringIO(csv_nan_data), delimiter=",")
data30 = np.nan_to_num(data30)
print("\nQ30 Cleaned Data:\n", data30)

# Q31
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[2, 0], [1, 2]])
print("\nQ31 Matrix Multiplication:\n", np.dot(mat1, mat2))

# Q32
mat = np.array([[1, 2], [3, 4]])
inv_mat = np.linalg.inv(mat)
print("\nQ32 Inverse:\n", inv_mat)

# Q33
A = np.array([[3, 1], [1, 2]])
B = np.array([9, 8])
sol = np.linalg.solve(A, B)
print("\nQ33 Solution:", sol)

# Q34
m = np.array([[1, 2], [3, 4]])
print("\nQ34:")
print("Determinant:", np.linalg.det(m))
print("Rank:", np.linalg.matrix_rank(m))

# Q35
m35 = np.array([[4, -2], [1, 1]])
eigvals = np.linalg.eigvals(m35)
print("\nQ35 Eigenvalues:", eigvals)

# Q36
revenue = np.array([1000, 1200, 1100, 1300, 1400])
growth = np.diff(revenue) / revenue[:-1] * 100
print("\nQ36 Monthly Growth %:", growth.round(2))

# Q37
steps = np.array([1000, 3000, 5000, 4000, 6000])
moving_avg = np.convolve(steps, np.ones(3)/3, mode='valid')
print("\nQ37 Moving Avg:", moving_avg)

# Q38
scores38 = np.array([[80, 70], [90, 95], [60, 75], [85, 80]])
total = np.sum(scores38, axis=1)
top_3_idx = np.argsort(total)[-3:][::-1]
print("\nQ38 Top 3 Students Index:", top_3_idx)

# Q39
rainfall = np.array([10, 15, 5, 20, 18])
above_avg_rain = np.sum(rainfall > np.mean(rainfall))
print("\nQ39 Days with above-average rain:", above_avg_rain)

# Q40
stock = np.array([100, 105, 110, 115, 90])
change = np.diff(stock) / stock[:-1] * 100
print("\nQ40 Days with >5% increase:", np.sum(change > 5))
