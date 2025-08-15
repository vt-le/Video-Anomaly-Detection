import json
from datetime import datetime

content = """
# [Awesomme Video Anomaly Detection](https://github.com/vt-le/Video-Anomaly-Detection) [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)
"""

content += " ## Related works "
content += """HSTforU: See [HSTforU: Anomaly Detection in Aerial and Ground-based Videos with Hierarchical Spatio-Temporal Transformer for U-net
](https://vt-le.github.io/HSTforU/)."""

#content += """
#ASTNet: See [ASTNet: Attention-based Residual Autoencoder for Video Anomaly Detection](https://github.com/vt-le/astnet).
#"""

# write table headers
content += "| Title | Date | Venue | Task | Resource | Model |\n"
content += "| --- | --- | --- | --- | --- | --- |\n"

badges = {
    "image": "![](./assets/image.svg)",
    "video": "![](./assets/video.svg)",
    "3d": "![](./assets/3d.svg)",
    "speech": "![](./assets/speech.svg)",
    "others": "![](./assets/others.svg)",
    "code": "[![](./assets/code.svg)]({})",
    "website": "[![](./assets/website.svg)]({})",
}

data = json.loads(open("./scripts/data.json").read())

# Convert the "Initial Date" from string to datetime object for accurate sorting
for item in data:
    item["Date"] = datetime.strptime(item["Date"], "%Y")

# Sort the items by "Initial Date"
data = sorted(data, key=lambda x: x["Date"])

# Convert the "Initial Date" back to string format for displaying
for item in data:
    item["Date"] = item["Date"].strftime("%Y")

for row in data:
    content += f"| [{row['Title']}]({row['Link']}) | {row['Date']} | {row['Venue']} | "
    # {row['Task']} | {row['Resource']} |\n
    for task in row['Task']:
        content += f"{badges[task.lower()]} "
    content += f"| "
    for k, v in row['Resource'].items():
        if (v != "-"):
            content += badges[k.lower()].format(v) + " "
        else:
            content += "-" + " "
    content += f"| [{row['Model']}]({row['ModelLink']}) |\n"

content += \
"""
🚀 🚀 🚀
"""
content += '''
## Weakly Supervised VAD
'''
# write table headers
content += "| Title | Date | Venue | Task | Resource | Model |\n"
content += "| --- | --- | --- | --- | --- | --- |\n"

data = json.loads(open("./scripts/data_weakly.json").read())

# Convert the "Initial Date" from string to datetime object for accurate sorting
for item in data:
    item["Date"] = datetime.strptime(item["Date"], "%Y")

# Sort the items by "Initial Date"
data = sorted(data, key=lambda x: x["Date"])

# Convert the "Initial Date" back to string format for displaying
for item in data:
    item["Date"] = item["Date"].strftime("%Y")

for row in data:
    content += f"| [{row['Title']}]({row['Link']}) | {row['Date']} | {row['Venue']} | "
    # {row['Task']} | {row['Resource']} |\n
    for task in row['Task']:
        content += f"{badges[task.lower()]} "
    content += f"| "
    for k, v in row['Resource'].items():
        if (v != "-"):
            content += badges[k.lower()].format(v) + " "
        else:
            content += "-" + " "
    content += f"| [{row['Model']}]({row['ModelLink']}) |\n"

content += \
"""
🚀 🚀 🚀
"""
content += '''
## Surveys
'''
# write table headers
content += "| Title | Date | Venue | Task | Resource | Model |\n"
content += "| --- | --- | --- | --- | --- | --- |\n"

data = json.loads(open("./scripts/data_surveys.json").read())

# Convert the "Initial Date" from string to datetime object for accurate sorting
for item in data:
    item["Date"] = datetime.strptime(item["Date"], "%Y")

# Sort the items by "Initial Date"
data = sorted(data, key=lambda x: x["Date"])

# Convert the "Initial Date" back to string format for displaying
for item in data:
    item["Date"] = item["Date"].strftime("%Y")

for row in data:
    content += f"| [{row['Title']}]({row['Link']}) | {row['Date']} | {row['Venue']} | "
    # {row['Task']} | {row['Resource']} |\n
    for task in row['Task']:
        content += f"{badges[task.lower()]} "
    content += f"| "
    for k, v in row['Resource'].items():
        if (v != "-"):
            content += badges[k.lower()].format(v) + " "
        else:
            content += "-" + " "
    content += f"| [{row['Model']}]({row['ModelLink']}) |\n"

content += \
"""
🚀 🚀 🚀
"""
content += '''
## New VAD Datasets
'''
# write table headers
content += "| Title | Date | Venue | Task | Resource | Model |\n"
content += "| --- | --- | --- | --- | --- | --- |\n"

data = json.loads(open("./scripts/data_datasets.json").read())

# Convert the "Initial Date" from string to datetime object for accurate sorting
for item in data:
    item["Date"] = datetime.strptime(item["Date"], "%Y")

# Sort the items by "Initial Date"
data = sorted(data, key=lambda x: x["Date"])

# Convert the "Initial Date" back to string format for displaying
for item in data:
    item["Date"] = item["Date"].strftime("%Y")

for row in data:
    content += f"| [{row['Title']}]({row['Link']}) | {row['Date']} | {row['Venue']} | "
    # {row['Task']} | {row['Resource']} |\n
    for task in row['Task']:
        content += f"{badges[task.lower()]} "
    content += f"| "
    for k, v in row['Resource'].items():
        if (v != "-"):
            content += badges[k.lower()].format(v) + " "
        else:
            content += "-" + " "
    content += f"| [{row['Model']}]({row['ModelLink']}) |\n"

content += \
"""
🚀 🚀 🚀
"""

with open("README.md", "w") as readme:
    readme.write(content)
