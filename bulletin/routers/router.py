from typing import Annotated

from fastapi import APIRouter,Request,Form,Depends,HTTPException,WebSocket,UploadFile
from fastapi.responses import HTMLResponse,RedirectResponse,JSONResponse,FileResponse,StreamingResponse
from starlette.templating import Jinja2Templates
from typing import Optional

import os

from models import MessageData

templates_path=os.path.join("..",os.path.split(os.path.dirname(os.path.abspath(__file__)))[0],"templates")
templates=Jinja2Templates(directory=templates_path)

router=APIRouter()

@router.get("/")
def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")

@router.get("/api/bulletin")
def index(request: Request):
    data=MessageData.getMessages()
    return JSONResponse(status_code=200,content=data)
@router.post("/api/bulletin")
def index(request: Request,message:Optional[str]=Form(...),image= Form(None)):
    data=MessageData.createMessage(message,image)
    return JSONResponse(status_code=200,content=data)