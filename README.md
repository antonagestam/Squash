# Squash

**Disclaimer:** Squash is still under development. It's not ready for production and is [fairly destructive](issues).

Squash is like pre-processors' `@extend`, but for CSS. It parses your stylesheets and finds selectors that have the same properties/values and combines them together under the same selector. This way it's possible make your stylesheets even more efficient than with ordinary CSS compression tools.

### Usage
```python
>>> from squash import squash
>>> print squash("""
.foo {
  background: red;
}
.bar {
  background: red;
  font-size: 12px;
}
""")
```

### Result
```css
.bar {
font-size: 12px;
}
.foo, .bar {
background: red;
}
```

### Benchmark
- `squash.benchmark.benchmark`

### Project Roadmap
- Turn into an easy-to-install/use package
