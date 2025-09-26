import google.auth
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


class GoogleDriveClient:
    '''Cliente para interagir com o Google Drive, incluindo autenticação e upload de arquivos.'''
    def __init__(self, credentials_file="credentials.json"):
        self.scopes = ["https://www.googleapis.com/auth/drive.file"]
        self.credentials_file = credentials_file
        self.service = self.authenticate()

    def authenticate(self):
        '''Autentica o cliente do Google Drive usando OAuth 2.0.'''
        creds = None
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file(
                "token.json", self.scopes)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_file, self.scopes
                )
                creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(creds.to_json())

        try:
            service = build("drive", "v3", credentials=creds)
            return service
        except HttpError as error:
            print(f"Ocorreu um erro ao criar o serviço do Drive: {error}")
            return None

    def upload_file(self, file_path, file_name):
        '''Faz upload de um arquivo para o Google Drive e retorna o link de acesso.'''
        if not self.service:
            print("Serviço do Google Drive não autenticado. Upload cancelado.")
            return None

        try:
            print(
                f"Iniciando o upload de '{file_name}' para o Google Drive...")
            file_metadata = {"name": file_name}
            media = MediaFileUpload(
                file_path, mimetype="video/mp4", resumable=True)
            file = (
                self.service.files()
                .create(body=file_metadata, media_body=media, fields="id, webViewLink")
                .execute()
            )
            link_do_video = file.get("webViewLink")
            print(f"Upload concluído! Link de acesso: {link_do_video}")
            return link_do_video

        except HttpError as error:
            print(f"Ocorreu um erro durante o upload: {error}")
            return None


