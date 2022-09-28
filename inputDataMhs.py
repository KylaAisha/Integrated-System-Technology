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
        else:
            new_info_mhs = {
                        "nim": nim_mhs,
                        "nama": nama_mhs
            }

            def write_json(new_data, filename='dataMhs.json'):
                with open(filename,'r+') as file:
                    file_data = json.load(file)
                    file_data["mhs"].append(new_data)
                    file.seek(0)
                    json.dump(file_data, file, indent = 4)
 
            write_json(new_info_mhs)
            return new_info_mhs
            
    raise HTTPException(
        status_code=404, detail=f'Item not found'
    )