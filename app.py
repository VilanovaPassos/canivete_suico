import gradio as gr
import fitz
import os
import socket
import tempfile


#definicoes caminhos
HOLYRICS_VIDEO = "C:\\Holyrics\\Holyrics\\files\\media\\video" 
HOLYRICS_AUDIO = "C:\\Holyrics\\Holyrics\\files\\media\\audio"
HOLYRICS_IMAGEM = "C:\\Holyrics\\Holyrics\\files\\media\\image"
TEMPORARIO = tempfile.gettempdir()
#Pega indereço IP
IP_ADDR = socket.gethostbyname(socket.gethostname())

#CSS https://cdn1.iconfinder.com/data/icons/logotypes/32/youtube-512.png

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

# ************************ Youtube Downloader ************************

def realiza_download_video(video_link, save_path, resolucao, nome="%(title)s"):
    #baixar video
    os.system(f"yt-dlp -P \"{save_path}\" -S \"res:{resolucao},vcodec:264,acodec:m4a\" -o \"{nome}.%(ext)s\" {video_link}") 

def realiza_download_audio(video_link, save_path, nome="%(title)s"):
    #baixar como audio
    os.system(f"yt-dlp -P \"{save_path}\" -x --audio-format mp3 -o \"{nome}.%(ext)s\" {video_link}")
    

def video_downloader(video_link, tipo, resolution, como_salvar,progress=gr.Progress()):
    #verifica se url é valida
    progress.visible=True
    progress(0.1, desc="Iniciando...")
    if video_link.split("//")[0] == "https:" :

        #Verifica tipo e encaminha para download de video ou audio 
        progress(0.3, desc="Procurando video...")
        if tipo != "somente audio":

            progress(0.65, desc="Iniciando Download...")
            progress(0.8, desc="Baixando...")

            realiza_download_video(video_link, HOLYRICS_VIDEO, resolution)

            progress(0.95, desc="Abrindo pasta...")
            if como_salvar == "sim":
                os.system(f"explorer {HOLYRICS_VIDEO}")

            gr.Info("Video Baixado!")
            return "DOWNLOAD REALIZADO COM SUCESSO!!! VIDEO SALVO NA PASTA DO HOLYRICS!!"
            
        else:
            progress(0.65, desc="Iniciando Download...")

            progress(0.8, desc="Baixando...")
            realiza_download_audio(video_link, HOLYRICS_AUDIO)

            progress(0.95, desc="Abrindo pasta...")
            if como_salvar == "sim":
               os.system(f"explorer {HOLYRICS_AUDIO}") 
  
            gr.Info("Video Baixado!")
            return "DOWNLOAD REALIZADO COM SUCESSO!!! VIDEO SALVO NA PASTA DO HOLYRICS!!"
    else:
        gr.Error("URL INVALIDA!!!")

# ************************* Conversor PDF ****************************

def converte(pdf, path, file_name):
    #  # Load a document
    #  pdf = pdfium.PdfDocument(pdf)
    #  pdf.get_metadata_dict 

    #  # Loop over pages and render
    #  for i in range(len(pdf)):
    #      page = pdf[i]
    #      image = page.render(scale=4).to_pil()
    #      image.save(f"{path}\\{file_name}.jpg")

    pdffile = pdf
    doc = fitz.open(pdffile)
    page = doc.load_page(0)  # number of page
    pix = page.get_pixmap()
    output = f"{path}\\{file_name}.png"
    pix.save(output)
    doc.close()

            

def pdf_converter(file, como_salvar):
    # file name with extension
    file_name = os.path.basename(file)

    # file name without extension
    file_name = os.path.splitext(file_name)[0]

    if como_salvar != "sim":
        converte(file, TEMPORARIO, file_name)

        gr.Warning("Convertido com sucesso")
        return gr.DownloadButton(label="salvar", value=f"{TEMPORARIO}\\{file_name}.png", visible=True)
    else:
        converte(file, HOLYRICS_IMAGEM, file_name)

        gr.Warning("Convertido com sucesso")

# ************************** PAGINAS *******************************

with gr.Blocks(css="style.css", title="Canivete Holyrics V1.1.0", js=js_func) as demo:
    with gr.Tab("Download"):

        url_input = gr.Textbox(label="", placeholder="Cole a URL do video aqui", elem_classes="url")

        tipo_input = gr.Radio(label="Selecione o tipo de arquivo para baixar", choices=["video", "somente audio"], value="video")

        como_salvar_input = gr.Radio(label="Abrir pasta apos download?", choices=["sim", "não"], value="não")

        download_button = gr.Button("Baixar")

        with gr.Accordion(label="Outras Opções", open=False):
            gr.Markdown("ATENÇÃO!! A escolha de outras resoluções aumentara muito o tempo de download!!")
            resolution_input = gr.Radio(label="resolução", choices=["144", "360", "480", "720", "1080"], value="720", )

        progress_output = gr.Textbox(label="")


        download_button.click(fn=video_downloader, inputs=[url_input, tipo_input, resolution_input, como_salvar_input], outputs=[progress_output])

    with gr.Tab("Conversor PDF"):
        gr.Markdown("CONVERSOR PDF ---> JPEG")

        file_input = gr.File()

        como_salvar_input = gr.Radio(label="Salvar arquivo direto no holyrics?", choices=["sim", "não"], value="sim")

        salvar_output = gr.DownloadButton("Salvar Como", visible=False)

        converte_btn = gr.Button("CONVERTER")

        converte_btn.click(fn=pdf_converter, inputs=[file_input,como_salvar_input], outputs=salvar_output)

if __name__ == "__main__":
    os.system(f'start http://{IP_ADDR}') #abre navegador 
    demo.launch(server_name=IP_ADDR, server_port=80, quiet=True, show_api=False, favicon_path="icon.ico", allowed_paths=["."])