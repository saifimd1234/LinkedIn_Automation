Focus on the **20% of techniques** that solve **80% of locator brittleness**:

1. **Custom/Data Attributes** (`data-*`)
2. **Logical Relatives** (parent/child/sibling)
3. **Text‑based Anchors** (`normalize-space()`)
4. **Partial‑matching Functions** (`contains()`, `starts-with()`)
5. **Waiting & Visibility Guards**

---

## 1. Basic Static Locators

When elements have stable IDs or class names:

```html
<!-- Example -->
<div id="profile-pic">
  <img src="me.jpg" alt="My Photo">
</div>
```

```python
# CSS
driver.find_element(By.CSS_SELECTOR, "#profile-pic img")

# XPath
driver.find_element(By.XPATH, "//div[@id='profile-pic']//img")
```

> **Edge Case**: multiple `img` under same parent → add `[1]` or a more specific filter.

---

## 2. Using Data‑Attributes (Most Robust)

Web apps often include `data-test`, `data-id`, etc. Always prefer these:

```html
<button data-test="connect-btn">Connect</button>
```

```python
driver.find_element(By.CSS_SELECTOR, "button[data-test='connect-btn']")
```

> **Why**: unlikely to change, designed for automated tests.

---

## 3. Partial Matching for Dynamic Classes/IDs

Use `contains()` or `starts-with()` when IDs/classes have random suffixes:

```html
<div class="profileCard_abc123">…</div>
```

```python
# XPath contains()
driver.find_element(By.XPATH, "//div[contains(@class, 'profileCard_')]")

# CSS [class^=] for “starts‑with”
driver.find_element(By.CSS_SELECTOR, "div[class^='profileCard_']")
```

---

## 4. Text‑Anchored Locators

When text is stable but structure shifts:

```html
<li><a href="/jobs">Jobs</a></li>
```

```python
driver.find_element(By.XPATH,
    "//li[.//a[normalize-space()='Jobs']]/a"
)
```

> **Tip**: wrap text in `normalize-space()` to trim whitespace.

---

## 5. Logical Relatives & Axes

Target elements relative to known anchors to isolate them:

```html
<div class="card">
  <h2>Data Engineer</h2>
  <button>Apply</button>
</div>
```

```python
# find “Apply” under the card titled “Data Engineer”
driver.find_element(By.XPATH,
  "//div[h2[normalize-space()='Data Engineer']]//button"
)
```

> **Axes Examples**:

* `parent::`, `following-sibling::`, `preceding-sibling::`

---

## 6. Handling Lists & Index‑shifts

When multiple similar items exist:

```html
<ul>
  <li class="feed-item">…</li>
  <li class="feed-item">…</li>
  <li class="feed-item">…</li>
</ul>
```

```python
# pick second feed item
driver.find_element(By.XPATH,
  "(//li[contains(@class,'feed-item')])[2]"
)
```

> **Edge Case**: better if each `<li>` has a sub‑attribute to target.

---

## 7. Waiting for AJAX‑Loaded Elements

Combine locators with explicit waits to avoid stale/before‑load errors:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

locator = (By.CSS_SELECTOR, "button[data-test='connect-btn']")
btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(locator)
)
btn.click()
```

---

## 8. Advanced: Shadow DOM & Iframes

* **Iframes**: switch context

  ```python
  driver.switch_to.frame("my_iframe_id")
  driver.find_element(By.CSS_SELECTOR, "…")
  driver.switch_to.default_content()
  ```
* **Shadow DOM**: requires JS execution

  ```python
  host = driver.find_element(By.CSS_SELECTOR, "my-component")
  shadow = driver.execute_script("return arguments[0].shadowRoot", host)
  shadow.find_element(By.CSS_SELECTOR, "button.save")
  ```

---

## 9. Putting It All Together: Real‑World Example

Imagine LinkedIn’s “Message” button with dynamic classes, loaded in a modal:

```html
<!-- Simplified -->
<div class="msg-overlay-container">
  <button class="msg-form__send-button artdeco-button">Send</button>
</div>
```

```python
# Combined strategy
locator = (By.XPATH,
  "//div[contains(@class,'msg-overlay-container')]"
  "//button[contains(@class,'msg-form__send-button') and normalize-space()='Send']"
)
send_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(locator)
)
send_btn.click()
```

**Why robust?**

* Anchored to a stable parent (`msg-overlay-container`)
* Partial match on button class
* Exact text match

---

## 🏁 TL;DR – Your 80/20 Locator Toolkit

1. **Data‑attributes** (`data-*`)
2. **Partial‑match** (`contains()`, `starts-with()`)
3. **Text anchors** (`normalize-space()`)
4. **Logical relatives** (parent/child/sibling axes)
5. **Explicit waits**

Combine these, and you’ll handle **80% of dynamic‑DOM brittleness** with **20% of the effort**.
