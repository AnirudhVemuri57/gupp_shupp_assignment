
1. Install Python 3.8+
2. (Optional) Create a venv:
   ```bash
   python -m venv venv
   source venv/bin/activate  # on windows: venv\\Scripts\\activate
   pip install flask
   ```
3. Run the examples to see outputs:
   ```bash
   python examples.py
   ```
4. Run the API:
   ```bash
   python app.py
   ```
   - POST JSON `{"messages": [...30 messages...]}` to `http://localhost:5000/extract_memory`
   - POST JSON `{"reply":"your answer","tone":"mentor"}` to `http://localhost:5000/reply`

