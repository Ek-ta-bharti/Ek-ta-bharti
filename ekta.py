import datetime
import requests
import numpy as np
import matplotlib.pyplot as plt

# GitHub username
username = "Ek-ta-bharti"

# GitHub API endpoint for contributions
url = f"https://api.github.com/users/{username}/events"

# Fetching contributions from GitHub API
response = requests.get(url)
data = response.json()

# Initializing contribution dictionary
contributions = {}

# Extracting contributions from fetched data
for event in data:
    date = event["created_at"][:10]
    if date not in contributions:
        contributions[date] = 1
    else:
        contributions[date] += 1

# Converting contributions dictionary to 2D array
dates = sorted(contributions.keys())
start_date = datetime.datetime.strptime(dates[0], "%Y-%m-%d")
end_date = datetime.datetime.strptime(dates[-1], "%Y-%m-%d")
num_days = (end_date - start_date).days + 1
contribution_matrix = np.zeros((7, num_days))

for i, date in enumerate(dates):
    day = (datetime.datetime.strptime(date, "%Y-%m-%d") - start_date).days
    weekday = datetime.datetime.strptime(date, "%Y-%m-%d").weekday()
    contribution_matrix[weekday, day] = contributions[date]

# Plotting the 3D isometric contribution graph
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection="3d")

_x = np.arange(num_days)
_y = np.arange(7)
_xx, _yy = np.meshgrid(_x, _y)
x, y = _xx.ravel(), _yy.ravel()

top = contribution_matrix.ravel()
bottom = np.zeros_like(top)
width = depth = 1

ax.bar3d(x, y, bottom, width, depth, top, shade=True)
ax.set_title("GitHub Contributions")
ax.set_xlabel("Day")
ax.set_ylabel("Weekday")
ax.set_zlabel("Contributions")

plt.show()
