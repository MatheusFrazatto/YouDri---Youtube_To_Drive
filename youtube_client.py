import yt_dlp


class YouTubeClient:
    def __init__(self):
        '''Inicializa o cliente do YouTube com opções padrão.'''
        self.ydl_opts = {
            'outtmpl': '%(title)s.%(ext)s',
        }

    def download_video(self, video_url):
        '''Baixa o vídeo do YouTube e retorna o caminho do arquivo baixado.'''
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                print("Obtendo informações do vídeo...")
                info_dict = ydl.extract_info(video_url, download=False)
                file_path = ydl.prepare_filename(info_dict)
                print(f"Iniciando o download para o arquivo: '{file_path}'")
                ydl.download([video_url])

            print("\nDownload concluído com sucesso!")
            return file_path

        except Exception as e:
            print(f"\nOcorreu um erro durante o download: {e}")
            return None

    def getTitle(self, video_url):
        '''Obtém o título do vídeo do YouTube.'''
        try:
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                info_dict = ydl.extract_info(video_url, download=False)
                video_title = info_dict.get("title", "Sem título")
                return video_title
        except Exception as e:
            print(f"\nOcorreu um erro ao obter o título: {e}")
            return "Sem título"

