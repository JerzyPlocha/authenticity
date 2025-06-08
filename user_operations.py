from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    """Simple user data representation."""
    user_id: int
    name: str
    email: str


class UserOperations(ABC):
    """Interface defining basic user CRUD operations."""

    @abstractmethod
    def create_user(self, name: str, email: str) -> User:
        """Create a new user and return the created :class:`User`."""
        raise NotImplementedError

    @abstractmethod
    def get_user(self, user_id: int) -> Optional[User]:
        """Retrieve a user by their unique identifier."""
        raise NotImplementedError

    @abstractmethod
    def update_user(self, user_id: int, name: Optional[str] = None, email: Optional[str] = None) -> Optional[User]:
        """Update a user's information."""
        raise NotImplementedError

    @abstractmethod
    def delete_user(self, user_id: int) -> bool:
        """Delete a user and return ``True`` if successful."""
        raise NotImplementedError
