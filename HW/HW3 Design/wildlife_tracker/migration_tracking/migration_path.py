
from dataclasses import dataclass
from typing import Optional
from wildlife_tracker.habitat_management.habitat import Habitat

@dataclass
class MigrationPath:
    path_id: int
    species: str
    start_location: Habitat
    destination: Habitat
    duration: Optional[int] = None