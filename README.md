# Security audit: CosmosOS/Cosmos

Date: 2026-11-12 | Auditor: [mutsuumii](https://github.com/mutsuumii)

## Summary

Found 5 issue(s): 4 high, 1 medium.

## Findings

### 1. [MEDIUM] Insecure temp file creation

**CWE-377** | `.github/scripts/aggregate-coverage.py` line 150

Predictable temp file path allows symlink attacks by local users.

```
with open("/tmp/coverage_pr_comment.md", "w") as f:
```

**Fix:** Use tempfile.mkstemp() or tempfile.NamedTemporaryFile() which creates files atomically.
---

### 2. [HIGH] Use-after-free pattern

**CWE-416** | `src/Cosmos.Kernel.Native.MultiArch/ACPI/uacpi_host.c` line 99

Freed pointer not immediately set to NULL. Dangling pointer reuse corrupts heap and can lead to code execution.

```
__cosmos_heap_free(mem);
```

**Fix:** Set pointer to NULL immediately after free(). Enable AddressSanitizer in CI: -fsanitize=address.
---

### 3. [HIGH] Use-after-free pattern

**CWE-416** | `src/Cosmos.Kernel.Native.MultiArch/ACPI/uacpi_host.c` line 206

Freed pointer not immediately set to NULL. Dangling pointer reuse corrupts heap and can lead to code execution.

```
uacpi_kernel_free(handle);
```

**Fix:** Set pointer to NULL immediately after free(). Enable AddressSanitizer in CI: -fsanitize=address.
---

### 4. [HIGH] Use-after-free pattern

**CWE-416** | `src/Cosmos.Kernel.Native.MultiArch/ACPI/uacpi_host.c` line 273

Freed pointer not immediately set to NULL. Dangling pointer reuse corrupts heap and can lead to code execution.

```
uacpi_kernel_free(handle);
```

**Fix:** Set pointer to NULL immediately after free(). Enable AddressSanitizer in CI: -fsanitize=address.
---

### 5. [HIGH] Use-after-free pattern

**CWE-416** | `src/Cosmos.Kernel.Native.MultiArch/ACPI/uacpi_host.c` line 479

Freed pointer not immediately set to NULL. Dangling pointer reuse corrupts heap and can lead to code execution.

```
uacpi_kernel_free(handle);
```

**Fix:** Set pointer to NULL immediately after free(). Enable AddressSanitizer in CI: -fsanitize=address.
---
