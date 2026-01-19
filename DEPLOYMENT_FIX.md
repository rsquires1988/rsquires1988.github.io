# GitHub Pages Deployment Fix

## Issue
The site at https://rsquires1988.github.io is showing a plain white page because GitHub Pages is serving outdated content from the `gh-pages` branch that references the old custom domain `https://rousebrowse.com` for all assets (CSS, JavaScript, images, etc.).

## Root Cause
1. The GitHub Actions workflow (`.github/workflows/deploy.yml`) successfully builds the Pelican site with the correct URL (`https://rsquires1988.github.io`)
2. However, GitHub Pages is currently configured to deploy from the `gh-pages` branch, not from the workflow artifacts
3. The `gh-pages` branch contains old HTML files that were generated with the old custom domain
4. Since GitHub Pages is set to "Deploy from a branch," it ignores the workflow deployments and only serves content from the gh-pages branch

## Solution
Change the GitHub Pages source to "GitHub Actions" and delete the outdated `gh-pages` branch.

### Steps to Fix (REQUIRED)

#### Step 1: Change GitHub Pages Source (CRITICAL)
1. Go to https://github.com/rsquires1988/rsquires1988.github.io/settings/pages
2. Under "Build and deployment" > "Source"
3. Change from "Deploy from a branch" to **"GitHub Actions"**
4. Click Save

This is the CRITICAL step! Without this, GitHub Pages will continue to deploy from the gh-pages branch instead of the workflow artifacts.

#### Step 2: Delete the gh-pages Branch (Recommended)
Delete the `gh-pages` branch to prevent confusion:

**Option A - Command Line:**
```bash
git push origin --delete gh-pages
```

**Option B - GitHub Web Interface:**
1. Go to https://github.com/rsquires1988/rsquires1988.github.io/branches
2. Find the `gh-pages` branch
3. Click the trash icon to delete it

#### Step 3: Trigger a New Deployment
1. Go to https://github.com/rsquires1988/rsquires1988.github.io/actions
2. Click on "Deploy Pelican Site to GitHub Pages" workflow
3. Click "Run workflow" > "Run workflow" to manually trigger it
4. OR simply push a commit to the `main` branch

#### Step 4: Verify
- Wait for the workflow to complete (should take ~30 seconds)
- Visit https://rsquires1988.github.io
- The site should now display properly with the Pelican theme and content

## Why This Happens
GitHub Pages can be configured to deploy from one of two sources:
1. **Deploy from a branch** (legacy method) - GitHub automatically builds and deploys when a specified branch is updated
2. **GitHub Actions** (modern method) - Custom workflows control the build and deployment process

This repository is currently set to "Deploy from a branch" (using the gh-pages branch), which means GitHub Pages ignores the workflow artifacts and only serves the outdated content from the gh-pages branch.

## How to Confirm It's Fixed
After changing the Pages source to "GitHub Actions":
1. Check https://github.com/rsquires1988/rsquires1988.github.io/deployments
2. You should see deployments from the "github-pages" environment (from the workflow)
3. The "pages build and deployment" workflow should no longer run automatically
4. Visit https://rsquires1988.github.io - the site should render with full styling and correct content

## Technical Details
- The workflow builds the site using `make publish` which uses `publishconf.py`
- `publishconf.py` correctly sets `SITEURL = 'https://rsquires1988.github.io'`
- The output is uploaded as an artifact and deployed via `actions/deploy-pages@v4`
- All generated HTML files reference the correct domain for assets
