import numpy as np
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
import requests

app =FastAPI()

getT = 'http://172.17.0.2:80/api/model/'
#getT = 'http://localhost:5000/api/model/'  

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "conpre  input"}

@app.post("/api/product")
async def read_str(request: Request):
    data = await request.json()
    data_list = data["data"]
    all_numbers = all(isinstance(item, int) for item in data_list)
    if all_numbers:
        if (len(data_list)==7):
            res = requests.get(getT, json=data)
            return res.json()
        else:
            return "Incomplete information entered. Please enter again."
    else:
        return "Entered incorrect information. Please enter again."

   
# @app.post("/api/model")
# async def predi(request: Request):
#     data = await request.json()
#     data_list = data["data"]
#     Tr=requests.get(getT,json=data_list)
#     if(Tr):
#         reshaped_data = np.array(data_list).reshape(1, -1)
#         res = m.predict(reshaped_data)
#         return {"Product": res.tolist()}
#     else:
#         return "Entered incorrect information. Please enter again."
       