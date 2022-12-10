from pathlib import Path
from tempfile import NamedTemporaryFile
import shutil
from fastapi import UploadFile, HTTPException

def temp_file(upload_file:UploadFile, 
              allowed_extension:list) -> Path:
    try:
        suffix = Path(upload_file.filename).suffix
        with NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
            shutil.copyfileobj(upload_file.file, tmp)
            tmp_path = Path(tmp.name)
            if suffix not in allowed_extension:
                error_msg = 'Format not supported, make sure you select the correct file.'
                raise HTTPException(status_code=415,
                                    detail={'message': error_msg})
    except Exception:
        error_msg = 'File problems, make sure you have selected the correct file.'
        raise HTTPException(status_code=415,
                            detail={'message': error_msg})
    finally:
        upload_file.file.close()
    return tmp_path