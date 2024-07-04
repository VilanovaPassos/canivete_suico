import gradio as gr
from pytube import YouTube
import os
import tempfile
import moviepy.editor as mpe


#definicoes caminhos
HOLYRICS_VIDEO = "C:\\Holyrics\\Holyrics\\files\\media\\video" 
HOLYRICS_AUDIO = "C:\\Holyrics\\Holyrics\\files\\media\\audio"
TEMPORARIO = tempfile.gettempdir()

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

def realiza_download_video_resolucao(video_link, resolution, save_path, progress=gr.Progress()):
    # ATENÇÃO USANDO ESTE METODO O PROGRAMA IRA DEMORAR SIGNIFICATIVAMENTE MAIS, POIS FARA O DOWNLOAD
    # DA STREAM DE VIDEO E DE AUDIO SEPARADO, TENDO QUE RENDERIZAR UM NOVO ARQUIVO DE VIDEO PARA JUNTAR OS DOIS

    # Download video and rename
    progress(0.3, desc="Procurando video..")
    video_st = YouTube(video_link).streams.filter(subtype='mp4', resolution=resolution).first().download(save_path, "clip.mp4")

    progress(0.55, desc="Iniciando download!")
    # Download audio and rename
    audio_st =YouTube(video_link).streams.filter(only_audio=True).first().download(save_path, "audio.mp3")

    progress(0.65, desc="Baixando!!!")
    #titulo do video
    title = YouTube(video_link).title
    title = title.replace(" ","_").replace("|","") #remove | e espaços do titulo
    salvar = f"{save_path}\\{title}.mp4"
    print(salvar)

    progress(0.7, desc="Baixando..")
    # Setting the audio to the video
    video = mpe.VideoFileClip(video_st)
    audio = mpe.AudioFileClip(audio_st)
    final = video.set_audio(audio)

    progress(0.85, desc="Terminando Download...")
    # Output result
    final.write_videofile(salvar)


    progress(0.95, desc="Salvando")
    # Delete video and audio to keep the result
    os.remove(video_st)
    os.remove(audio_st)


    return salvar

def realiza_download_video(video_link, save_path, progress=gr.Progress()):
    progress(0.3, desc="Procurando video..")
    yt = YouTube(video_link)
     
    progress(0.55, desc="Iniciando download!")
    title = yt.title
    title = title.replace("|", "") #retira | do titulo do video, pode causar problemas com salvamento

    progress(0.7, desc="Baixando..")
    video = yt.streams.filter().get_highest_resolution().download(save_path, f"{title}.mp4") #faz o download da stream com maior qualidade disponivel com audio

    progress(0.85, desc="Salvando video...")
    return os.path.abspath(video)


def realiza_download_audio(video_link, save_path, progress=gr.Progress()):
    #baixar como audio
    progress(0.3, desc="Procurando video..")
    video_url = YouTube(video_link)

    progress(0.55, desc="Iniciando download!")
    video = video_url.streams.filter(only_audio = True).first()

    progress(0.7, desc="Baixando..")
    out_file = video.download(save_path)

    progress(0.85, desc="Salvando video...")
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    return new_file

def video_downloader(video_link, tipo,resolution, como_salvar, progress=gr.Progress()):
    #verifica se url é valida
    progress.visible=True
    progress(0.1, desc="Iniciando...")
    if video_link.split("//")[0] == "https:" :

        #Verifica tipo e encaminha para download de video ou audio 
        if tipo != "somente audio":
            #verifica se salvamento sera no holyrics
            if como_salvar == "sim":
                save_path = HOLYRICS_VIDEO

                #verifica se uma resolucao foi escolhida 
                if resolution != "automatico":
                    base = realiza_download_video_resolucao(video_link, resolution, save_path)
                else:
                    base = realiza_download_video(video_link, save_path)

                gr.Warning("Video Baixado!")
                return "DOWNLOAD REALIZADO COM SUCESSO!!! VIDEO SALVO NA PASTA DO HOLYRICS!!", gr.DownloadButton(label="salvar", value=base, visible=False)
            else:
                save_path = TEMPORARIO

                #verifica se uma resolucao foi escolhida 
                if resolution != "automatico":
                    base = realiza_download_video_resolucao(video_link, resolution, save_path)
                else:
                    base = realiza_download_video(video_link, save_path)

                gr.Warning("Video Baixado!")
                return "DOWNLOAD REALIZADO COM SUCESSO!!! ESCOLHA UMA PASTA PARA SALVARO O ARQUIVO", gr.DownloadButton(label="salvar", value=base, visible=True)
        else:
            if como_salvar == "sim":
                base = realiza_download_audio(video_link, HOLYRICS_AUDIO)
                gr.Warning("Video Baixado!")
                return "DOWNLOAD REALIZADO COM SUCESSO!!! VIDEO SALVO NA PASTA DO HOLYRICS!!", gr.DownloadButton(label="salvar", value=base, visible=False)
            else:
                base = realiza_download_audio(video_link, TEMPORARIO)
                gr.Warning("Video Baixado!")
                return "DOWNLOAD REALIZADO COM SUCESSO!!! ESCOLHA UMA PASTA PARA SALVARO O ARQUIVO", gr.DownloadButton(label="salvar", value=base, visible=True)
    else:
        gr.Error("URL INVALIDA!!!")
            

# ************************** PAGINAS *******************************

with gr.Blocks(css=css, title="Youtube Downloader", js=js_func) as demo:
    with gr.Tab("Youtube download"):
        gr.Markdown("Fazer download video youtube")

        url_input = gr.Textbox(label="", placeholder="Cole a URL do video aqui", elem_classes="url")

        tipo_input = gr.Radio(label="selecione a resolução", choices=["video", "somente audio"], value="video")

        como_salvar_input = gr.Radio(label="Salvar arquivo direto no holyrics?", choices=["sim", "não"], value="sim")

        download_button = gr.Button("Baixar")

        with gr.Accordion(label="Avançado", open=False):
            gr.Markdown("ATENÇÃO!! A escolha de qualquer resolução aumentara muito o tempo de download!!")
            resolution_input = gr.Radio(label="resolução", choices=["144p", "360p", "480p", "720p", "1080p", "automatico"], value="automatico", )

        progress_output = gr.Textbox(label="")



        salvar_output = gr.DownloadButton("Salvar Como", visible=False)

        download_button.click(fn=video_downloader, inputs=[url_input, tipo_input, resolution_input, como_salvar_input], outputs=[progress_output, salvar_output])
    with gr.Tab("Conversor"):
        gr.Markdown("CONVERSOR PDF ---> JPEG")

if __name__ == "__main__":
    os.system('explorer http://127.0.0.1:80') #abre navegador 
    demo.launch(server_port=80, quiet=True, show_api=False)