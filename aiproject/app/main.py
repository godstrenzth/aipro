from fastapi import FastAPI, Request
from joblib import dump, load
import numpy as np

app = FastAPI() 

m = load(f'model/modelpro1.joblib')
#m = load(r'..\model\modelpro1.joblib')

@app.get("/")
def read_root():
    return {"test product"}


@app.get("/api/model")
async def predi(request: Request):
    data = await request.json()
    data_list = data["data"]
    reshaped_data = np.array(data_list).reshape(1, -1)
    res = m.predict(reshaped_data)
    return {"Product": res.tolist()}

    
