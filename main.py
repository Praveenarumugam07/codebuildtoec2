from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 Hello from CodeArtifact-based Python app in EC2!"

def main():
    app.run(host="0.0.0.0", port=8080)

if __name__ == "__main__":
    main()
