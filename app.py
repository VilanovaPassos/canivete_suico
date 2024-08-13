import gradio as gr
import fitz #PDF
import os
import subprocess
import socket
#import tempfile
import segno #QRCODE
import sys
import shutil


#definicoes caminhos
HOLYRICS_VIDEO = "C:\\Holyrics\\Holyrics\\files\\media\\video" 
HOLYRICS_AUDIO = "C:\\Holyrics\\Holyrics\\files\\media\\audio"
HOLYRICS_IMAGEM = "C:\\Holyrics\\Holyrics\\files\\media\\image"
#TEMPORARIO = tempfile.gettempdir()

#Pega indereço IP
IP_ADDR = socket.gethostbyname(socket.gethostname())

#css interno
css = """
.url textarea {
    background-color: red !important;
    padding-left: 45px !important;
    background: url("/file=VideoDownload.png") no-repeat left !important;
    background-size: 40px !important;
  }

#qrcode {
      display: block;
      margin-left: auto;
      margin-right: auto;
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

# ************************ Youtube Downloader ************************

def realiza_download_video(video_link, save_path, resolucao, nome="%(title)s"):
    #baixar video
    os.system(f"yt-dlp -P \"{save_path}\" -S \"res:{resolucao},vcodec:264,acodec:m4a\" --yes-playlist -o \"{nome}.%(ext)s\" {video_link} >> output.log") 

def realiza_download_audio(video_link, save_path, nome="%(title)s"):
    #baixar como audio
    os.system(f"yt-dlp -P \"{save_path}\" -x --audio-format mp3 --yes-playlist -o \"{nome}.%(ext)s\" {video_link} >> output.log")
    

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
                os.system("schtasks /Run /TN abre_video") #abre pasta de video

            gr.Info("Video Baixado!")
            return "Download realizado com sucesso!!! VIDEO SALVO NA PASTA DO HOLYRICS!!"
            
        else:
            progress(0.65, desc="Iniciando Download...")

            progress(0.8, desc="Baixando...")
            realiza_download_audio(video_link, HOLYRICS_AUDIO)

            progress(0.95, desc="Abrindo pasta...")
            if como_salvar == "sim":
               os.system("schtasks /Run /TN abre_audio") #abre pasta de audio 
  
            gr.Info("Audio Baixado!")
            return "Download realizado com sucesso!!! AUDIO SALVO NA PASTA DO HOLYRICS!!"
    else:
        gr.Error("URL INVALIDA!!!")

# ************************* Conversor PDF ****************************

def converte_pdf(pdf, path, file_name):
   #cria pasta para salvar o pdf com nome do arquivo
    pasta = file_name
  
    # Parent Directory path 
    parent_dir = path
  
    # Path 
    path = os.path.join(parent_dir, pasta) 
  
    # Create the directory  
    os.mkdir(path) 

    #converte pdf
    pdffile = pdf

    doc = fitz.open(pdffile)
    
    for i in range(doc.page_count):
        page = doc.load_page(i)  # number of page
        os.system("echo convertendo pagina {i} >> output.log") #log
        pix = page.get_pixmap()
        output = f"{path}\\{file_name}{i}.png"
        pix.save(output)

    doc.close()

            

def pdf_converter(file, como_salvar):
    # file name with extension
    file_name = os.path.basename(file)

    # file name without extension
    file_name = os.path.splitext(file_name)[0]

    os.system("echo iniciando conversao PDF!! >> output.log") #log

    if como_salvar == "sim":
        converte_pdf(file, HOLYRICS_IMAGEM, file_name)

        gr.Info("Convertido com sucesso")
        os.system("schtasks /Run /TN abre_imagem") #abre pasta de imagens    
    else:
        converte_pdf(file, HOLYRICS_IMAGEM, file_name)

        gr.Info("Convertido com sucesso")

    os.system("echo PDF convertido!! >> output.log") #log

# ******************* CONVERSOR VIDEO PARA MP3 ********************
def converte_mp3(file, path, file_name):
    os.system(f"ffmpeg -i \"{file}\" \"{path}\\{file_name}.mp3\" 2> output.log")

def mp3_converter(file, como_salvar):
    # file name with extension
    file_name = os.path.basename(file)

    # file name without extension
    file_name = os.path.splitext(file_name)[0]

    if como_salvar == "sim":
        converte_mp3(file, HOLYRICS_AUDIO, file_name)

        gr.Info("Convertido com sucesso")
        os.system("schtasks /Run /TN abre_audio") #abre pasta de audio
    else:
        converte_mp3(file, HOLYRICS_AUDIO, file_name)

        gr.Info("Convertido com sucesso")


# *************************** QR CODE ******************************
def qr_code():
    qrcode = segno.make_qr(f"http://{socket.gethostbyname(socket.gethostname())}")
    qrcode.save("ip_qr_code.png", scale=10)

    return "."

def refresh():
    image = os.path.join(qr_code(), "ip_qr_code.png")
    return image

# *************************** LOG *********************************
def read_logs():
    sys.stdout.flush()
    with open(os.path.join(".", "output.log"), "r") as f:
        return f.read()

# ************************ ENVIAR ARQUIVOS *************************
def enviar_arquivo(file):
     # pega nome do arquivo com extencao
    file_name = os.path.basename(file)

    # pega extencao arquivo
    extension = os.path.splitext(file_name)[1]
    print(extension)

    if(extension == ".mp3"):
        #envia para pasta de audios
        shutil.move(file, HOLYRICS_AUDIO)
        gr.Info("enviado para Audios!!")
        os.system(f"echo {file_name} enviado para Audios!! >> output.log")
    elif(extension == ".mp4"):
        shutil.move(file, HOLYRICS_VIDEO)
        gr.Info("enviado para Videos!!")
        os.system(f"echo {file_name} enviado para Videos!! >> output.log")
    elif(extension == ".png" or extension == ".jpeg" or extension == ".jpg"):
        shutil.move(file, HOLYRICS_IMAGEM)
        gr.Info("enviado para Imagens!!")
        os.system(f"echo {file_name} enviado para Imagens!! >> output.log")
    else:
        gr.Info("Arquivo NÂO Suportado!!!")
        os.system(f"echo Erro ao enviar arquivo {file_name} >> output.log")

# ************************** PAGINAS *******************************

with gr.Blocks(css=css, title="Canivete Holyrics V1.4.1", js=js_func) as demo:
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
        #gr.Markdown("<img style=\"float: left;\" src=\"file/PDF2JPG.png\" height=\"40\" width=\"40\">  CONVERSOR PDF ---> JPEG")
        gr.Markdown("CONVERSOR PDF ---> JPEG")

        file_input = gr.File()

        como_salvar_input = gr.Radio(label="Abrir pasta apos conversão?", choices=["sim", "não"], value="não")

        converte_btn = gr.Button("CONVERTER")

        converte_btn.click(fn=pdf_converter, inputs=[file_input,como_salvar_input])

    with gr.Tab("Conversor MP3"):
        gr.Markdown("CONVERSOR VIDEO ---> MP3")

        file_input = gr.File()

        como_salvar_input = gr.Radio(label="Abrir pasta apos conversão?", choices=["sim", "não"], value="não")

        converte_btn = gr.Button("CONVERTER")

        converte_btn.click(fn=mp3_converter, inputs=[file_input,como_salvar_input])
    
    with gr.Tab("Enviar arquivo"):
        gr.Markdown("CONVERSOR VIDEO ---> MP3")

        file_input = gr.File()

        envia_btn = gr.Button("Enviar")

        envia_btn.click(fn=enviar_arquivo, inputs=[file_input])

    with gr.Accordion("Acesse pelo celular usando QR CODE clicando AQUI.  OBS: precisa estar conectado no mesmo WI-FI", open=False):
        image = gr.Image(show_label=False, width=250, height=250, elem_id="qrcode") #QR CODE
        demo.load(fn=refresh, inputs=None, outputs=image, show_progress=False, every=10) 

    with gr.Accordion("LOGS", open=False):
        logs = gr.Textbox(autoscroll=True)
        demo.load(read_logs, None, logs, every=1) 

if __name__ == "__main__":
    os.system("schtasks /Run /TN abre_navegador") #abre navegador 

    os.system("echo %date% -- %time% servidor iniciado >> output.log") #inicia log com timestamp

    demo.launch(server_name="0.0.0.0", server_port=80, quiet=True, show_api=False, favicon_path="icon.ico", allowed_paths=["."])