import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'client_gutierrezworkout.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

def upload_video(title:str, path_video:str):
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    upload_date_time = datetime.datetime(2020, 12, 25, 12, 30, 0).isoformat() + '.000Z'

    request_body = {
        'snippet': {
            'categoryI': 19,
            'title': title,
            'description': 'Hello World Description',
            'tags': ['Travel', 'video test', 'Travel Tips']
        },
        'status': {
            'privacyStatus': 'private',
            'publishAt': upload_date_time,
            'selfDeclaredMadeForKids': False, 
        },
        'notifySubscribers': False
    }

    mediaFile = MediaFileUpload(path_video)

    response = service.videos().insert(part='snippet,status',
                                    body=request_body,
                                    media_body=mediaFile)
    # print(dir(response))
    response_upload = response.execute()

    service.thumbnails().set(
        videoId=response_upload.get('id'),
        media_body=MediaFileUpload('thumbnail.png')
    ).execute()

    # print(response_upload)
    video_id = response_upload.get('id')
    video_url = f'URL: https://youtu.be/{video_id}'
    print(video_url)
    return video_url

# response = None
# while response is None:
#     status, response = response_upload.next_chunk()
#     if status:
#         sp = status.progress() * 100
#         print(f'Upload {sp} complete')

