from fastapi import UploadFile
from sqlmodel import Field, Session, SQLModel,select,insert,update
from typing import Optional
import datetime,uuid
from . import engine,client,BUCKET_NAME

class MessageData(SQLModel, table=True):
    __tablename__ = "messages"
    id: str = Field(default=None, primary_key=True)
    message: Optional[str]= Field(default=None)
    src:  Optional[str] = None
    create_time: str = Field(default_factory=lambda: datetime.datetime.now(datetime.timezone.utc))

    @classmethod
    def getMessages(self):
        message_data=[]
        with Session(engine) as session:
            statement=select(MessageData).order_by(MessageData.create_time.desc())
            datas=session.exec(statement).fetchall()
            for data in datas:
                if data.src:
                    src="https://d115hy679wmzms.cloudfront.net/"+data.src
                else:
                    src=""
                message_data.append([data.message,src])
            return {"status":"success","message_data":message_data}
    
    @classmethod
    def createMessage(self,message:str,image:UploadFile):
        if message or image: 
            if image !='':
                filename=None
                if (image.content_type =="image/png" or image.content_type =="image/jpeg" or image.content_type =="image/jpg") and image.size<=2000000:
                    filename="img/img-"+str(uuid.uuid4())+"."+str.split(image.filename,".")[1]
                    contents=image.file.read()
                    response = client.put_object(Body=contents,Bucket=BUCKET_NAME,Key=filename)
                dt = datetime.datetime.now(datetime.timezone.utc)
                dt_sec = dt.isoformat(timespec='seconds') 
                dt_iso = dt_sec.replace("+00:00", "Z")
                m=MessageData(id=str(uuid.uuid4()),message=message,src=filename,create_time=dt_iso)
                with Session(engine) as session:
                    session.add(m)
                    session.commit()
                if filename:
                    filename="https://d115hy679wmzms.cloudfront.net/"+filename
                return {"status":"success","message_data":[[message,filename]]}
