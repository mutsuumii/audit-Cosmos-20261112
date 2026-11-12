# Insecure temp file creation
# CWE-377 | Severity: MEDIUM
# File: .github/scripts/aggregate-coverage.py line 150

**Risk:** Predictable temp file path allows symlink attacks by local users.

**Fix:** Use tempfile.mkstemp() or tempfile.NamedTemporaryFile() which creates files atomically.
