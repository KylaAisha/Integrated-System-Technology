from fastapi import FastAPI, File, UploadFile
import json
app = FastAPI(debug = True)
@app.post("/upload_files/")
def create_upload_files(upload_file: UploadFile = File(...)):
    json_data = json.load(upload_file.file);
    return{"data_in_file": json_data}