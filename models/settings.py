from pydantic import BaseModel
from typing import Optional

class ScrapeSettings(BaseModel):
    max_pages: Optional[int] = None
    proxy: Optional[str] = None
    

