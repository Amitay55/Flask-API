from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # מאפשר גישה מרחוק

# פונקציה ליצירת פרויקט חדש
@app.route('/create_project', methods=['GET', 'POST'])
def create_project():
    if request.method == 'GET':
        return jsonify({"message": "This is the create_project endpoint. Use POST to send data."})
    
    data = request.json  # מקבל את הבקשה מה-GPT
    project_name = data.get("project_name", "MyProject")
    
    # כאן אפשר להוסיף לוגיקה של יצירת קובץ (למשל, יצירת ZIP, APK וכו')
    file_link = f"https://your-server.com/files/{project_name}.zip"

    return jsonify({"status": "success", "download_link": file_link})

# פונקציה לבדיקה מקדימה
@app.route('/preview_live', methods=['GET', 'POST'])
def preview_live():
    if request.method == 'GET':
        return jsonify({"message": "This is the preview_live endpoint. Use POST to send data."})

    data = request.json
    preview_link = f"https://your-preview-server.com/{data.get('project_name', 'default')}"
    return jsonify({"status": "success", "preview_link": preview_link})

# פונקציה להורדת קובץ
@app.route('/download_project', methods=['GET', 'POST'])
def download_project():
    if request.method == 'GET':
        return jsonify({"message": "This is the download_project endpoint. Use POST to send data."})

    data = request.json
    file_link = f"https://your-server.com/files/{data.get('project_name', 'default')}.zip"
    return jsonify({"status": "success", "download_link": file_link})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
