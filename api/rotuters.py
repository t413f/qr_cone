from fastapi import APIRouter
from loguru import logger
from typing import Optional
from schemas.schemas import QRin
from fastapi import Depends
from services.qrgenerator import QR_manager

router = APIRouter(
    prefix='/qrgen',
)

@router.post('/')
async def get_qr(req: QRin = Depends()):
    QR_manager.create_simple_qr(content=req.content, colored=req.color)
    return await QR_manager.base64_from_img()
