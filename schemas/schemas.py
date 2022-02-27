from pydantic import BaseModel
from typing import Optional
from fastapi import File, UploadFile, Form, Query


class QRin(BaseModel):
    color: Optional[str] = Query(...)
    content: Optional[str] = Query(...)
    file: Optional[UploadFile] = File(...)
