import urllib.request
import json

url = "https://script.google.com/macros/s/AKfycbwpWPcO5rDCNAR37nuftSFDTdowAMFff0ULhbUvm_8107L_agTUj1rmcOpU2y_wKnX-/exec"
data = json.dumps({"name": "Test", "rating": 5, "text": "Test", "date": "14. 5. 2026"}).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={'Content-Type': 'text/plain;charset=utf-8'}, method='POST')

try:
    with urllib.request.urlopen(req) as response:
        print("Response:", response.read().decode('utf-8'))
except Exception as e:
    print("Error:", e)
