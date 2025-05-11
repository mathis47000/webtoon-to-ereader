from dataclasses import dataclass, field
from typing import List, Dict
from datetime import datetime

@dataclass
class Webtoon:
    id: str
    name: str
    link: str
    last_ep: Dict[str, str] = field(default_factory=dict)
    download_list: List[str] = field(default_factory=list)
    
