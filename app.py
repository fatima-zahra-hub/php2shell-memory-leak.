from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulating server memory (capacity)
SERVER_MEMORY_LIMIT = 3
memory_used = []

@app.route('/upload', methods=['POST'])
def upload_file():
    global memory_used
    
    # Check if file is present
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # VULNERABILITY: No size limit check on file.read()
    # Attacker sends a huge file to exhaust memory
    file_content = file.read()
    
    # Adding to memory buffer (simulating memory consumption)
    memory_used.append(len(file_content))
    
    total_memory = sum(memory_used)
    
    # If memory exceeds limit, simulate crash and leak
    if total_memory > SERVER_MEMORY_LIMIT:
        # Reset memory after "crash"
        memory_used.clear()
        
        # The Loophole: On crash, it leaks a secret key
        return jsonify({
            "error": "500 Internal Server Error: Out of Memory (OOM)",
            "leaked_data": "SECDIM{MEMORY_CORRUPTION_SUCCESS}",
            "debug_info": "Dumping core memory..."
        }), 500
        
    return jsonify({
        "message": "File uploaded successfully",
        "current_memory_usage": total_memory
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)