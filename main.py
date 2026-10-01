import os
import subprocess

print('MKV to MP4 Converter')
directory = input('What is the files path? ')

# 1. Trava de segurança: verifica se o diretório digitado
# realmente existe
if not os.path.exists(directory):
    print('Error: Directory not found. Exiting...')
    exit()

# 2. Se a pasta existe, capturamos o conteúdo da pasta e
# guardamos na variável folder_files
folder_files = os.listdir(directory) 
mkv_files = []

# 3. O loop lê os arquivos da pasta e adiciona os que são .mkv
# na lista mkv_files
for file in folder_files:
    # O fatiamento de string lê os 4 últimos caracteres do nome
    # do arquivo e compara com '.mkv'
    if file[-4:] == '.mkv': 
        mkv_files.append(file)

# 4. Se o tamanho da lista mkv_files for 0, significa que não há
# arquivos .mkv na pasta
if len(mkv_files) == 0:
    print('No MKV files found...')
    # E aí o programa é encerrado
    exit()

print(f'Found {len(mkv_files)} MKV file(s)!')

# 5. Selecionamos se será com 1 ou 2 faixas de áudio usando um
# loop while True
while True:
    audio_tracks = input('MP4 with 1 or 2 audio tracks? [type 1 or 2]: ')
    if audio_tracks == '1' or audio_tracks == '2':
        print(f'Selected {audio_tracks} audio track(s).')
        break
    else:
        print('Wrong selection. Please type 1 or 2.')

# 6. Pergunta das legendas (mesma estrutura lógica)
while True:
    subtitles = input('Do you want to include subtitles? [y/n]: ').lower()
    if subtitles == 'y' or subtitles == 'n':
        print(f'Subtitles option: {subtitles}')
        break
    else:
        print('Wrong selection. Please type y or n.')

# 7. Resumo de confirmação antes de iniciar a conversão
print('\n--- SUMMARY ---')
print(f'Folder: {directory}')
print(f'Files to convert: {len(mkv_files)}')
print(f'Audio tracks selected: {audio_tracks}')
print(f'Subtitles selected: {subtitles}')
print('----------------')

confirm = input('Do you want to proceed with the conversion? [y/n]: ').lower()

if confirm != 'y':
    print('Operation canceled by user. Exiting...')
    exit()

# 8. Início da conversão chamando o FFmpeg no terminal via subprocess 
print('\nStarting conversion...\n')

# Mapeamento do áudio com base na variável audio_tracks
if audio_tracks == '1':
    audio_map = ['-map', '0:a:0']
else:
    audio_map = ['-map', '0:a:0', '-map', '0:a:1']

# Mapeamento das legendas com base na variável subtitles
if subtitles == 'y':
    subtitle_map = ['-map', '0:s:0?', '-c:s', 'mov_text']
else:
    subtitle_map = ['-sn']

# Loop para converter arquivo por arquivo mantendo a sua variável file
for file in mkv_files:
    input_path = os.path.join(directory, file)
    output_file = file[:-4] + '.mp4'
    output_path = os.path.join(directory, output_file)

    print(f'Converting: {file} -> {output_file}')

    # Monta a lista de comando para o subprocess do Python chamar o FFmpeg[cite: 3]
    command = ['ffmpeg', '-i', input_path, '-map', '0:v'] + audio_map + subtitle_map + ['-c:v', 'copy', '-c:a', 'copy', output_path]

    # Executa o FFmpeg e exibe a barra de progresso no terminal do Linux[cite: 3, 5]
    subprocess.run(command)

print('\nTask finished successfully! All files converted.')