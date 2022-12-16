from fastapi import FastAPI, Depends
import uvicorn
import dataschema
import models

from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session 

#create the database tables on app startup or reload on the engine configuration
Base.metadata.create_all(engine)

#get the session 
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

app = FastAPI()

@app.get("/")
def getItems(session: Session = Depends(get_session)):
    items = session.query(models.Item).all() #query all the items
    return items



@app.post("/")
def addItem(item:dataschema.Item, session = Depends(get_session)):
    item = models.Item(task = item.task, status = item.status)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@app.get("/{id}")
def getItem(id:int, session: Session = Depends(get_session)):
    item = session.query(models.Item).get(id)
    return item




@app.put("/{id}")
def updateItem(id:int, item:dataschema.Item, session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    itemObject.task = item.task
    session.commit()
    return itemObject



@app.delete("/{id}")
def deleteItem(id:int, session = Depends(get_session)):
    itemObject = session.query(models.Item).get(id)
    session.delete(itemObject)
    session.commit()
    session.close()
    return 'Item was deleted'










if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")