import os
from youtube_client import YouTubeClient
from google_drive_client import GoogleDriveClient
# By Matheus Frazatto Dias


def main():
    '''Função principal que gerencia a interação do usuário e o fluxo do programa. Chamando quando 
    necessário funções de download e upload vinda das classes YoutubeClient e GoogleDriveClient.'''
    yt_client = YouTubeClient()
    drive_client = GoogleDriveClient()

    print("\n| Bem-vindo ao YouDri!")
    while True:
        print("| Escolha uma opção:")
        print("| [1] Baixar Vídeo Para Drive: ")
        print("| [2] Sair: ")
        option = input(">>").lower().strip()

        if option == "1":
            print("\n| Insira a URL do vídeo do YouTube: ")
            video_url = input(">>")
            print("")
            print(
                f"\n| O Título <{yt_client.getTitle(video_url)}> está correto? <Y/N>")
            option = input(">>").lower().strip()

            if option in ["yes", "y", "sim", "s"]:
                print("\n >> Iniciando o processo de download e upload...")
                local_video_path = yt_client.download_video(video_url)

                if local_video_path and os.path.exists(local_video_path):
                    drive_link = drive_client.upload_file(
                        local_video_path, local_video_path)
                    if drive_link:
                        print(f"\n>> PROCESSO CONCLUÍDO")
                        print(
                            f">> O vídeo foi enviado com sucesso para o Google Drive.")
                        print(f">> Link de acesso: {drive_link}")

                    print(f">> Removendo o arquivo local: {local_video_path}")
                    os.remove(local_video_path)
                    print("Limpeza concluída.")

                else:
                    print(
                        "\n>> Não foi possível concluir o processo devido a um erro no download.")
            else:
                print(">> Reiniciando o processo...")
        if option == "2":
            print(">> Saindo...")
            break


if __name__ == "__main__":
    main()
