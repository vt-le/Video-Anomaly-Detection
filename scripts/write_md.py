import json
from datetime import datetime

content = """
# [Awesome Video Anomaly Detection](https://github.com/vt-le/Video-Anomaly-Dection) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

"""


# write table headers
content += "| Paper | Date | Venue | Task | Resource | Model |\n"
content += "| --- | --- | --- | --- | --- | --- |\n"

badges = {
    "image": "![](./scripts/assets/image.svg)",
    "video": "![](./scripts/assets/video.svg)",
    "3d": "![](./scripts/assets/3d.svg)",
    "speech": "![](./scripts/assets/speech.svg)",
    "others": "![](./scripts/assets/others.svg)",
    "code": "[![](./scripts/assets/code.svg)]({})",
    "website": "[![](./scripts/assets/website.svg)]({})",
}

data = json.loads(open("./scripts/data.json").read())

# Convert the "Initial Date" from string to datetime object for accurate sorting
for item in data:
    item["Date"] = datetime.strptime(item["Date"], "%d %b %Y")

# Sort the items by "Initial Date"
data = sorted(data, key=lambda x: x["Date"])

# Convert the "Initial Date" back to string format for displaying
for item in data:
    item["Date"] = item["Date"].strftime("%d %b %Y")

for row in data:
    content += f"| [{row['Title']}]({row['Link']}) | {row['Date']} | {row['Venue']} | "
    # {row['Task']} | {row['Resource']} | {row['Resource']} |\n
    for task in row['Task']:
        content += f"{badges[task.lower()]} "
    content += f"| "
    for k, v in row['Resource'].items():
        content += badges[k.lower()].format(v) + " "
    content += f"| {row['Venue']}  |\n"

content += \
"""
🚀 🚀 🚀
"""

with open("README.md", "w") as readme:
    readme.write(content)
