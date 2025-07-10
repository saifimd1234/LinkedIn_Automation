Here's your **detailed and concise study notes** on:

* `from selenium.webdriver.common.by import By`
* `from selenium.webdriver.support.ui import WebDriverWait`

Including real-world **use cases**, important **methods**, and **example code** for different automation scenarios.

---

## 🧠 1. `from selenium.webdriver.common.by import By`

### ✅ What is `By`?

`By` is a class provided by Selenium to **locate web elements**. It provides a standard and readable way to define element locator strategies.

---

### 🔑 Common Locator Strategies (with `By`):

| `By` Method            | Description                               | Example                                 |
| ---------------------- | ----------------------------------------- | --------------------------------------- |
| `By.ID`                | Locates element by `id` attribute         | `By.ID, "username"`                     |
| `By.NAME`              | Locates element by `name` attribute       | `By.NAME, "email"`                      |
| `By.CLASS_NAME`        | Locates by class (first match only)       | `By.CLASS_NAME, "input-field"`          |
| `By.TAG_NAME`          | Locates element by tag (e.g., input, div) | `By.TAG_NAME, "input"`                  |
| `By.LINK_TEXT`         | Exact visible text of a link              | `By.LINK_TEXT, "Login"`                 |
| `By.PARTIAL_LINK_TEXT` | Partial match of link text                | `By.PARTIAL_LINK_TEXT, "Log"`           |
| `By.CSS_SELECTOR`      | CSS selector                              | `By.CSS_SELECTOR, "input[type='text']"` |
| `By.XPATH`             | XPath expression                          | `By.XPATH, "//input[@id='username']"`   |

---

### ✅ Real-World Use Case: Login Page

```python
from selenium.webdriver.common.by import By

# Locators
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
```

---

## 🧠 2. `from selenium.webdriver.support.ui import WebDriverWait`

### ✅ What is `WebDriverWait`?

`WebDriverWait` is used to **pause** your script until a certain condition is met (or timeout occurs). It prevents errors caused by trying to interact with elements that aren't ready yet.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```

---

### 🔑 Common `ExpectedConditions` (EC)

| Condition                       | Description                                                     |
| ------------------------------- | --------------------------------------------------------------- |
| `presence_of_element_located`   | Waits until the element is in the DOM (not necessarily visible) |
| `visibility_of_element_located` | Waits until element is visible (i.e., has height/width)         |
| `element_to_be_clickable`       | Waits until the element is visible and enabled (clickable)      |
| `text_to_be_present_in_element` | Waits until a specific text appears inside an element           |
| `invisibility_of_element`       | Waits until an element disappears or is hidden                  |
| `alert_is_present`              | Waits until a JavaScript alert is present                       |

---

### ✅ Real-World Use Case: Wait for Search Results

```python
# Wait for the search input box
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.ID, "search-input")))
search_box.send_keys("Data Analyst Jobs")

# Wait for results
results = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "job-card")))
```

---

## 🎯 Combined Example: Real Login and Search

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 20)

driver.get("https://www.linkedin.com/login")

# Wait for username
username = wait.until(EC.presence_of_element_located((By.ID, "username")))
username.send_keys("testuser@example.com")

# Wait for password
password = driver.find_element(By.ID, "password")
password.send_keys("password123")

# Wait for login button to be clickable
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
login_button.click()

# Wait for Jobs page nav bar to appear after login
wait.until(EC.presence_of_element_located((By.TAG_NAME, "nav")))

driver.get("https://www.linkedin.com/jobs/")
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "job-card")))

print("Login and Job page loaded successfully!")
driver.quit()
```

---

## 📌 Summary Cheat Sheet

### ✅ `By` Locators

| Locator                              | Use When                                     |
| ------------------------------------ | -------------------------------------------- |
| `By.ID`                              | Most reliable if ID is unique                |
| `By.CLASS_NAME`                      | Use for styling classes, caution if multiple |
| `By.NAME`                            | Forms and input fields                       |
| `By.LINK_TEXT` / `PARTIAL_LINK_TEXT` | Anchor tags `<a>`                            |
| `By.TAG_NAME`                        | Generic targeting (e.g., get all buttons)    |
| `By.CSS_SELECTOR`                    | Precise, powerful for hierarchy              |
| `By.XPATH`                           | Most powerful for complex conditions         |

---

### ✅ `WebDriverWait + EC`

| EC Condition                    | Scenario                                |
| ------------------------------- | --------------------------------------- |
| `presence_of_element_located`   | DOM loaded but may be invisible         |
| `visibility_of_element_located` | Ready to interact                       |
| `element_to_be_clickable`       | Perfect for buttons and links           |
| `alert_is_present`              | Waiting for JS alerts                   |
| `invisibility_of_element`       | Wait for loader or spinner to disappear |

---

## 🧪 Real-World Use Cases:

### 📥 Form Submission

```python
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
```

### 🗃️ Table/Data Appears

```python
wait.until(EC.presence_of_element_located((By.XPATH, "//table[@id='results']")))
```

### 📂 Upload Completion

```python
wait.until(EC.invisibility_of_element((By.ID, "upload-spinner")))
```

### 📢 Pop-up Alert

```python
WebDriverWait(driver, 5).until(EC.alert_is_present())
driver.switch_to.alert.accept()
```

---

Let me know if you’d like a **PDF version** or **visual diagram** for this study note.
