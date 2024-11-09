from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import shutil
import os
import time

app = FastAPI()

# Define the directory to save uploaded files
UPLOAD_DIRECTORY = "uploaded_files"

# Ensure the directory exists
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

def get_unique_filename(file_path: str) -> str:
    """
    Generates a unique filename by appending a timestamp or a random string if file already exists.
    """
    if os.path.exists(file_path):
        # Append timestamp to the file name to avoid overwriting
        base, extension = os.path.splitext(file_path)
        timestamp = time.strftime("%Y%m%d%H%M%S")
        unique_file_path = f"{base}_{timestamp}{extension}"
        return unique_file_path
    return file_path

# Define the endpoint to upload a file
@app.post("/uploadfile/")
async def upload_file(file: UploadFile = File(...)):
    # Get the file name and location
    file_location = os.path.join(UPLOAD_DIRECTORY, file.filename)
    
    # Ensure the file name is unique (i.e., no overwriting)
    file_location = get_unique_filename(file_location)
    
    # Save the file
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return JSONResponse(content={"filename": file.filename, "file_location": file_location}, status_code=200)

