## 🧾 Real-World HTML Page Example (Banking Portal Simulation)

Let’s imagine this is a login and dashboard page for an online banking system.

```html
<!-- Save as banking_portal.html -->
<!DOCTYPE html>
<html>
<head>
  <title>MyBank Portal</title>
</head>
<body>
  <h1>Welcome to MyBank</h1>

  <div id="login-box">
    <form id="loginForm">
      <label for="userId">User ID:</label>
      <input type="text" id="userId" name="uid">

      <label for="password">Password:</label>
      <input type="password" id="password" name="pwd">

      <button type="submit" id="loginBtn">Login</button>
    </form>
  </div>

  <div id="dashboard" style="display: none;">
    <h2>Dashboard</h2>
    <p id="welcomeMsg">Hello, John Doe!</p>
    <a href="statement.html" id="viewStmt">View Bank Statement</a>
    <button id="logoutBtn">Logout</button>
  </div>
</body>
</html>
```

---

## ✅ Objective: Automate this page using the most important **browser and navigation** commands in Selenium

We will now:

1. Load the page
2. Interact with elements
3. Navigate between pages
4. Get page info (title, URL, etc.)
5. Close browser tabs/windows

---

## 🚀 Setup (required for all tests)

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()  # Launch Chrome browser
driver.get("file:///C:/Users/YourName/Desktop/banking_portal.html")  # Open local file
```

---

## 1. `driver.get(url)` → Open a webpage

**Purpose:** Launches a webpage (URL or file path)

```python
driver.get("https://example.com")  # Load live site
driver.get("file:///C:/path/to/file.html")  # Load local file
```

🧠 Use Case: Open login page, load dashboard, test local apps.

---

## 2. `driver.title`, `driver.current_url`, `driver.page_source`

**Purpose:** Get **page information**

```python
print(driver.title)         # → MyBank Portal
print(driver.current_url)   # → file:///.../banking_portal.html
print(driver.page_source)   # → Full HTML code
```

🧠 Use Case: Validate page loaded correctly or debug.

---

## 3. `driver.find_element()` → Find **a single web element**

```python
username = driver.find_element(By.ID, "userId")
password = driver.find_element(By.ID, "password")
login_btn = driver.find_element(By.ID, "loginBtn")
```

### Parameters You Can Use:

* `By.ID`
* `By.NAME`
* `By.CLASS_NAME`
* `By.TAG_NAME`
* `By.XPATH`
* `By.CSS_SELECTOR`
* `By.LINK_TEXT` / `PARTIAL_LINK_TEXT`

🧠 Use Case: Automate form fields, buttons, links.

---

## 4. `.send_keys()` → Type into input fields

```python
username.send_keys("john123")
password.send_keys("mypassword")
```

🧠 Use Case: Login forms, search boxes, inputs.

---

## 5. `.click()` → Click a button, link, etc.

```python
login_btn.click()
```

🧠 Use Case: Submit forms, click links, open modals.

---

## 6. `.clear()` → Clear pre-filled input box

```python
username.clear()
```

🧠 Use Case: Clear old text before typing new one.

---

## 7. `driver.back()`, `driver.forward()`, `driver.refresh()`

```python
driver.get("https://google.com")
driver.get("https://github.com")

driver.back()       # Goes to Google
driver.forward()    # Goes back to GitHub
driver.refresh()    # Refreshes GitHub page
```

🧠 Use Case: Simulate browser behavior.

---

## 8. `driver.close()` vs `driver.quit()`

```python
driver.close()  # Closes current tab
driver.quit()   # Closes whole browser
```

🧠 Use Case: Clean up after tests.

---

## 9. `time.sleep(seconds)` (Not Selenium but often used)

```python
time.sleep(2)  # Wait 2 seconds
```

🧠 Use Case: Wait for manual animation or load (use WebDriverWait instead for best practice)

---

## 🧠 Real-World Automation Example With All Commands

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# 1. Open local HTML banking portal
driver.get("file:///C:/Users/YourName/Desktop/banking_portal.html")
print("Title:", driver.title)
print("URL:", driver.current_url)

# 2. Fill login form
driver.find_element(By.ID, "userId").send_keys("john123")
driver.find_element(By.ID, "password").send_keys("mypassword")

# 3. Click login
driver.find_element(By.ID, "loginBtn").click()
time.sleep(2)  # Simulate dashboard loading

# 4. Navigate to another page
driver.get("https://example.com")
driver.back()
driver.forward()
driver.refresh()

# 5. Close browser
driver.quit()
```

---

## 🧪 Use Case Scenarios

| Scenario              | Commands Used                                           |
| --------------------- | ------------------------------------------------------- |
| Login to banking app  | `.get()`, `.find_element()`, `.send_keys()`, `.click()` |
| Validate correct page | `.title`, `.current_url`, `.page_source`                |
| Navigate app sections | `.back()`, `.forward()`, `.refresh()`                   |
| Exit test             | `.close()`, `.quit()`                                   |

---

# ✅ Summary Table – Pareto 80/20 Commands

| Command                              | Description        | Usage                     |
| ------------------------------------ | ------------------ | ------------------------- |
| `get(url)`                           | Open a webpage     | Start browser session     |
| `find_element(By.XXX, "value")`      | Find an element    | Fill forms, click buttons |
| `send_keys()`                        | Type into inputs   | Login, search             |
| `click()`                            | Click elements     | Submit, navigate          |
| `title` / `current_url`              | Get page info      | Verify correct page       |
| `back()` / `forward()` / `refresh()` | Browser navigation | Test browser actions      |
| `clear()`                            | Clear input field  | Reset forms               |
| `close()` / `quit()`                 | End session        | Close tab/browser         |

---

