import json
from datetime import datetime

content = """
# [Video Anomaly Detection](https://github.com/vt-le/Video-Anomaly-Detection) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

"""


# write table headers
content += "| Title | Date | Venue | Task | Resource |\n"
content += "| --- | --- | --- | --- | --- |\n"

badges = {
    "image": "![](.github/assets/image.svg)",
    "video": "![](.github/assets/video.svg)",
    "3d": "![](.github/assets/3d.svg)",
    "speech": "![](.github/assets/speech.svg)",
    "others": "![](.github/assets/others.svg)",
    "code": "[![](.github/assets/code.svg)]({})",
    "website": "[![](.github/assets/website.svg)]({})",
}

data = json.loads(open("data.json").read())

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
    # {row['Task']} | {row['Resource']} |\n
    for task in row['Task']:
        content += f"{badges[task.lower()]} "
    content += f"| "
    for k, v in row['Resource'].items():
        content += badges[k.lower()].format(v) + " "
    content += f"| \n"

content += \
"""
🚀 🚀 🚀
"""

with open("README.md", "w") as readme:
    readme.write(content)
