import os.path

from configurations import values


class DirectoryPathValue(values.PathValue):
    """A PathValue requiring that its path is a directory, optionally creating it if necessary."""

    ensure_exists: bool

    def __init__(self, *args, ensure_exists: bool = False, **kwargs) -> None:
        self.ensure_exists = ensure_exists
        super().__init__(*args, **kwargs)

    def setup(self, name: str) -> str:
        value = super().setup(name)
        if os.path.exists(value) and not os.path.isdir(value):
            raise ValueError(f"Path {repr(value)} is not a directory.")
        if self.ensure_exists:
            os.makedirs(value, exist_ok=True)
        return value
