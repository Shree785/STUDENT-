"""
Setup script to create all necessary files and folders for the Flask app
Run this script first: python setup.py
"""
import os

# Create templates directory
if not os.path.exists('templates'):
    os.makedirs('templates')
    print("✓ Created 'templates' folder")
else:
    print("✓ 'templates' folder already exists")

# Create index.html
index_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Performance Analyzer</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            max-width: 500px;
            width: 100%;
        }
        h1 { color: #333; margin-bottom: 30px; text-align: center; }
        .form-group { margin-bottom: 20px; }
        label {
            display: block;
            margin-bottom: 8px;
            color: #555;
            font-weight: 600;
        }
        input {
            width: 100%;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 8px;
            font-size: 16px;
            transition: border-color 0.3s;
        }
        input:focus { outline: none; border-color: #667eea; }
        button {
            width: 100%;
            padding: 14px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 18px;
            font-weight: 600;
            cursor: pointer;
            transition: transform 0.2s;
        }
        button:hover { transform: translateY(-2px); }
        button:active { transform: translateY(0); }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Student Performance Analyzer</h1>
        <form action="/analyze" method="POST">
            <div class="form-group">
                <label for="name">Student Name:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="maths">Mathematics Score (0-100):</label>
                <input type="number" id="maths" name="maths" min="0" max="100" step="0.01" required>
            </div>
            <div class="form-group">
                <label for="ccl">CCL Score (0-100):</label>
                <input type="number" id="ccl" name="ccl" min="0" max="100" step="0.01" required>
            </div>
            <div class="form-group">
                <label for="spcc">SPCC Score (0-100):</label>
                <input type="number" id="spcc" name="spcc" min="0" max="100" step="0.01" required>
            </div>
            <button type="submit">Analyze Performance</button>
        </form>
    </div>
</body>
</html>"""

with open('templates/index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
print("✓ Created 'templates/index.html'")

# Create result.html
result_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Analysis Results</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }
        h1 { color: #333; margin-bottom: 10px; text-align: center; }
        .student-name {
            text-align: center;
            color: #667eea;
            font-size: 24px;
            margin-bottom: 30px;
            font-weight: 600;
        }
        .scores-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 40px;
        }
        .score-card {
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        .score-card h3 { color: #333; margin-bottom: 10px; }
        .current-score {
            font-size: 32px;
            color: #667eea;
            font-weight: bold;
            margin: 10px 0;
        }
        .predicted-score {
            font-size: 24px;
            color: #28a745;
            font-weight: 600;
            margin-top: 10px;
        }
        .improvement { color: #666; font-size: 14px; margin-top: 5px; }
        .history { margin-top: 40px; }
        .history h2 { color: #333; margin-bottom: 20px; }
        table {
            width: 100%;
            border-collapse: collapse;
            background: white;
        }
        th, td {
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }
        th {
            background: #667eea;
            color: white;
            font-weight: 600;
        }
        tr:hover { background: #f5f5f5; }
        .btn-back {
            display: inline-block;
            margin-top: 30px;
            padding: 12px 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            transition: transform 0.2s;
        }
        .btn-back:hover { transform: translateY(-2px); }
    </style>
</head>
<body>
    <div class="container">
        <h1>📈 Performance Analysis</h1>
        <div class="student-name">{{ name }}</div>
        
        <div class="scores-container">
            <div class="score-card">
                <h3>📐 Mathematics</h3>
                <div class="current-score">{{ maths }}</div>
                <div class="predicted-score">→ {{ prediction.maths }}</div>
                <div class="improvement">+{{ "%.2f"|format(prediction.maths - maths) }}% improvement</div>
            </div>
            
            <div class="score-card">
                <h3>💻 CCL</h3>
                <div class="current-score">{{ ccl }}</div>
                <div class="predicted-score">→ {{ prediction.ccl }}</div>
                <div class="improvement">+{{ "%.2f"|format(prediction.ccl - ccl) }}% improvement</div>
            </div>
            
            <div class="score-card">
                <h3>🖥️ SPCC</h3>
                <div class="current-score">{{ spcc }}</div>
                <div class="predicted-score">→ {{ prediction.spcc }}</div>
                <div class="improvement">+{{ "%.2f"|format(prediction.spcc - spcc) }}% improvement</div>
            </div>
        </div>

        {% if history %}
        <div class="history">
            <h2>📚 Student History</h2>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Maths</th>
                        <th>CCL</th>
                        <th>SPCC</th>
                        <th>Pred. Maths</th>
                        <th>Pred. CCL</th>
                        <th>Pred. SPCC</th>
                    </tr>
                </thead>
                <tbody>
                    {% for record in history %}
                    <tr>
                        <td>{{ record.name }}</td>
                        <td>{{ record.maths }}</td>
                        <td>{{ record.ccl }}</td>
                        <td>{{ record.spcc }}</td>
                        <td>{{ record.pred_maths }}</td>
                        <td>{{ record.pred_ccl }}</td>
                        <td>{{ record.pred_spcc }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        {% endif %}

        <a href="/" class="btn-back">← Analyze Another Student</a>
    </div>
</body>
</html>"""

with open('templates/result.html', 'w', encoding='utf-8') as f:
    f.write(result_html)
print("✓ Created 'templates/result.html'")

# Create error.html
error_html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 40px;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            max-width: 500px;
            width: 100%;
            text-align: center;
        }
        .error-icon { font-size: 64px; margin-bottom: 20px; }
        h1 { color: #dc3545; margin-bottom: 20px; }
        .error-message { color: #666; font-size: 18px; margin-bottom: 30px; }
        .btn-back {
            display: inline-block;
            padding: 12px 30px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-decoration: none;
            border-radius: 8px;
            font-weight: 600;
            transition: transform 0.2s;
        }
        .btn-back:hover { transform: translateY(-2px); }
    </style>
</head>
<body>
    <div class="container">
        <div class="error-icon">⚠️</div>
        <h1>Error</h1>
        <div class="error-message">{{ error }}</div>
        <a href="/" class="btn-back">← Go Back</a>
    </div>
</body>
</html>"""

with open('templates/error.html', 'w', encoding='utf-8') as f:
    f.write(error_html)
print("✓ Created 'templates/error.html'")

print("\n" + "="*50)
print("✅ Setup complete! All files created successfully.")
print("="*50)
print("\nNext steps:")
print("1. Install requirements: pip install -r requirements.txt")
print("2. Run the app: python app.py")
print("3. Open browser: http://127.0.0.1:5000/")
print("\n" + "="*50)