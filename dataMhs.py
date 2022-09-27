from http.client import HTTPException
import json
from fastapi import FastAPI
with open("dataMhs.json","r") as read_file:
    data = json.load(read_file)
app = FastAPI()
@app.get('/mhs/{nim_mhs}')
async def read_data(nim_mhs: int,nama_mhs: str):
    for info_mhs in data['mhs']:
        if info_mhs['nim'] == nim_mhs and info_mhs['nama'] == nama_mhs:
            return info_mhs
    raise HTTPException(
        status_code=404, detail=f'Item not found'
    )