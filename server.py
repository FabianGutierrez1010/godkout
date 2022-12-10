import uvicorn


if __name__ == '__main__':
    API_PORT = 5050
    """Sin certificados Cliente/servidor"""
    uvicorn.run('app:app', host='0.0.0.0', port=API_PORT)

