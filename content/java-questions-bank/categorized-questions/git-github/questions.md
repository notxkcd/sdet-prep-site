---
title: "Git & GitHub Interview Questions"
date: 2026-01-30
draft: false
categories: ["Git & GitHub"]
---

## Beginner (Basics & Fundamentals)
1. [What is git hub?](#1-what-is-git-hub)
2. [Explain git?](#2-explain-git)
3. [Explain Git?](#3-explain-git)
4. [What is the purpose of Git?](#4-what-is-the-purpose-of-git)
5. [Why is GIT used?](#5-why-is-git-used)
6. [What are the advantages of Git Hub?](#6-what-are-the-advantages-of-git-hub)
7. [Why is GitHub considered version control?](#7-why-is-github-considered-version-control)
8. [Currently, do you use GitHub?](#8-currently-do-you-use-github)
9. [Tell me about git usage in your current project?](#9-tell-me-about-git-usage-in-your-current-project)
10. [What are pull and push?](#10-what-are-pull-and-push)
11. [What is the difference between Commit and Push in Github?](#11-what-is-the-difference-between-commit-and-push-in-github)
12. [Explain git commands: commit and merge?](#12-explain-git-commands-commit-and-merge)
13. [What is the command to push code and to create a branch?](#13-what-is-the-command-to-push-code-and-to-create-a-branch)
14. [How do you create a branch in GitHub?](#14-how-do-you-create-a-branch-in-github)
15. [What is the difference between clone and checkout in GitHub?](#15-what-is-the-difference-between-clone-and-checkout-in-github)

## Intermediate (Commands & Practical Usage)
1. [List git commands for code push and code pull?](#1-list-git-commands-for-code-push-and-code-pull)
2. [How will you push a code in Git? Please explain with git commands?](#2-how-will-you-push-a-code-in-git-please-explain-with-git-commands)
3. [How will you push your code to the server in GitHub?](#3-how-will-you-push-your-code-to-the-server-in-github)
4. [How to push code to git and list its commands?](#4-how-to-push-code-to-git-and-list-its-commands)
5. [How do you push the codes, what tools are you using for it, and explain the hierarchy?](#5-how-do-you-push-the-codes- what-tools-are-you-using-for-it-and-explain-the-hierarchy)
6. [Are you using git and how are you pushing your code to git?](#6-are-you-using-git-and-how-are-you-pushing-your-code-to-git)
7. [What are the git commands you use in your project?](#7-what-are-the-git-commands-you-use-in-your-project)
8. [Do you know how to push the codes in Git and how to work on this?](#8-do-you-know-how-to-push-the-codes-in-git-and-how-to-work-on-this)
9. [When will we push the code to GIT?](#9-when-will-we-push-the-code-to-git)
10. [How to delete code in GitHub?](#10-how-to-delete-code-in-github)
11. [What is the difference between git fetch and git pull?](#11-what-is-the-difference-between-git-fetch-and-git-pull)
12. [Have you used GitLab?](#12-have-you-used-gitlab)
13. [How do you configure Jenkins with GitHub?](#13-how-do-you-configure-jenkins-with-github)
14. [What is "GIT Stash" and what is it used for?](#14-what-is-git-stash-and-what-is-it-used-for)
15. [What is stash in GitHub?](#15-what-is-stash-in-github)

## Advanced (Conflict Resolution & Complex Logic)
1. [What is a git conflict?](#1-what-is-a-git-conflict)
2. [Did you use git in your project and what is a git conflict?](#2-did-you-use-git-in-your-project-and-what-is-a-git-conflict)
3. [How do you resolve a git conflict?](#3-how-do-you-resolve-a-git-conflict)
4. [How to resolve a conflict in GIT?](#4-how-to-resolve-a-conflict-in-git)
5. [Explain git conflict and how to resolve it?](#5-explain-git-conflict-and-how-to-resolve-it)
6. [How do you resolve Conflicts in Git?](#6-how-do-you-resolve-conflicts-in-git)
7. [How will you handle a git conflict?](#7-how-will-you-handle-a-git-conflict)
8. [What is rebase in GitHub?](#8-what-is-rebase-in-github)
9. [What is the difference between git pull and git patch?](#9-what-is-the-difference-between-git-pull-and-git-patch)
10. [How do you push test cases from Branch A to Branch B? Write the code?](#10-how-do-you-push-test-cases-from-branch-a-to-branch-b-write-the-code)
11. [I am facing an error that says "Fast forward" while pushing my code to the server in GitHub. How do I resolve it?](#11-i-am-facing-an-error-that-says-fast-forward-while-pushing-my-code-to-the-server-in-github-how-do-i-resolve-it)

---

## Questions with Answers

### Beginner (Basics & Fundamentals) - Answers

### 1. What is git hub? {#1-what-is-git-hub}
**Answer**: GitHub is a cloud-based hosting service that lets you manage and share your Git repositories. It provides a web interface for collaboration and version control.

### 2. Explain git? {#2-explain-git}
**Answer**: Git is a **Distributed Version Control System (DVCS)** that tracks changes in source code during software development. It allows multiple developers to work on the same project simultaneously.

### 3. Explain Git? {#3-explain-git}
**Answer**: Git is an open-source tool used to track changes in files. It helps in maintaining a history of edits, allowing you to revert to previous versions if something goes wrong.

### 4. What is the purpose of Git? {#4-what-is-the-purpose-of-git}
**Answer**: Its main purpose is **Version Control**—managing code history, enabling collaboration, and ensuring that multiple people don't overwrite each other's work.

### 5. Why is GIT used? {#5-why-is-git-used}
**Answer**: To keep a record of all changes, coordinate work among team members, and branch out new features without breaking the main code.

### 6. What are the advantages of Git Hub? {#6-what-are-the-advantages-of-git-hub}
**Answer**: It offers easy collaboration, issue tracking, project management, and serves as a portfolio for developers. It also integrates well with CI/CD tools.

### 7. Why is GitHub considered version control? {#7-why-is-github-considered-version-control}
**Answer**: Because it stores every version of your code. Every time you "commit," GitHub saves a snapshot, allowing you to track exactly who changed what and when.

### 8. Currently, do you use GitHub? {#8-currently-do-you-use-github}
**Answer**: Yes, I use it daily to push my automation scripts, create pull requests for review, and store project documentation.

### 9. Tell me about git usage in your current project? {#9-tell-me-about-git-usage-in-your-current-project}
**Answer**: We use a central repository on GitHub. Developers and testers work on separate branches, and we merge them into the `main` branch after code reviews.

### 10. What are pull and push? {#10-what-are-pull-and-push}
**Answer**:
- **Push**: Sending your local code changes to the remote repository (GitHub).
- **Pull**: Fetching and merging changes from the remote repository to your local machine.

### 11. What is the difference between Commit and Push in Github? {#11-what-is-the-difference-between-commit-and-push-in-github}
**Answer**:
- **Commit**: Saves changes to your **local** repository.
- **Push**: Uploads those local commits to the **remote** server (GitHub).

### 12. Explain git commands: commit and merge? {#12-explain-git-commands-commit-and-merge}
**Answer**:
- **Commit**: Records a snapshot of your changes with a message.
- **Merge**: Combines changes from one branch (e.g., `feature`) into another (e.g., `main`).

### 13. What is the command to push code and to create a branch? {#13-what-is-the-command-to-push-code-and-to-create-a-branch}
**Answer**:
- **Create Branch**: `git branch branch_name`
- **Push Code**: `git push origin branch_name`

### 14. How do you create a branch in GitHub? {#14-how-do-you-create-a-branch-in-github}
**Answer**: On the website, click the "Branch" dropdown and type a new name. Locally, use `git checkout -b branch_name`.

### 15. What is the difference between clone and checkout in GitHub? {#15-what-is-the-difference-between-clone-and-checkout-in-github}
**Answer**:
- **Clone**: Copies an entire repository from GitHub to your computer for the first time.
- **Checkout**: Switches between different branches within an already cloned repository.

### Intermediate (Commands & Practical Usage) - Answers

### 1. List git commands for code push and code pull? {#1-list-git-commands-for-code-push-and-code-pull}
**Answer**:
- `git add .` (Stage)
- `git commit -m "msg"` (Commit)
- `git push origin branch` (Push)
- `git pull origin branch` (Pull)

### 2. How will you push a code in Git? Please explain with git commands? {#2-how-will-you-push-a-code-in-git-please-explain-with-git-commands}
**Answer**:
1. `git add .`
2. `git commit -m "description"`
3. `git push origin branch_name`

### 3. How will you push your code to the server in GitHub? {#3-how-will-you-push-your-code-to-the-server-in-github}
**Answer**: By using the command `git push origin <branch_name>` after staging and committing locally.

### 4. How to push code to git and list its commands? {#4-how-to-push-code-to-git-and-list-its-commands}
**Answer**: Stage (`add`), Commit (`commit`), then Push (`push`).

### 5. How do you push the codes, what tools are you using for it, and explain the hierarchy? {#5-how-do-you-push-the-codes-what-tools-are-you-using-for-it-and-explain-the-hierarchy}
**Answer**: I use the **Git CLI** or **GitBash**. The hierarchy is: **Working Directory** -> **Staging Area** -> **Local Repo** -> **Remote Repo (GitHub)**.

### 6. Are you using git and how are you pushing your code to git? {#6-are-you-using-git-and-how-are-you-pushing-your-code-to-git}
**Answer**: Yes, I push code via terminal commands to ensure versioning of my Selenium scripts.

### 7. What are the git commands you use in your project? {#7-what-are-the-git-commands-you-use-in-your-project}
**Answer**: `status`, `add`, `commit`, `push`, `pull`, `branch`, `checkout`, and `log`.

### 8. Do you know how to push the codes in Git and how to work on this? {#8-do-you-know-how-to-push-the-codes-in-git-and-how-to-work-on-this}
**Answer**: Yes, I initialize the repo, add files, commit them with meaningful messages, and push to the remote branch.

### 9. When will we push the code to GIT? {#9-when-will-we-push-the-code-to-git}
**Answer**: Once a feature is complete, locally tested, and ready for a peer review or integration.

### 10. How to delete code in GitHub? {#10-how-to-delete-code-in-github}
**Answer**: Locally: `git rm file_name`. On GitHub: Navigate to the file and click the delete (trash) icon, then commit the change.

### 11. What is the difference between git fetch and git pull? {#11-what-is-the-difference-between-git-fetch-and-git-pull}
**Answer**:
- **Fetch**: Only downloads the data from remote; it doesn't change your local files.
- **Pull**: Downloads the data AND immediately merges it into your local branch.

### 12. Have you used GitLab? {#12-have-you-used-gitlab}
**Answer**: Yes, it is similar to GitHub but often used for private enterprise hosting with built-in CI/CD pipelines.

### 13. How do you configure Jenkins with GitHub? {#13-how-do-you-configure-jenkins-with-github}
**Answer**: By adding the GitHub repository URL in the Jenkins job configuration and setting up a **Webhook** to trigger builds on push.

### 14. What is "GIT Stash" and what is it used for? {#14-what-is-git-stash-and-what-is-it-used-for}
**Answer**: It temporarily "hides" your uncommitted changes so you can switch branches without committing unfinished work. You can bring them back later using `git stash pop`.

### 15. What is stash in GitHub? {#15-what-is-stash-in-github}
**Answer**: It is a local Git feature (not specific to GitHub) to store temporary work safely.

### Advanced (Conflict Resolution & Complex Logic) - Answers

### 1. What is a git conflict? {#1-what-is-a-git-conflict}
**Answer**: It happens when two people change the **same line** in the same file, and Git doesn't know which version to keep during a merge.

### 2. Did you use git in your project and what is a git conflict? {#2-did-you-use-git-in-your-project-and-what-is-a-git-conflict}
**Answer**: Yes. A conflict occurs when merging branches if overlapping changes are found.

### 3. How do you resolve a git conflict? {#3-how-do-you-resolve-a-git-conflict}
**Answer**:
1. Open the conflicting file.
2. Manually choose the correct code (removing the `<<<<`, `====`, `>>>>` markers).
3. `git add` the file and `git commit`.

### 4. How to resolve a conflict in GIT? {#4-how-to-resolve-a-conflict-in-git}
**Answer**: By manually editing the files to merge the logic and then finalizing the commit.

### 5. Explain git conflict and how to resolve it? {#5-explain-git-conflict-and-how-to-resolve-it}
**Answer**: Identifying the overlap, communicating with the teammate if needed, and manually merging the code in the editor.

### 6. How do you resolve Conflicts in Git? {#6-how-do-you-resolve-conflicts-in-git}
**Answer**: Using tools like VS Code or IntelliJ's merge tool makes it easier to compare and resolve.

### 7. How will you handle a git conflict? {#7-how-will-you-handle-a-git-conflict}
**Answer**: Pull the latest code, identify the conflict, resolve it manually, and push the resolved version.

### 8. What is rebase in GitHub? {#8-what-is-rebase-in-github}
**Answer**: It is the process of moving or combining a sequence of commits to a new base commit. It creates a cleaner, linear project history compared to merging.

### 9. What is the difference between git pull and git patch? {#9-what-is-the-difference-between-git-pull-and-git-patch}
**Answer**:
- **Pull**: Downloads and merges entire commits.
- **Patch**: A single file containing a set of differences (diff) that can be applied to another branch.

### 10. How do you push test cases from Branch A to Branch B? Write the code? {#10-how-do-you-push-test-cases-from-branch-a-to-branch-b-write-the-code}
**Answer**:
1. `git checkout BranchB`
2. `git merge BranchA`
3. `git push origin BranchB`

### 11. I am facing an error that says "Fast forward" while pushing my code to the server in GitHub. How do I resolve it? {#11-i-am-facing-an-error-that-says-fast-forward-while-pushing-my-code-to-the-server-in-github-how-do-i-resolve-it}
**Answer**: This usually means your local repo is behind the remote. Resolve it by doing a `git pull` first to synchronize, then push your changes.
