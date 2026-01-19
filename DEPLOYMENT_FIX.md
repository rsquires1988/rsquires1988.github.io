# GitHub Pages Deployment Fix

## Issue
The site at https://rsquires1988.github.io is showing a plain white page because GitHub Pages is serving outdated content from the `gh-pages` branch that references the old custom domain `https://rousebrowse.com` for all assets (CSS, JavaScript, images, etc.).

## Root Cause
1. The GitHub Actions workflow (`.github/workflows/deploy.yml`) successfully builds the Pelican site with the correct URL (`https://rsquires1988.github.io`)
2. However, the `gh-pages` branch contains old HTML files that were generated with the old custom domain
3. GitHub Pages is configured to deploy from BOTH the workflow artifacts AND the `gh-pages` branch
4. The `gh-pages` branch deployment runs after the workflow deployment, overwriting the correct content

## Solution
**Delete the `gh-pages` branch** to ensure only the GitHub Actions workflow deploys the site.

### Steps to Fix
1. Go to the repository settings
2. Navigate to "Settings" > "Pages"
3. Confirm that "Source" is set to "GitHub Actions" (not "Deploy from a branch")
4. Delete the `gh-pages` branch by running:
   ```bash
   git push origin --delete gh-pages
   ```
   OR via the GitHub web interface:
   - Go to the repository main page
   - Click on "branches" (shows "X branches")
   - Find the `gh-pages` branch
   - Click the trash icon to delete it

5. Once the branch is deleted, the next deployment from the GitHub Actions workflow will be the only source
6. The site should render correctly at https://rsquires1988.github.io

## Verification
After deleting the `gh-pages` branch:
1. Go to Actions tab
2. Manually trigger the "Deploy Pelican Site to GitHub Pages" workflow (or push to main branch)
3. Wait for the workflow to complete
4. Visit https://rsquires1988.github.io
5. The site should now display properly with the Pelican theme and content

## Technical Details
- The workflow builds the site using `make publish` which uses `publishconf.py`
- `publishconf.py` correctly sets `SITEURL = 'https://rsquires1988.github.io'`
- The output is uploaded as an artifact and deployed via `actions/deploy-pages@v4`
- All generated HTML files reference the correct domain for assets
