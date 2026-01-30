# SDET Interview Preparation Kit

This is a Hugo-based site containing scripts, analysis, and a library of interview questions for SDET (Software Development Engineer in Test) roles.

## Project Structure

- `content/`: Contains the Markdown files for each module.
- `themes/`: Contains the site layouts and styling.
- `static/`: Assets that are served as-is (CSS, JS, etc.).

## Common Issues & Troubleshooting

### Page Not Found (404) on New Folders

**Issue:**
When adding a new section folder (e.g., `12_Company_Based_Questions`), the page shows "Page Not Found" even if the files exist.

**Root Causes:**
1.  **URL Casing:** Hugo defaults to lowercase URLs. If a folder has uppercase letters, the generated path might be lowercase (e.g., `/12_company_based_questions/`), leading to mismatches if the user or the site's internal links use uppercase.
2.  **Missing `_index.md` Metadata:** Hugo needs an `_index.md` file in the folder with correct front matter to render the section.
3.  **Draft Status:** If `draft: true` (or if `draft` is missing and defaults to true in some configs), the page won't build.

**Solution:**
1.  **Standardize Casing:** Use lowercase for all content folder names and URLs (e.g., rename `12_Company_Based_Questions` to `12_company_based_questions`).
2.  **Provide Proper Front Matter:** Ensure `_index.md` exists with at least:
    ```yaml
    ---
    title: "Your Section Title"
    draft: false
    category: "Projects" # Required by this theme for homepage visibility
    ---
    ```
3.  **Sync Homepage Links:** Ensure links in the main dashboard (`content/_index.md`) match the lowercase folder name.