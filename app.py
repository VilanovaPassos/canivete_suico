import gradio as gr
import os
import socket
import tempfile


#definicoes caminhos
HOLYRICS_VIDEO = "C:\\Holyrics\\Holyrics\\files\\media\\video" 
HOLYRICS_AUDIO = "C:\\Holyrics\\Holyrics\\files\\media\\audio"
TEMPORARIO = tempfile.gettempdir()
#Pega indereço IP
IP_ADDR = socket.gethostbyname(socket.gethostname())

#CSS
css = """
.url textarea {
  background-color: red !important;
  padding-left: 55px !important;
  background: url("https://cdn1.iconfinder.com/data/icons/logotypes/32/youtube-512.png") no-repeat left !important;
  background-size: 50px !important;
}

footer {visibility: hidden}
"""
#javaScript força modo escuro
js_func = """
function refresh() {
    const url = new URL(window.location);

    if (url.searchParams.get('__theme') !== 'dark') {
        url.searchParams.set('__theme', 'dark');
        window.location.href = url.href;
    }
}
"""



def realiza_download_video(video_link, save_path, resolucao, nome="%(title)s"):
    #baixar video
    os.system(f"yt-dlp -P \"{save_path}\" -S \"res:{resolucao},vcodec:264,acodec:m4a\" -o \"{nome}.%(ext)s\" {video_link}") 

def realiza_download_audio(video_link, save_path, nome="%(title)s"):
    #baixar como audio
    os.system(f"yt-dlp -P \"{save_path}\" -x --audio-format mp3 -o \"{nome}.%(ext)s\" {video_link}")
    

def video_downloader(video_link, tipo, resolution, como_salvar, progress=gr.Progress()):
    #verifica se url é valida
    progress.visible=True
    progress(0.1, desc="Iniciando...")
    if video_link.split("//")[0] == "https:" :

        #Verifica tipo e encaminha para download de video ou audio 
        if tipo != "somente audio":
            #verifica se salvamento sera no holyrics
            if como_salvar == "sim":
                realiza_download_video(video_link, HOLYRICS_VIDEO, resolution)

                gr.Warning("Video Baixado!")
                return "DOWNLOAD REALIZADO COM SUCESSO!!! VIDEO SALVO NA PASTA DO HOLYRICS!!", gr.DownloadButton(label="salvar", value="base", visible=False)
            else:
                realiza_download_video(video_link, TEMPORARIO, resolution, "temp")

                gr.Warning("Video Baixado!")
                return "DOWNLOAD REALIZADO COM SUCESSO!!! ESCOLHA UMA PASTA PARA SALVARO O ARQUIVO", gr.DownloadButton(label="salvar", value=f"{TEMPORARIO}\\temp.mp4", visible=True)
        else:
            if como_salvar == "sim":
                realiza_download_audio(video_link, HOLYRICS_AUDIO)
                gr.Warning("Video Baixado!")
                return "DOWNLOAD REALIZADO COM SUCESSO!!! VIDEO SALVO NA PASTA DO HOLYRICS!!", gr.DownloadButton(label="salvar", value="base", visible=False)
            else:
                realiza_download_audio(video_link, TEMPORARIO, "temp")
                gr.Warning("Video Baixado!")
                return "DOWNLOAD REALIZADO COM SUCESSO!!! ESCOLHA UMA PASTA PARA SALVARO O ARQUIVO", gr.DownloadButton(label="salvar", value=f"{TEMPORARIO}\\temp.mp3", visible=True)
    else:
        gr.Error("URL INVALIDA!!!")
            

# ************************** PAGINAS *******************************

with gr.Blocks(css=css, title="Youtube Downloader", js=js_func) as demo:
    with gr.Tab("Download"):
        gr.Markdown("Download de Videos")

        url_input = gr.Textbox(label="", placeholder="Cole a URL do video aqui", elem_classes="url")

        tipo_input = gr.Radio(label="selecione a resolução", choices=["video", "somente audio"], value="video")

        como_salvar_input = gr.Radio(label="Salvar arquivo direto no holyrics?", choices=["sim", "não"], value="sim")

        download_button = gr.Button("Baixar")

        with gr.Accordion(label="Outras Opções", open=False):
            gr.Markdown("ATENÇÃO!! A escolha de qualquer resolução aumentara muito o tempo de download!!")
            resolution_input = gr.Radio(label="resolução", choices=["144", "360", "480", "720", "1080", "automatico"], value="720", )

        progress_output = gr.Textbox(label="")



        salvar_output = gr.DownloadButton("Salvar Como", visible=False)

        download_button.click(fn=video_downloader, inputs=[url_input, tipo_input, resolution_input, como_salvar_input], outputs=[progress_output, salvar_output])
    with gr.Tab("Conversor"):
        gr.Markdown("CONVERSOR PDF ---> JPEG")

if __name__ == "__main__":
    os.system(f'start http://{IP_ADDR}') #abre navegador 
    demo.launch(server_name=IP_ADDR, server_port=80, quiet=True, show_api=False)