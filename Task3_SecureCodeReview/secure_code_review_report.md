# 🔍 Secure Code Review – Task 3 (CodeAlpha Internship)

## 📂 File Reviewed
`vulnerable_app.py`

---

### 1️⃣ Issue: Hardcoded Login Details
```python
if username == "admin" and password == "admin123":
