from fastapi import FastAPI, Header, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from aux_functions import temp_file
from upload_video import upload_video

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)


@app.get('/')
async def main():
    return {'message': 'Welcome to Godkout'}

@app.post('/upload_video/')
async def upload_yt_video(title:str = Form(),
                     video:UploadFile = File()):
    """
    Upload a video to youtube
    """
    path_video = temp_file(upload_file=video, 
                           allowed_extension=['.mp4'])
    video_url = upload_video(title=title, 
                             path_video=path_video)
    return video_url


