from enum import Enum
from typing import Set, Dict, Optional, Callable

from domain.pin import Pin


class FixtureState(Enum):
    FREE = "FREE"
    ASSEMBLING = "ASSEMBLING"
    COMPLETED = "COMPLETED"
    PENDING = "PENDING"


class Fixture:
    def __init__(self, name: str, states: Dict[FixtureState, Pin]):
        self.name = name
        self.states = states

    def __repr__(self):
        return f"Fixture(name={self.name}, states={self.states})"


class Workbench:
    def __init__(self, name: str, fixtures: Set[Fixture], rotation_func: Optional[Callable[[], None]] = None):
        self.name = name
        self.fixtures: Dict[str, Fixture] = {fixture.name: fixture for fixture in fixtures}
        self.rotation_func = rotation_func
        self.rotations = 0

    def get_available_states_for_given_fixture(self, fixture: Fixture) -> Dict[FixtureState, Pin]:
        return {state: pin for state, pin in fixture.states.items()}

    def rotate(self) -> int:
        if self.rotation_func:
            self.rotation_func()
            self.rotations = self.rotations + 1
            return self.rotations
        else:
            raise Exception(f"Rotation function not defined for workbench {self.name}")

    def __repr__(self):
        return f"Workbench(name={self.name}, fixtures={self.fixtures})"
