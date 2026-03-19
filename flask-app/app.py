from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    forwarded_user = request.headers.get("X-Forwarded-User", "Not provided")
    forwarded_email = request.headers.get("X-Forwarded-Email") or "Not sent by oauth2-proxy in current config"
    auth_header = request.headers.get("Authorization", "Not provided")

    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <title>SSO Demo App</title>
      <style>
        body {{
          font-family: Arial, sans-serif;
          max-width: 800px;
          margin: 40px auto;
          line-height: 1.5;
        }}
        code {{
          background: #f4f4f4;
          padding: 2px 6px;
          border-radius: 4px;
        }}
        .box {{
          background: #f9f9f9;
          border: 1px solid #ddd;
          padding: 16px;
          border-radius: 8px;
          margin-top: 20px;
        }}
      </style>
    </head>
    <body>
      <h1>SSO Demo App</h1>
      <p>You reached this app through <strong>OIDC SSO</strong>.</p>

      <div class="box">
        <p><strong>X-Forwarded-User:</strong> <code>{forwarded_user}</code></p>
        <p><strong>X-Forwarded-Email:</strong> <code>{forwarded_email}</code></p>
        <p><strong>Authorization header present:</strong> <code>{"Yes" if auth_header != "Not provided" else "No"}</code></p>
      </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)