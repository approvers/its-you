from datetime import timedelta

from pydantic import Field

from src.config.interface import ConfigIF


class DomainConfigIF(ConfigIF):
    REACT_PROBABILITY: float = Field(
        ge=0.0, lt=1.0, description="Probability to react to a message"
    )
    INTERVAL_FOR_SAME_TARGET_SEC: timedelta = Field(
        ge=timedelta(), description="Time interval to react to a same target"
    )
    DO_REACT_TO_GROUP: bool = Field(
        default=False, description="Whether or not to react to a group"
    )
    DO_REACT_TO_USER: bool = Field(
        default=True, description="Whether or not to react to a user"
    )
