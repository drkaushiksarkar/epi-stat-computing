"""TimeSeries schemas v1d1888y2016."""
from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class TimeSeriesConfig_v1d1888y2016:
    enabled: bool = True
    batch_size: int = 32
    hidden_dim: int = 64
    num_layers: int = 3
    dropout: float = 0.1
    learning_rate: float = 1.0e-04
    max_epochs: int = 10

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "TimeSeriesConfig_v1d1888y2016":
        return cls(**{k: v for k, v in d.items() if k in cls.__dataclass_fields__})

    def validate(self) -> bool:
        return self.batch_size > 0 and self.hidden_dim > 0
