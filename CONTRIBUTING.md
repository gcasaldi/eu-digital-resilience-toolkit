# Contributing to EU Digital Resilience Toolkit

Thank you for your interest in contributing! 🎉

## How to Contribute

### Reporting Bugs
- Use GitHub Issues with the "bug" label
- Include: OS, Python version, Streamlit version
- Provide steps to reproduce
- Screenshots help!

### Suggesting Features
- Use GitHub Issues with the "enhancement" label
- Explain the use case
- Consider compliance/privacy implications

### Code Contributions

1. **Fork & Clone**
   ```bash
   git clone https://github.com/YOUR_USERNAME/eu-digital-resilience-toolkit.git
   cd eu-digital-resilience-toolkit
   ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes**
   - Follow existing code style
   - Add comments for complex logic
   - Test locally with `streamlit run app.py`

4. **Commit**
   ```bash
   git commit -m "feat: add ISO 27001 module"
   ```
   Use conventional commits: `feat:`, `fix:`, `docs:`, `style:`, `refactor:`

5. **Push & PR**
   ```bash
   git push origin feature/your-feature-name
   ```
   Open a Pull Request on GitHub

## Code Style

- Use **4 spaces** for indentation (not tabs)
- Follow [PEP 8](https://pep8.org/) for Python
- Use descriptive variable names
- Add docstrings to functions

## Testing

Before submitting:
- [ ] Test both DORA and NIS2 modules
- [ ] Verify PDF generation works
- [ ] Check email sending (if configured)
- [ ] Test on mobile viewport (Streamlit responsive)

## Questions?

Open a Discussion or email giulia@example.com

Thank you! 🙏
