Sure! Below is a detailed `README.md` content for your GitHub repository, which explains how to set up, run, and use the FastAPI file upload application.

---

# FastAPI File Upload

A simple FastAPI application that allows users to upload files via HTTP and save them to a specified directory on the server. The app automatically handles file naming conflicts by appending a timestamp to filenames, ensuring that files with the same name do not overwrite each other. This project demonstrates basic file upload functionality with FastAPI.

## Features

- Upload files through an HTTP POST request.
- Files are saved to a server-side directory (`uploaded_files`).
- Automatically renames files if they already exist, appending a timestamp to avoid overwriting.
- Uses FastAPI for handling requests and Python's standard libraries for file manipulation.

## Requirements

To run this project, you need:

- Python 3.7 or higher
- FastAPI
- Uvicorn (for running the app)

## Installation and Setup

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/fastapi-file-upload.git
cd fastapi-file-upload
```

### 2. Create a Virtual Environment (Optional, but recommended)

If you're using `venv` (recommended), you can set up a virtual environment to keep dependencies isolated:

```bash
python -m venv .env
source .env/bin/activate  # On Linux/MacOS
.env\Scripts\activate     # On Windows
```

### 3. Install Dependencies

Install FastAPI and Uvicorn (for running the application) using `pip`:

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, you can manually install the dependencies:

```bash
pip install fastapi uvicorn
```

### 4. Ensure the `uploaded_files` Directory Exists

The application will save uploaded files to a folder named `uploaded_files`. You can create this directory manually or let the app handle it.

```bash
mkdir uploaded_files
```

The app will automatically create the `uploaded_files` directory if it does not exist.

## Running the Application

### 1. Run the FastAPI Application

You can run the FastAPI app using `uvicorn`, which is the ASGI server recommended for FastAPI.

```bash
uvicorn main:app --reload
```

- The app will be available at `http://127.0.0.1:8000`.
- `--reload` makes the server restart automatically when you change the code.

### 2. Open the Swagger Documentation

FastAPI provides interactive documentation for your APIs using Swagger UI. You can access it by navigating to:

```
http://127.0.0.1:8000/docs
```

This UI allows you to test the file upload functionality directly from the browser.

## Usage

### Uploading a File

You can upload a file using the `/uploadfile/` endpoint.

#### Method: POST  
#### URL: `/uploadfile/`

- **Request Body:**
  - `file`: The file you want to upload. This is a `multipart/form-data` request.

#### Example Request Using cURL:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/uploadfile/' \
  -F 'file=@/path/to/your/file.txt'
```

#### Example Response:

```json
{
  "filename": "file.txt",
  "file_location": "uploaded_files/file.txt"
}
```

If you upload a file with the same name (`file.txt`), the app will rename it to avoid overwriting, and the response will include the new filename:

```json
{
  "filename": "file.txt",
  "file_location": "uploaded_files/file_20231109123045.txt"
}
```

### File Renaming Logic

- If a file with the same name already exists in the `uploaded_files` directory, the app will append the current timestamp to the filename to make it unique.
- For example, if you upload `file.txt` twice, the first file will be saved as `uploaded_files/file.txt` and the second will be saved as `uploaded_files/file_20231109123045.txt`.

## Project Structure

```plaintext
fastapi-file-upload/
│
├── main.py              # FastAPI app and file upload logic
├── .gitignore           # Git ignore file for common unnecessary files
├── requirements.txt     # Python dependencies for the project
├── uploaded_files/      # Directory where uploaded files are saved
├── README.md            # This README file
```

## Requirements File

If you're using a `requirements.txt` file for dependency management, you can generate it with the following command:

```bash
pip freeze > requirements.txt
```

## Development

To contribute or modify the project, follow these steps:

1. Fork the repository.
2. Clone your forked repository.
3. Create a new branch.
4. Make your changes and test the application.
5. Submit a pull request (PR) with a detailed description of your changes.

### Code Style

- Follow PEP 8 guidelines for Python code.
- Use descriptive commit messages.
- Keep functions and methods small and focused on a single task.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/) for the easy-to-use framework.
- [Uvicorn](https://www.uvicorn.org/) for serving the FastAPI app.

---