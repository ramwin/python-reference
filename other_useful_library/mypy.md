# mypy

## 单行配置
```
<error code>  # type: ignore[assignment]
```

## [配置](https://mypy.readthedocs.io/en/stable/config_file.html)
```
[mypy]
plugins =
    mypy_django_plugin.main

exclude = (?x)(
    ^one\.py$    # files named "one.py"
    | two\.pyi$  # or files ending with "two.pyi"
    | ^three\.   # or files starting with "three."
  )

[mypy.plugins.django-stubs]
django_settings_module = "project.settings"
strict_settings = false
```

* exclude
排除的时候还要再设置
```
[mypy-examples.*]
follow_imports = skip
```
[stack overflow的问题](https://stackoverflow.com/questions/67130900/why-is-mypy-checking-files-that-ive-excluded)
