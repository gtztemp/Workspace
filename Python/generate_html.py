from markdown2 import markdown

# Load your markdown content
with open("guide.md", "r", encoding="utf-8") as f:
    markdown_content = f.read()

# Convert Markdown to HTML
html_content = markdown(markdown_content)

# Apply dark theme styling
html_wrapped = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Python Beginner Guide</title>
    <style>
        body {{
            font-family: "Segoe UI", sans-serif;
            background-color: #1e1e1e;
            color: #d4d4d4;
            line-height: 1.6;
            padding: 40px;
        }}
        h1, h2, h3 {{
            color: #4ec9b0;
        }}
        code {{
            background-color: #252526;
            color: #dcdcaa;
            padding: 2px 6px;
            border-radius: 4px;
        }}
        pre {{
            background-color: #1e1e1e;
            color: #dcdcdc;
            padding: 10px;
            border-radius: 6px;
            overflow-x: auto;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 0.95em;
        }}
        th, td {{
            border: 1px solid #3c3c3c;
            padding: 8px 12px;
        }}
        th {{
            background-color: #333;
            color: #dcdcaa;
        }}
        td {{
            background-color: #2d2d2d;
        }}
        blockquote {{
            background-color: #264f78;
            color: #ffffff;
            padding: 15px;
            border-left: 6px solid #007acc;
            margin-top: 30px;
        }}
    </style>
</head>
<body>
{html_content}
</body>
</html>
"""

# Save to HTML file
with open("Python_Beginner_Guide_Dark.html", "w", encoding="utf-8") as f:
    f.write(html_wrapped)

print("✅ HTML file generated: Python_Beginner_Guide_Dark.html")

