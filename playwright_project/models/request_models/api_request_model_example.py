from dataclasses import dataclass, asdict
from typing import Optional, Dict, Any


@dataclass
class ApiRequestModelExample:
    id: Optional[int] = None
    type: Optional[str] = None
    status: Optional[str] = None
    user_id: Optional[str] = None
    limit: Optional[str] = None
    offset: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in asdict(self).items() if v is not None}
