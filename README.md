# gk-dac

* Full-width panel (one row, spans full dashboard):
```
"gridPos": {"x": 0, "y": 0, "w": 24, "h": 6}
```

* Stack panels vertically (same x, increasing y):
```
{"x": 0, "y": 0, "w": 12, "h": 6},  # Top panel
{"x": 0, "y": 6, "w": 12, "h": 6}   # Below the top panel
```

* Multiple rows with different column spans:
```
{"x": 0, "y": 0, "w": 8, "h": 6},   # 1/3rd width
{"x": 8, "y": 0, "w": 8, "h": 6},   # Middle 1/3rd
{"x": 16, "y": 0, "w": 8, "h": 6}   # Right 1/3rd
```
