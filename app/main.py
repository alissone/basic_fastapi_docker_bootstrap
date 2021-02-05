from typing import Optional
from fastapi import FastAPI, File, UploadFile
#import cv2
import numpy as np
from PIL import features

app = FastAPI()


@app.get("/")
def read_root():
    f = features.check_module('webp')
    print(f)
    return {"Hello": str(f)}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}




#@app.post('/file')
#def _file_upload(my_file: UploadFile = File(...)):
#    image_bytes = my_file.file.read()
#    decoded = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)
#    return {"file_size": my_file.filename}
