from datetime import datetime
from typing import List
import uuid
from pydantic import BaseModel, constr
from typing import Optional

class SourceBaseSchema(BaseModel):
    source: str
    source_type: str
    source_tag: str
    from_date: datetime
    to_date: datetime
    frequency: Optional[str]
    source_id: Optional[int]
    last_update_date:  Optional[datetime]
    class Config:
        orm_mode = True


class CreateSourceSchema(SourceBaseSchema):
    pass


class SourceResponse(SourceBaseSchema):
    source_id: int
    source: str
    source_type: str
    source_tag: str
    last_update_date: datetime
    from_date: datetime
    to_date: datetime
    frequency: str

class UpdateSourceResponse(BaseModel):
    status: str
    class Config:
        orm_mode = True

class UpdateSourceSchema(BaseModel):
    source_id: int
    from_date: datetime
    to_date: datetime
    last_update_date: Optional[datetime] = datetime.now()

    class Config:
        orm_mode = True



