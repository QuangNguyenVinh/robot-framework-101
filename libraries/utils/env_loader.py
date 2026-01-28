from dotenv import load_dotenv
from pathlib import Path


class EnvLoader:
    def load(self, relative_path: str) -> None:
        """
        Load env file using path relative to project root (cwd).
        """
        env_path = Path(relative_path).resolve()

        if not env_path.exists():
            raise RuntimeError(f".env file not found: {env_path}")

        loaded = load_dotenv(dotenv_path=env_path, override=True)

        if not loaded:
            raise RuntimeError(f"Failed to load env file: {env_path}")
