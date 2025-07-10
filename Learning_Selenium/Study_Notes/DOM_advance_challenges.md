Below is the provided snippet as standalone HTML, followed by **30 real‑world locator patterns**—from **basic** to **advanced**—each with a brief code example and explanation. You can mix CSS and XPath as needed.

---

```html
<header id="global-nav" aria-label="Global Navigation" class="global-nav global-alert-offset-top global-nav--hide-text global-nav--visible">
  <div class="global-nav__content">
    <a class="sweUDwHDWDFIeFKJCGYvmbdSxlCtpFtSOwpCMRc"
       href="https://www.linkedin.com/feed/?nis=true"
       data-test-app-aware-link="">
      <div class="ivm-image-view-model global-nav__branding-logo">
        <div class="ivm-view-attr__img-wrapper">
          <li-icon type="app-linkedin-bug-color-icon"
                   class="ivm-view-attr__icon"
                   size="large"
                   role="img"
                   aria-label="LinkedIn">
            <!-- svg omitted -->
          </li-icon>
        </div>
      </div>
    </a>

    <div id="global-nav-search" class="global-nav__search global-nav__search--jobs">
      <div class="jobs-search-box__container jobs-search-box">
        <div class="jobs-search-box__input jobs-search-box__input--keyword jobs-search-box__input--both-bars jobs-search-box__input--clear-text">
          <div class="jobs-search-box__semantic-search-inner--rounded"
               id="keyword-typeahead-instance-ember32">
            <div class="relative">
              <label for="jobs-search-box-keyword-id-ember32"
                     class="jobs-search-box__input-icon jobs-search-box__keywords-label jobs-search-box__semantic-search-input-icon">
                <span class="visually-hidden">Search by title, skill, or company</span>
              </label>
              <input id="jobs-search-box-keyword-id-ember32"
                     class="basic-input jobs-search-box__text-input jobs-search-box__keyboard-text-input jobs-search-global-typeahead__input jobs-search-box__text-input--with-clear jobs-search-box__text-input--rounded"
                     role="combobox"
                     aria-autocomplete="list"
                     aria-label="Search by title, skill, or company"
                     data-job-search-box-keywords-input-trigger="Data Analyst"
                     type="text">
              <button id="ember35"
                      class="artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view jobs-search-box__clear-input jobs-search-box__clear-keyword-input"
                      type="button">
                <span class="artdeco-button__text">Clear search keywords</span>
              </button>
            </div>
          </div>
        </div>

        <div class="jobs-search-box__input jobs-search-box__input--location jobs-search-box__input--both-bars jobs-search-box__input--clear-text">
          <div class="jobs-search-box__semantic-search-inner--rounded"
               id="location-typeahead-instance-ember32">
            <div class="relative">
              <label for="jobs-search-box-location-id-ember32"
                     class="jobs-search-box__input-icon jobs-search-box__semantic-search-input-icon">
                <span class="visually-hidden">City, state, or zip code</span>
              </label>
              <input id="jobs-search-box-location-id-ember32"
                     class="basic-input jobs-search-box__text-input jobs-search-box__text-input--with-clear jobs-search-box__text-input--rounded"
                     role="combobox"
                     aria-autocomplete="list"
                     aria-label="City, state, or zip code"
                     data-job-search-box-location-input-trigger="India"
                     type="text">
              <button id="ember39"
                      class="artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view jobs-search-box__clear-input jobs-search-box__clear-location-input"
                      type="button">
                <span class="artdeco-button__text">Clear search location</span>
              </button>
            </div>
          </div>
        </div>

        <button class="jobs-search-box__submit-button artdeco-button artdeco-button--2 artdeco-button--secondary"
                type="button">Search</button>
        <button aria-label="Cancel"
                id="ember37"
                class="jobs-search-box__dismiss artdeco-button artdeco-button--circle artdeco-button--1 artdeco-button--tertiary ember-view"
                type="button"></button>
      </div>
    </div>

    <nav class="global-nav__nav" aria-label="Primary Navigation">
      <ul class="global-nav__primary-items">
        <li class="global-nav__primary-item">
          <a class="sweUDwHDWDFIeFKJCGYvmbdSxlCtpFtSOwpCMRc global-nav__primary-link"
             href="https://www.linkedin.com/feed/?nis=true&amp;" data-test-app-aware-link="">
            <span class="t-12 break-words block t-black--light t-normal global-nav__primary-link-text"
                  title="Home">Home</span>
          </a>
        </li>
        <!-- …other li items… -->
      </ul>
    </nav>
  </div>
</header>
```

---

### 1. By ID (CSS)

**HTML**

```html
<header id="global-nav" …>
  …  
</header>
```

```python
driver.find_element(By.CSS_SELECTOR, "#global-nav")
```

* **Matches** the `<header>` with `id="global-nav"`.
* **Use when** IDs are stable and unique.

---

### 2. By ID (XPath)

**HTML**

```html
<header id="global-nav" …>
  …
</header>
```

```python
driver.find_element(By.XPATH, "//*[@id='global-nav']")
```

* **Same target** as #1, but using XPath.

---

### 3. By Class (CSS)

**HTML**

```html
<div class="global-nav__content">
  …  
</div>
```

```python
driver.find_element(By.CSS_SELECTOR, ".global-nav__content")
```

* **Matches** the first element with that class.
* **Caveat**: if multiple share it, only the first is returned.

---

### 4. Multiple Classes (CSS)

**HTML**

```html
<input class="basic-input jobs-search-box__text-input jobs-search-box__keyboard-text-input …" …>
```

```python
driver.find_element(
    By.CSS_SELECTOR,
    ".basic-input.jobs-search-box__text-input"
)
```

* **Ensures** the `<input>` has **both** classes.

---

### 5. Attribute Exists (CSS)

**HTML**

```html
<a data-test-app-aware-link="" href="…">…</a>
```

```python
driver.find_element(By.CSS_SELECTOR, "[data-test-app-aware-link]")
```

* **Matches** any element with that `data-` attribute.

---

### 6. Partial Attribute Value (CSS)

**HTML**

```html
<a href="https://www.linkedin.com/feed/?nis=true">…</a>
```

```python
driver.find_element(By.CSS_SELECTOR, "a[href*='linkedin.com/feed']")
```

* **Matches** the `<a>` whose `href` contains that substring.

---

### 7. Starts‑With Attribute (CSS)

**HTML**

```html
<button id="ember35" …>…</button>
```

```python
driver.find_element(By.CSS_SELECTOR, "button[id^='ember']")
```

* **Matches** any `<button>` with an `id` starting with `"ember"`.

---

### 8. Ends‑With Attribute (CSS)

**HTML**

```html
<div id="keyword-typeahead-instance-ember32">…</div>
```

```python
driver.find_element(By.CSS_SELECTOR, "div[id$='ember32']")
```

* **Matches** `<div>` whose `id` ends with `"ember32"`.

---

### 9. Contains‑Substring in Attribute (CSS)

**HTML**

```html
<div class="jobs-search-box__input jobs-search-box__input--keyword …">…</div>
```

```python
driver.find_element(By.CSS_SELECTOR, "[class*='jobs-search-box__input']")
```

* **Matches** any element where `class` contains that substring.

---

### 10. Descendant Selector (CSS)

**HTML**

```html
<header id="global-nav">
  …
  <div class="ivm-view-attr__img-wrapper">
    <li-icon>…</li-icon>
  </div>
</header>
```

```python
driver.find_element(
    By.CSS_SELECTOR,
    "#global-nav .ivm-view-attr__img-wrapper li-icon"
)
```

* **Matches** the `<li-icon>` **inside** the header.

---

### 11. Direct Child Selector (CSS)

**HTML**

```html
<div class="jobs-search-box__input">
  <div class="relative">…</div>
</div>
```

```python
driver.find_element(
    By.CSS_SELECTOR,
    "div.jobs-search-box__input > div.relative"
)
```

* **Matches** the **direct** child `<div class="relative">`.

---

### 12. nth‑Child (CSS)

**HTML**

```html
<ul class="global-nav__primary-items">
  <li>Home</li>
  <li>My Network</li>
  <li>Jobs</li>
  …
</ul>
```

```python
driver.find_element(
    By.CSS_SELECTOR,
    "ul.global-nav__primary-items li:nth-child(3)"
)
```

* **Matches** the **3rd** `<li>` (“Jobs”).

---

### 13. Group Selectors (CSS OR)

**HTML**

```html
<button class="jobs-search-box__submit-button">Search</button>
<button class="jobs-search-box__dismiss">Cancel</button>
```

```python
elems = driver.find_elements(
    By.CSS_SELECTOR,
    ".jobs-search-box__submit-button, .jobs-search-box__dismiss"
)
```

* **Matches** both buttons; returns a list of two elements.

---

### 14. Negation Pseudo‑Class (CSS)

**HTML**

```html
<button disabled>…</button>
<button>…</button>
```

```python
enabled = driver.find_elements(
    By.CSS_SELECTOR,
    "button:not([disabled])"
)
```

* **Matches** only buttons **without** `disabled`.

---

### 15. By Exact Text (XPath)

**HTML**

```html
<span class="global-nav__primary-link-text" title="Home">Home</span>
```

```python
driver.find_element(By.XPATH, "//span[text()='Home']")
```

* **Matches** the `<span>` whose exact text is “Home”.

---

### 16. Contains Text (XPath)

**HTML**

```html
<button class="jobs-search-box__clear-input">Clear search keywords</button>
```

```python
driver.find_element(By.XPATH, "//button[contains(.,'Clear search')]")
```

* **Matches** any `<button>` whose visible text includes “Clear search”.

---

### 17. normalize-space() (XPath)

**HTML**

```html
<span>  Home  </span>
```

```python
driver.find_element(
    By.XPATH,
    "//span[normalize-space()='Home']"
)
```

* **Matches** “Home” ignoring extra spaces.

---

### 18. Multiple Attributes AND (XPath)

**HTML**

```html
<input role="combobox" aria-autocomplete="list" …>
```

```python
driver.find_element(
    By.XPATH,
    "//input[@role='combobox' and @aria-autocomplete='list']"
)
```

* **Matches** only if **both** attributes are present.

---

### 19. Attribute OR (XPath)

**HTML**

```html
<button id="ember35">…</button>
<button aria-label="Cancel">…</button>
```

```python
driver.find_element(
    By.XPATH,
    "//button[@id='ember35' or @aria-label='Cancel']"
)
```

* **Matches** either the first or the second, whichever appears first in DOM order.

---

### 20. starts-with() for Dynamic IDs (XPath)

**HTML**

```html
<div id="keyword-typeahead-instance-ember32">…</div>
```

```python
driver.find_element(
    By.XPATH,
    "//div[starts-with(@id,'keyword-typeahead-instance-')]"
)
```

* **Matches** any `<div>` whose ID begins with that prefix.

---

### 21. contains() on Class (XPath)

**HTML**

```html
<div class="global-nav__search global-nav__search--jobs">…</div>
```

```python
driver.find_element(
    By.XPATH,
    "//div[contains(@class,'global-nav__search--jobs')]"
)
```

* **Matches** the jobs search container.

---

### 22. last() Position (XPath)

**HTML**

```html
<ul class="global-nav__primary-items">
  <li>Home</li>
  <!-- … -->
  <li class="global-nav__overflow-menu">More</li>
</ul>
```

```python
driver.find_element(
    By.XPATH,
    "(//li[contains(@class,'global-nav__primary-item')])[last()]"
)
```

* **Matches** the **last** primary nav item.

---

### 23. following-sibling (XPath)

**HTML**

```html
<label for="jobs-search-box-keyword-id-ember32">…</label>
<input id="jobs-search-box-keyword-id-ember32" …>
```

```python
driver.find_element(
    By.XPATH,
    "//label[@for='jobs-search-box-keyword-id-ember32']"
    "/following-sibling::input"
)
```

* **Matches** the `<input>` that directly follows its `<label>`.

---

### 24. preceding-sibling (XPath)

**HTML**

```html
<input id="jobs-search-box-location-id-ember32" …>
<button id="ember39">…</button>
```

```python
driver.find_element(
    By.XPATH,
    "//button[@id='ember39']/preceding-sibling::input"
)
```

* **Matches** the `<input>` immediately before the button.

---

### 25. ancestor (XPath)

**HTML**

```html
<a …><span>Home</span></a>
```

```python
driver.find_element(
    By.XPATH,
    "//span[text()='Home']/ancestor::a"
)
```

* **Matches** the `<a>` wrapping the “Home” span.

---

### 26. parent (XPath)

**HTML**

```html
<div class="relative">
  <input id="jobs-search-box-location-id-ember32" …>
</div>
```

```python
driver.find_element(
    By.XPATH,
    "//input[@id='jobs-search-box-location-id-ember32']/parent::div"
)
```

* **Matches** the immediate parent `<div>`.

---

### 27. Deep Nesting (XPath)

**HTML**

```html
<header id="global-nav">
  <nav>
    <ul>
      <li>Home</li>
      <li>My Network</li>
      <li><span>Jobs</span></li>
      …
```

```python
driver.find_element(
    By.XPATH,
    "//header[@id='global-nav']//nav//li[3]//span"
)
```

* **Matches** the `<span>` inside the 3rd `<li>` under the header.

---

### 28. Case‑Insensitive Text (XPath)

**HTML**

```html
<span>HOME</span>
```

```python
driver.find_element(
    By.XPATH,
    "//span[translate(normalize-space(.), 'HOME', 'home')='home']"
)
```

* **Matches** “HOME”, “home”, or any case combination.

---

### 29. Attribute Name Pattern via JS

**HTML**

```html
<li-icon role="img" data-dynamic-123="…">…</li-icon>
```

```python
host = driver.find_element(By.CSS_SELECTOR, "li-icon[role='img']")
found = driver.execute_script("""
  return [...arguments[0].attributes]
    .find(a => a.name.startsWith('data-'));
""", host)
```

* **Finds** the first `data-*` attribute name on that element via JS.

---

### 30. Shadow DOM & Iframe Hybrid

**HTML**

```html
<iframe id="msg_iframe">…</iframe>
<!-- Inside that iframe: -->
<custom-shadow-host>
  #shadow-root
    <button class="send">Send</button>
```

```python
# 1) Switch to iframe
driver.switch_to.frame("msg_iframe")
# 2) Locate shadow host
host = driver.find_element(By.CSS_SELECTOR, "custom-shadow-host")
# 3) Enter shadow root
shadow = driver.execute_script("return arguments[0].shadowRoot", host)
# 4) Find & click button
shadow.find_element(By.CSS_SELECTOR, "button.send").click()
# 5) Return to main document
driver.switch_to.default_content()
```

* **Handles** both iframe context and Shadow DOM encapsulation.

---

With these **HTML+locator+explanation** triplets, you can see exactly **which markup** each pattern targets and **why** it’s structured that way. Mix and match patterns to build bullet‑proof locators for even the most dynamic LinkedIn components.
