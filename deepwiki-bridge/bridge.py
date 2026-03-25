import sys
import json
import requests
import select

URL = "https://mcp.deepwiki.com/mcp"
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json, text/event-stream"
}

def log(msg):
    sys.stderr.write(f"[DeepWiki Bridge] {msg}\n")
    sys.stderr.flush()

def main():
    log("Starting bridge...")
    
    session = requests.Session()

    while True:
        try:
            line = sys.stdin.readline()
            if not line:
                break
                
            line = line.strip()
            if not line:
                continue

            try:
                request_data = json.loads(line)
            except json.JSONDecodeError as e:
                log(f"JSON Decode Error: {e}")
                continue

            log(f"Sending: {line[:100]}...")

            try:
                response = session.post(URL, json=request_data, headers=HEADERS, stream=True, timeout=60)
                response.raise_for_status()

                for chunk_bytes in response.iter_lines():
                    if chunk_bytes:
                        chunk = chunk_bytes.decode('utf-8')
                        
                        if chunk.startswith("data: "):
                            data_content = chunk[6:]
                            print(data_content)
                            sys.stdout.flush()
                        
            except requests.exceptions.RequestException as e:
                log(f"HTTP Request Failed: {e}")
                if "id" in request_data:
                    err = {
                        "jsonrpc": "2.0",
                        "id": request_data["id"],
                        "error": {"code": -32000, "message": str(e)}
                    }
                    print(json.dumps(err))
                    sys.stdout.flush()

        except KeyboardInterrupt:
            break
        except Exception as e:
            log(f"Loop error: {e}")
            break

if __name__ == "__main__":
    main()