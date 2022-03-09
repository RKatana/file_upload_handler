import shutil, os, pathlib
from typing import Dict
from fastapi import (
                        FastAPI, 
                        UploadFile, 
                        File
                    )


app = FastAPI()

@app.post('/file-upload/')
async def file_uploader(file: UploadFile = File(...)) -> Dict:
    """
    A helper function to upload video files
    Args: file - An instance of UploadFile type
    """
    file_dir = os.getcwd()+'/files/'
    filename = file.filename
    try:
        with open(f"{file_dir}/{filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer )
    except FileNotFoundError:
        os.mkdir(os.getcwd()+'/files/')
        file_dir = os.getcwd()+'/files/'
        with open(f"{file_dir}{filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer )
    
    path_ = os.path.abspath(buffer.name)#We can use os.path.relpath(buffer.name), if we need the relative path
    file_type = pathlib.Path(buffer.name).suffix[1:].upper()
    file_size = f"{os.path.getsize(path_)/1000000} MB"
    context = {
        'file_name': filename,
        'file_path': path_,
        'file_type': file_type,
        'file_size': file_size
    }
    return context