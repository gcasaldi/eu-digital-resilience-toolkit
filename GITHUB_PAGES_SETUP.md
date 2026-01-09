# GitHub Pages Setup Instructions

## ✅ Steps to Verify GitHub Pages is Working

### 1. Check Repository Settings

1. Go to https://github.com/gcasaldi/eu-digital-resilience-toolkit/settings/pages
2. Verify that:
   - **Source** is set to "GitHub Actions" (NOT "Deploy from a branch")
   - If you see "Deploy from a branch", change it to "GitHub Actions"

### 2. Check Workflow Status

1. Go to https://github.com/gcasaldi/eu-digital-resilience-toolkit/actions
2. Look for the "Deploy to GitHub Pages" workflow
3. Verify it completed successfully (green checkmark)
4. If failed, click on the workflow run to see error details

### 3. Wait for Deployment

After pushing changes:
- GitHub Actions workflow typically takes 1-3 minutes
- Watch the Actions tab for progress
- Once complete, site updates at https://gcasaldi.github.io/eu-digital-resilience-toolkit/

### 4. Clear Browser Cache

If changes don't appear:
```
Chrome/Edge: Ctrl + Shift + R (Windows) or Cmd + Shift + R (Mac)
Firefox: Ctrl + F5 (Windows) or Cmd + Shift + R (Mac)
Safari: Cmd + Option + R
```

Or open in incognito/private mode to bypass cache.

### 5. Test the Assessment Button

1. Open https://gcasaldi.github.io/eu-digital-resilience-toolkit/
2. Click "🚀 Start Risk Assessment" button
3. Check browser console (F12) for any JavaScript errors
4. Verify phase navigation works

## 🐛 Troubleshooting

### Button Not Working

**Check browser console (F12 → Console tab):**

Expected: No errors, should show:
```
DOM loaded, initializing...
Assessment engine loaded successfully
```

Common issues:
- `assessmentEngine is undefined` → JavaScript file not loading
- `startAssessment is not defined` → Event listener not attached
- CORS errors → GitHub Pages misconfigured

### Pages Not Updating

**Force rebuild:**
```bash
git commit --allow-empty -m "Trigger Pages rebuild"
git push origin main
```

### 404 Error on GitHub Pages

1. Check Settings → Pages → ensure "GitHub Actions" is selected
2. Verify `.nojekyll` file exists in root directory
3. Verify workflow completed successfully in Actions tab

### CSS/JS Not Loading

**Check paths in index.html:**
- Should be relative: `assets/css/style.css`
- NOT absolute: `/assets/css/style.css`
- NOT with domain: `https://...`

## 📋 Files Checklist

Required files for GitHub Pages:
- ✅ `index.html` (entry point)
- ✅ `.nojekyll` (disables Jekyll processing)
- ✅ `.github/workflows/pages.yml` (deployment workflow)
- ✅ `assets/js/assessment-2026.js` (assessment engine)
- ✅ `assets/js/main-2026.js` (UI controller)
- ✅ `assets/css/style.css` (styles)

## 🔍 Debugging Commands

Check deployment status:
```bash
# View recent commits
git log --oneline -5

# Check current branch
git branch -a

# View workflow file
cat .github/workflows/pages.yml

# Check if .nojekyll exists
ls -la | grep nojekyll
```

## 📞 Get Help

If issues persist:
1. Check Actions tab for workflow errors
2. Review browser console for JavaScript errors
3. Open an issue: https://github.com/gcasaldi/eu-digital-resilience-toolkit/issues

## ✅ Success Indicators

When everything works:
- ✅ Workflow shows green checkmark in Actions tab
- ✅ Site loads at https://gcasaldi.github.io/eu-digital-resilience-toolkit/
- ✅ Start button opens assessment without errors
- ✅ All 6 phases navigate correctly
- ✅ Results generate with export options
