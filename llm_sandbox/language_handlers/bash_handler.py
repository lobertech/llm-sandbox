import logging

from llm_sandbox.const import SupportedLanguage
from llm_sandbox.language_handlers.base import AbstractLanguageHandler, LanguageConfig


class BashHandler(AbstractLanguageHandler):
    """Handler for Bash language."""

    def __init__(self, logger: logging.Logger | None = None) -> None:
        """Initialize the Bash handler."""
        super().__init__()

        self.config = LanguageConfig(
            name=SupportedLanguage.BASH,
            file_extension="sh",
            execution_commands=["bash {file}"],
            package_manager=None,
            is_support_library_installation=False,
            plot_detection=None,
        )
        self.logger = logger or logging.getLogger(__name__)

    def get_import_patterns(self, module: str) -> str:
        """Get the regex patterns for import statements."""
        # In Bash, sourcing a file is similar to importing.
        return r"^\s*(source|\.)\s+.*" + module + r".*"

    @staticmethod
    def get_multiline_comment_patterns() -> str:
        """Get the regex patterns for multiline comments."""
        # Bash does not have native multiline comments, but you can use some hacks. Let's just return a pattern that matches nothing.
        return r"(?!)"

    @staticmethod
    def get_inline_comment_patterns() -> str:
        """Get the regex patterns for inline comments."""
        return r"#.*$"
