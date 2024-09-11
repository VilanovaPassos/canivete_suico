# *********************** BIBLIOTECAS *****************************
import gradio as gr
import fitz #PDF
import os #executar comandos no sistema
#import subprocess
import socket # pegar IP maquina
#import tempfile
import segno #QRCODE
import sys
import shutil #mover arquivo


# definicoes caminhos
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

    doc = fitz.open(pdffile) #abre arquivo
    
    for i in range(doc.page_count):
        page = doc.load_page(i)  # number of page
        os.system(f"echo convertendo pagina {i} >> output.log") #log
        pix = page.get_pixmap()
        output = f"{path}\\{file_name}{i}.png"
        pix.save(output)

    doc.close() #fecha arquivo

            

def pdf_converter(file, como_salvar):
    # recebe nome do arquivo com extensao
    file_name = os.path.basename(file)

    # recebe nome doarquivo sem extensao
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
    os.system(f"ffmpeg -i \"{file}\" \"{path}\\{file_name}.mp3\" 2> output.log") #comando para extrair audio

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

# *************************** GERAR FUNDO ******************************
def gerador(video, audio, path, file_name, inicio="", fim="", imagem="false"):
    if imagem:
        # comando para imagem
        os.system(f"ffmpeg -i \"{video}\" -i \"{audio}\" -map 0:v -map 1:a -c:v copy -c:a copy {inicio}{fim}\"{path}\\{file_name}.mp4\" 2> output.log")
    else:
        #comando paa video
        os.system(f"ffmpeg -i \"{video}\" -stream_loop -1 -i \"{audio}\" -map 0:v -map 1:a -c:v copy -c:a copy -shortest {inicio}{fim}\"{path}\\{file_name}.mp4\" 2> output.log")

def gerar_fundo(video, audio, como_salvar, trim, inicio, fim):
    # file name with extension
    file_name = os.path.basename(video)

    tipo = os.path.splitext(file_name)[1] #pega extensao arquivo

    # file name without extension
    file_name = os.path.splitext(file_name)[0]

    ss, to = "", ""
    if trim == "sim":
        ss = f" -ss {inicio} "
        to = f" -to {fim} "

    #verifica se arquivo é imagem ou video
    if(tipo == ".png" or tipo == ".jpeg" or tipo == ".jpg"):
        gerador(video, audio, HOLYRICS_VIDEO, file_name, ss, to, True)
    else:
        gerador(video, audio, HOLYRICS_VIDEO, file_name, ss, to, False)


    if como_salvar == "sim":
        gr.Info("Convertido com sucesso")
        os.system("schtasks /Run /TN abre_video") #abre pasta de video
    else:
        gerador(video, audio, HOLYRICS_VIDEO, file_name, ss, to)

        gr.Info("Convertido com sucesso")

# *************************** EDITOR VIDEO ******************************
def trim_video(inicio="00:00:00", fim="99"):
    #adiciona comando para trim
    comando = f"-ss {inicio} -to {fim} "

    return comando

def altera_volume(volume=100):
    # adiciona comando para nalterar volume
    volume = volume/100

    comando = f"-af \"volume={volume}\" "

    return comando

def adiciona_fade():
    #Adiciona comando para fade
    comando = "-vf \"fade=t=in:st=0:d=3\" "

    return comando

def converte_h265():
    #adiciona comando para converter para h265
    comando = "-c:v libx265 "

    return comando

def nome_saida(arquivo):
    #cria nome de saida
    file_name = os.path.basename(arquivo)

    return file_name

def editar(video, salvar, trim, inicio, fim, vol, volume, fade, h265 ):
    comando = f"ffmpeg -y -i \"{video}\" " #comando base

    #verifica quais opcoes foram selecionadas para adicionar comando correspondente
    if trim == "sim":
        comando += trim_video(inicio, fim)
    if vol == "sim":
        comando += altera_volume(int(volume))
    if fade == "sim":
        comando += adiciona_fade()
    if h265 == "sim":
        comando += converte_h265()

    comando += f"\"{HOLYRICS_VIDEO}\\{nome_saida(video)}\"" #adiciona caminho para salvar e nome do arquivo no comando

    os.system(f"{comando} 2> output.log") #executa comando 

    if salvar == "sim":
         os.system("schtasks /Run /TN abre_video") #abre pasta de audio
    
    gr.Info("Editado com sucesso !!")

# *************************** QR CODE ******************************
def qr_code():
    qrcode = segno.make_qr(f"http://{socket.gethostbyname(socket.gethostname())}") #cria qr code com IP da maquina
    qrcode.save("ip_qr_code.png", scale=10) # salva qr code

    return "." #retorna diretorio atual 

def refresh():
    image = os.path.join(qr_code(), "ip_qr_code.png") #cria qr code novo com base no IP da maquina
    return image #retorna caminho qr code

# *************************** LOG *********************************
def read_logs():
    sys.stdout.flush() #limpa cache
    with open(os.path.join(".", "output.log"), "r") as f: #abre arquivo output.log no diretorio atual
        return f.read() #retorna a linha que foi lida

# ************************ ENVIAR ARQUIVOS *************************
def enviar_arquivo(file):
     # pega nome do arquivo com extencao
    file_name = os.path.basename(file)

    # pega extencao arquivo
    extension = os.path.splitext(file_name)[1]

    if(extension == ".mp3"):
        #envia para pasta de audios
        shutil.move(file, HOLYRICS_AUDIO) #comando para mover arquivo
        gr.Info("enviado para Audios!!")
        os.system(f"echo {file_name} enviado para Audios!! >> output.log") #log
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

with gr.Blocks(css=css, title="Canivete Holyrics V1.6.0", js=js_func) as demo:
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
        gr.Markdown("Envie arquivos para o Holyrics")

        file_input = gr.File()

        envia_btn = gr.Button("Enviar")

        envia_btn.click(fn=enviar_arquivo, inputs=[file_input])

    with gr.Tab("Gerar fundo"):
        gr.Markdown("Gerador de fundos, adicione um video e um audio")

        gr.Markdown("Video:")
        video_input = gr.File()

        gr.Markdown("Audio:")
        audio_input = gr.File()

        como_salvar_input = gr.Radio(label="Abrir pasta apos conversão?", choices=["sim", "não"], value="não")
        
        with gr.Accordion("cortar video", open=False):
            trim = gr.Radio(label="Cortar o video?", choices=["sim", "não"], value="não")

            inicio = gr.Textbox(label="Tempo inicial do corte em HH:MM:SS", placeholder="tempo inicial em HH:MM:SS", value="00:00:00")

            fim = gr.Textbox(label="Tempo final do corte em HH:MM:SS", placeholder="tempo final em HH:MM:SS")

        gerar_btn = gr.Button("GERAR")

        gerar_btn.click(fn=gerar_fundo, inputs=[video_input, audio_input, como_salvar_input, trim, inicio, fim])

    with gr.Tab("Ediçao de video"):
        gr.Markdown("Edição de video ")

        gr.Markdown("Video")
        video_input = gr.File()

        como_salvar_input = gr.Radio(label="Abrir pasta apos conversão?", choices=["sim", "não"], value="não")

        trim = gr.Radio(label="Cortar o video?", choices=["sim", "não"], value="não")

        inicio = gr.Textbox(label="Tempo inicial do corte em HH:MM:SS", placeholder="Tempo inicial em HH:MM:SS", value="00:00:00")

        fim = gr.Textbox(label="Tempo final do corte em HH:MM:SS", placeholder="Tempo final em HH:MM:SS")

        vol = gr.Radio(label="Alterar volume?", choices=["sim", "não"], value="não")

        volume = gr.Textbox(label="Digite valor do volume menor que 100 para diminuir e maior para aumentar", value=100)

        fade = gr.Radio(label="Adicionar fade?", choices=["sim", "não"], value="não")

        h265 = gr.Radio(label="Transformar em h265?", choices=["sim", "não"], value="não")

        editar_btn = gr.Button("EDITAR")

        editar_btn.click(fn=editar, inputs=[video_input, como_salvar_input, trim, inicio, fim, vol, volume, fade, h265])

    with gr.Accordion("Acesse pelo celular usando QR CODE clicando AQUI.  OBS: precisa estar conectado no mesmo WI-FI", open=False):
        image = gr.Image(show_label=False, width=250, height=250, elem_id="qrcode") #QR CODE
        demo.load(fn=refresh, inputs=None, outputs=image, show_progress=False, every=10) #faz refresh qr code a cada 10 segundos

    with gr.Accordion("LOGS", open=False):
        logs = gr.Textbox(autoscroll=True, show_label=False, lines= 15)
        demo.load(read_logs, None, logs, every=1) #le arquivo de log a cada 1 segundo

if __name__ == "__main__": #inicio programa
    os.system("schtasks /Run /TN abre_navegador") #abre navegador 

    os.system("echo %date% -- %time% servidor iniciado >> output.log") #inicia log com timestamp

    demo.launch(server_name="0.0.0.0", server_port=80, quiet=True, show_api=False, favicon_path="icon.ico", allowed_paths=["."]) #inicia servidor