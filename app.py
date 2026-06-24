import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="EY Work Email Form",
    page_icon="📧",
    layout="centered",
)

st.title("EY Work Email")
st.caption("Submit your EY work email address.")

FORM_HTML = """
<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      margin: 0;
      padding: 0;
    }
    form {
      display: flex;
      flex-direction: column;
      gap: 12px;
      max-width: 420px;
    }
    label {
      font-weight: 600;
      font-size: 14px;
      color: #31333f;
    }
    input[type="email"] {
      padding: 10px 12px;
      font-size: 16px;
      border: 1px solid #d6d6d6;
      border-radius: 8px;
    }
    input[type="email"]:focus {
      outline: none;
      border-color: #2e2e38;
      box-shadow: 0 0 0 2px rgba(46, 46, 56, 0.15);
    }
    button {
      padding: 10px 16px;
      font-size: 16px;
      font-weight: 600;
      color: #ffffff;
      background: #2e2e38;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      width: fit-content;
    }
    button:hover {
      background: #1a1a22;
    }
    #success {
      display: none;
      color: #0d8050;
      font-weight: 600;
      font-size: 14px;
      margin: 0;
    }
  </style>
</head>
<body>
  <form id="eyForm">
    <label for="email">Work Email</label>
    <input
      type="email"
      id="email"
      name="email"
      placeholder="name@mt.ey.com"
      required
    />
    <button type="submit">Submit</button>
    <p id="success">Thank you! Your email has been submitted.</p>
  </form>

  <script>
    document.getElementById("eyForm").addEventListener("submit", function (e) {
      const email = document.getElementById("email").value.trim();
      const success = document.getElementById("success");

      if (!email.includes("@mt.ey.com")) {
        e.preventDefault();
        success.style.display = "none";
        alert("Please use your EY work email (@mt.ey.com)");
        return;
      }

      e.preventDefault();
      success.style.display = "block";
      document.getElementById("email").value = "";
    });
  </script>
</body>
</html>
"""

components.html(FORM_HTML, height=240, scrolling=False)
