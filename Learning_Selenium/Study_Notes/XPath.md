# ✅ What is XPath?

**XPath (XML Path Language)** is a query language used to **navigate through elements and attributes** in an HTML or XML document.

In **Selenium**, we use XPath to locate elements on a web page for automation.

---

# 🔎 Why Use XPath in Selenium?

* When `id`, `name`, or `className` are not sufficient
* To find elements with **complex structure**
* To **navigate relationships** between elements (parent → child, sibling, etc.)

---

# 🛠️ Syntax Basics You MUST Understand

Let’s break the XPath syntax into pieces:

| Syntax Part  | What It Means                                             | Example                               |
| ------------ | --------------------------------------------------------- | ------------------------------------- |
| `//`         | Select from **anywhere** in the document (Relative XPath) | `//div` selects all `<div>` tags      |
| `/`          | Selects from the **root** or direct child                 | `/html/body/div` (Absolute XPath)     |
| `@`          | Refers to an **attribute**                                | `@id`, `@class`, `@name`              |
| `[]`         | **Conditions or filters**                                 | `//input[@type='text']`               |
| `*`          | Wildcard (any tag name)                                   | `//*[text()='Login']`                 |
| `text()`     | Selects visible text                                      | `//a[text()='Logout']`                |
| `contains()` | Partial match of attribute or text                        | `//button[contains(@class,'submit')]` |

---

# 📌 Let's Begin with the Most Used 20% That You'll Use 80% of the Time

---

## ✅ 1. **Absolute XPath** (Starts with `/`) – ❌ Rarely Used in Real Life

### Example:

```xpath
/html/body/div[1]/form/input[1]
```

🧠 Explanation:

* Starts from the root: `/html`
* Goes one by one to reach target
* `[1]` means **first child**

🛑 **Why avoid?** Any small change in page structure breaks it.

---

## ✅ 2. **Relative XPath** – ✅ Used Most of the Time

### Syntax:

```xpath
//tagname[@attribute='value']
```

### Example:

```xpath
//input[@id='username']
```

🧠 Explanation:

* `//` — Selects from **anywhere** in the page
* `input` — Selects `<input>` tag
* `@id='username'` — Matches if it has an attribute `id="username"`

✅ This is your **default choice** for most test automation.

---

## ✅ 3. **Locating by Multiple Attributes**

You can use `and` or `or` to combine conditions:

### Example:

```xpath
//input[@type='text' and @name='email']
```

🧠 Explanation:

* Only selects `<input>` that has:

  * `type="text"`
  * and `name="email"`

---

## ✅ 4. **Using `text()` to Match Exact Visible Text**

### Example:

```xpath
//button[text()='Login']
```

🧠 Explanation:

* `//button` — Selects all `<button>` tags
* `[text()='Login']` — Matches if inner text is exactly "Login"

🛠️ Use when:

* You're selecting buttons, links, or labels with exact words.

---

## ✅ 5. **Using `contains()` for Partial Match (text or attribute)**

### Match partial attribute:

```xpath
//div[contains(@class, 'error')]
```

### Match partial text:

```xpath
//button[contains(text(), 'Log')]
```

🧠 Use this when:

* Class or ID has random suffixes
* You only know part of the text

---

## ✅ 6. **Using Starts-With (less frequent)**

```xpath
//input[starts-with(@id, 'user_')]
```

🧠 Use when attribute starts with a **known pattern**.

---

## ✅ 7. **Finding Element by Position**

```xpath
(//input[@type='text'])[2]
```

🧠 Explanation:

* `()` groups the XPath expression
* `[2]` selects the **second matching element**

---

## ✅ 8. **Parent-Child and Sibling Relationships**

### ➤ Child:

```xpath
//div[@class='form-group']/input
```

➤ Meaning: Inside a `<div>` with `class='form-group'`, find `<input>`.

---

### ➤ Parent:

```xpath
//input[@id='email']/parent::div
```

🧠 Useful when:

* You find an element, and you want to go **up** to its container

---

### ➤ Following Sibling:

```xpath
//label[text()='Username']/following-sibling::input
```

🧠 Used in forms:

* Labels and inputs are often **siblings** in HTML

---

## ✅ 9. **Wildcard `*` – Any Tag**

```xpath
//*[@id='submit']
```

🧠 Selects **any element** (div, input, span, etc.) with `id='submit'`

---

## 🧪 Real-World Example: Login Page XPath

Imagine a login page with this HTML:

```html
<input id="user-name" type="text" placeholder="Username">
<input id="password" type="password">
<input class="submit-button btn_action" type="submit" value="Login">
```

### Selenium Code:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com")

# Enter username
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("standard_user")

# Enter password
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("secret_sauce")

# Click login
driver.find_element(By.XPATH, "//input[contains(@class, 'submit-button')]").click()
```

---

# 💎 Extra XPath Features (Used Sometimes)

| Feature               | Syntax / Example                                   |
| --------------------- | -------------------------------------------------- |
| `last()`              | `(//div[@class='msg'])[last()]`                    |
| `normalize-space()`   | `//button[normalize-space()='Login']`              |
| `ancestor::`          | `//input[@id='email']/ancestor::form`              |
| `descendant::`        | `//div[@id='form']/descendant::input`              |
| `preceding-sibling::` | `//input[@id='password']/preceding-sibling::label` |

---

# ✅ Summary: XPath Quick Cheatsheet

| Task                | XPath                                              |
| ------------------- | -------------------------------------------------- |
| Find element by ID  | `//input[@id='email']`                             |
| Find button by text | `//button[text()='Submit']`                        |
| Partial class match | `//div[contains(@class, 'form-group')]`            |
| Input near label    | `//label[text()='Email']/following-sibling::input` |
| Go up to parent     | `//input[@id='email']/parent::div`                 |
| Select Nth match    | `(//input[@type='text'])[2]`                       |

---

# 🛠️ How Do You Find the XPath in Real Life?

1. **Open Chrome** → Right click → Inspect Element
2. Select the desired element
3. Right click the HTML → Copy → Copy XPath (Browser's version)
4. OR test custom XPath in Console:

```javascript
$x("//input[@id='email']")
```

---

# 🔁 Final Tip

Keep it **readable and maintainable**:

✅ Good:

```xpath
//input[@id='email']
```

❌ Bad:

```xpath
/html/body/div[2]/div[1]/form/input[1]
```

---

# ✅ Step-by-Step Guide to Learning XPath with a Real-Life HTML Page

We’ll create a **simple, realistic login and profile form**. Then, I’ll explain **every XPath query** using this page as the reference.

---

## 🧾 Sample HTML Page (Real-Life Style)

```html
<!DOCTYPE html>
<html>
<head>
  <title>My Account</title>
</head>
<body>
  <div id="header">
    <h1>Welcome to MyApp</h1>
    <a href="/logout" class="logout-btn">Logout</a>
  </div>

  <div class="login-section">
    <form id="loginForm">
      <label for="username">Username:</label>
      <input type="text" id="username" name="user_name" placeholder="Enter your username">

      <label for="password">Password:</label>
      <input type="password" id="password" name="user_pass">

      <input type="submit" value="Login" class="btn primary-btn">
    </form>
  </div>

  <div class="profile-section">
    <h2>Profile</h2>
    <div class="user-details">
      <p class="name">Name: <span>Mohammad Saifi</span></p>
      <p class="email">Email: <span>saifi@example.com</span></p>
    </div>

    <div class="actions">
      <button class="edit-btn">Edit</button>
      <button class="delete-btn">Delete</button>
    </div>
  </div>
</body>
</html>
```

---

Now let’s use XPath to **locate different elements** based on this HTML code.

---

# 🎯 Targeted XPath Examples With Detailed Explanation

---

### ✅ 1. **Find the Login Form**

```xpath
//form[@id='loginForm']
```

* `//form` → any `<form>` tag in the page.
* `[@id='loginForm']` → it must have an attribute `id="loginForm"`.

🔧 **Use in Selenium:**

```python
driver.find_element(By.XPATH, "//form[@id='loginForm']")
```

---

### ✅ 2. **Locate Username Input Field**

```xpath
//input[@id='username']
```

* Finds the `<input>` with ID = "username"

### Alternative:

```xpath
//input[@name='user_name']
```

🧠 Why alternatives matter: Some pages don’t use `id`, so you can fall back to `name`.

---

### ✅ 3. **Locate Label for Password**

```xpath
//label[@for='password']
```

* Finds the `<label>` with `for="password"` (it’s linked to the password input)

---

### ✅ 4. **Find the Login Button (Using Class)**

```xpath
//input[@class='btn primary-btn']
```

* Selects the submit button with exact class match.

### More Flexible:

```xpath
//input[contains(@class, 'primary-btn')]
```

* Use `contains()` when class names have **multiple values** or **framework-generated suffixes**.

---

### ✅ 5. **Find Text Value (Email)**

```xpath
//p[@class='email']/span
```

* Finds the email text (within the `<span>` under the `<p>` with class "email")

---

### ✅ 6. **Locate Logout Button by Text**

```xpath
//a[text()='Logout']
```

* Finds the `<a>` tag with exact visible text **"Logout"**

### More Flexible:

```xpath
//a[contains(text(), 'Log')]
```

* Use `contains()` when the full text is dynamic (e.g., "Logout (Admin)")

---

### ✅ 7. **Get Profile Section Header**

```xpath
//div[@class='profile-section']/h2
```

* Finds the `<h2>` inside the `div` with `class='profile-section'`

---

### ✅ 8. **Find Delete Button (Using Class)**

```xpath
//button[@class='delete-btn']
```

* Straightforward class match

---

### ✅ 9. **Find Username Label and Input Using Sibling Relationship**

```xpath
//label[text()='Username:']/following-sibling::input
```

* Locates the `<input>` that **immediately follows** the label with text "Username:"

---

### ✅ 10. **Go to Parent from Password Field**

```xpath
//input[@id='password']/parent::form
```

* Navigates **up** to the parent `<form>` element of the password field.

---

# 🧪 Real-Life XPath Usage in Selenium (Python Example)

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://localhost/myaccount.html")  # Assuming the page is local

# Fill username
driver.find_element(By.XPATH, "//input[@id='username']").send_keys("admin")

# Fill password
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("1234")

# Click login
driver.find_element(By.XPATH, "//input[@value='Login']").click()

# Click delete profile
driver.find_element(By.XPATH, "//button[@class='delete-btn']").click()
```

---

# 🧠 Visual XPath Map (from HTML)

| Element Description  | XPath                               |
| -------------------- | ----------------------------------- |
| Login form           | `//form[@id='loginForm']`           |
| Username field       | `//input[@id='username']`           |
| Password field       | `//input[@id='password']`           |
| Submit/Login button  | `//input[@class='btn primary-btn']` |
| Profile section      | `//div[@class='profile-section']`   |
| Edit button          | `//button[@class='edit-btn']`       |
| Delete button        | `//button[@class='delete-btn']`     |
| User name value      | `//p[@class='name']/span`           |
| Email value          | `//p[@class='email']/span`          |
| Logout button (text) | `//a[text()='Logout']`              |

---

# ✅ Conclusion – Learn XPath the Right Way

✅ Learn with real-world HTML structure
✅ Visualize what each tag and attribute means
✅ Practice in browser dev tools using `$x("...")` in console
✅ Stick to **relative XPath** with `//tag[@attr='value']` most of the time
✅ Use `contains()`, `text()`, and sibling/parent axes when needed

---

