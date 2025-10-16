from flask import Flask, request

app = Flask(__name__)

# Store previous results in memory
history = []

@app.route('/')
def index():
    # Generate HTML for history table
    history_html = ""
    if history:
        history_html = "<h2>📜 Previous Analyses</h2><table border='1' cellpadding='10' style='margin:auto; background:white;'>"
        history_html += "<tr><th>Name</th><th>Maths</th><th>CCL</th><th>SPCC</th><th>Pred Maths</th><th>Pred CCL</th><th>Pred SPCC</th></tr>"
        for record in history:
            history_html += f"<tr><td>{record['name']}</td><td>{record['maths']}</td><td>{record['ccl']}</td><td>{record['spcc']}</td><td>{record['pred_maths']}</td><td>{record['pred_ccl']}</td><td>{record['pred_spcc']}</td></tr>"
        history_html += "</table><br>"

    return f'''
    <html>
    <head>
        <title>Student Performance Analyzer</title>
    </head>
    <body style="font-family: Arial; background: linear-gradient(135deg, #74ebd5 0%, #acb6e5 100%); text-align: center; padding: 40px;">
        <h1>🎓 Student Performance Analyzer</h1>
        <form action="/analyze" method="post" style="background:white;display:inline-block;padding:30px;border-radius:10px;box-shadow:0 4px 20px rgba(0,0,0,0.2);">
            <input type="text" name="name" placeholder="Enter Student Name" required><br><br>
            <input type="number" name="maths" placeholder="Maths Marks (0-100)" required><br><br>
            <input type="number" name="ccl" placeholder="CCL Marks (0-100)" required><br><br>
            <input type="number" name="spcc" placeholder="SPCC Marks (0-100)" required><br><br>
            <button type="submit" style="background:#2196f3;color:white;padding:10px 20px;border:none;border-radius:5px;">Analyze</button>
        </form>
        <br><br>
        {history_html}
    </body>
    </html>
    '''

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        name = request.form.get('name', 'Student')
        maths = float(request.form.get('maths', 0))
        ccl = float(request.form.get('ccl', 0))
        spcc = float(request.form.get('spcc', 0))

        if not (0 <= maths <= 100 and 0 <= ccl <= 100 and 0 <= spcc <= 100):
            return "<h2>❌ Marks must be between 0 and 100.</h2><a href='/'>Go Back</a>"

        # Simple prediction (+10%)
        pred_maths = round(min(maths * 1.1, 100), 2)
        pred_ccl = round(min(ccl * 1.1, 100), 2)
        pred_spcc = round(min(spcc * 1.1, 100), 2)

        # Store in history
        history.append({
            'name': name,
            'maths': maths,
            'ccl': ccl,
            'spcc': spcc,
            'pred_maths': pred_maths,
            'pred_ccl': pred_ccl,
            'pred_spcc': pred_spcc
        })

        return f"""
        <html>
        <head><title>Result</title></head>
        <body style='background: linear-gradient(to right, #43cea2, #185a9d); font-family: Arial; text-align: center; padding: 50px; color:white;'>
            <h1>📊 Performance Report for {name}</h1>
            <table border='1' cellpadding='10' style='margin:auto; background:white; color:black; border-radius:8px;'>
                <tr><th>Subject</th><th>Actual Marks</th><th>Predicted Marks</th></tr>
                <tr><td>Maths</td><td>{maths}</td><td>{pred_maths}</td></tr>
                <tr><td>CCL</td><td>{ccl}</td><td>{pred_ccl}</td></tr>
                <tr><td>SPCC</td><td>{spcc}</td><td>{pred_spcc}</td></tr>
            </table>
            <br><a href='/' style='background:#2196f3;color:white;padding:10px 20px;border-radius:5px;text-decoration:none;'>🔙 Back to Analyzer</a>
        </body>
        </html>
        """

    except Exception as e:
        return f"<h1 style='color:red;'>⚠️ Internal Error:</h1><p>{str(e)}</p><a href='/'>Go Back</a>"

if __name__ == '__main__':
    print("✅ Flask app started at http://127.0.0.1:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)
