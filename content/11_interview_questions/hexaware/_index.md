---
title: "Hexaware Interview Questions"
date: 2026-01-30
draft: false
---

---

## 🧩 Round 1

| 1. **Self Introduction**

| 2. **Maven Build Tool**

   * Explain what Maven is and its role in project management.

| 3. **Write Any 5 Array Methods**

| 4. **Method Overloading**

| 5. **Types of Casting**

   * Example: Upcasting and Downcasting in Java.

| 6. **How to Perform Right Click in Selenium**

| 7. **Write Implicit Wait**

   ```java
   driver.manage().timeouts().implicitlyWait(Duration.ofSeconds(10));
   ```

| 8. **How to Scroll Using JavaScript Executor**

   ```java
   JavascriptExecutor js = (JavascriptExecutor) driver;
   js.executeScript("window.scrollBy(0,500)");
   ```

| 9. **How to Open the Incognito Browser**

   ```java
   ChromeOptions options = new ChromeOptions();
   options.addArguments("--incognito");
   WebDriver driver = new ChromeDriver(options);
   ```

| 10. **Find the First Repeated Number in an Array**

    ```java
    int[] a = {1, 2, 3, 4, 5, 2, 3, 4};
    Set<Integer> seen = new HashSet<>();
    for (int num : a) {
        if (!seen.add(num)) {
            System.out.println("First repeated number: " + num);
            break;
        }
    }
    ```

| 11. **Facing Critical Challenges in Your Project**

    * Discuss automation or testing challenges you encountered.

| 12. **Project Explanation**

---

## ⚙️ Round 2

| 1. **Write a Code to Launch Browser and Open `deals.com`**

   ```java
   WebDriver driver = new ChromeDriver();
   driver.get("https://www.deals.com");
   driver.manage().window().maximize();
   ```

| 2. **Get All Hyperlinks and Click on Links Containing “todaydeals”**

   ```java
   List<WebElement> links = driver.findElements(By.tagName("a"));
   for (WebElement link : links) {
       if (link.getText().toLowerCase().contains("todaydeals")) {
           link.click();
           break;
       }
   }
   ```

| 3. **Optimize the Above Code Using Waits**

   ```java
   WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(10));
   List<WebElement> links = wait.until(ExpectedConditions.visibilityOfAllElementsLocatedBy(By.tagName("a")));
   for (WebElement link : links) {
       if (link.getText().toLowerCase().contains("todaydeals")) {
           wait.until(ExpectedConditions.elementToBeClickable(link)).click();
           break;
       }
   }
   ```

| 4. **Day-to-Day Activities**

| 5. **Challenges Faced in Your Automation Framework**

| 6. **Roles and Responsibilities**

| 7. **Write the Workflow in Git Using Git Commands**

   ```bash
   git clone <repo-url>
   git checkout -b feature-branch
   git add .
   git commit -m "Added new feature"
   git push origin feature-branch
   git pull origin main
   git merge main
   git push origin main
   ```

| 8. **Jenkins Configuration**

   * Explain how you integrate and run your test scripts in Jenkins.

| 9. **Framework Explanation**

   * Describe the structure, tools, and flow of your automation framework.

---

Would you like me to merge this with the **Indium Interview Questions** into a single Markdown or PDF document for easier study/reference?
