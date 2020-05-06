def test_import():
    import {{ cookiecutter.module_name }}

    assert {{ cookiecutter.module_name }}.__version__ is not None
    assert len({{ cookiecutter.module_name }}.__version__) > 0
