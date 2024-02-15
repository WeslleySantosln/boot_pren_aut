#!/bin/bash

# Nome de usuário e senha do superusuário
superuser="gmateus"
senha="gm123"

echo "$senha" | sudo -S su


# Atualizar repositórios existentes
echo "$senha" | sudo -S apt update
#echo "$senha" | sudo -S apt upgrade -y



# Baixar o Google Chrome e deixar em home .
echo "$senha" | sudo -S wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -P /tmp

# Instalar o Google Chrome .
echo "$senha" | sudo -S dpkg -i /tmp/google-chrome-stable_current_amd64.deb
echo "$senha" | sudo -S apt update
echo "$senha" | sudo -S apt install -f -y




# importar a chave GPC do AnyDesk para assinar pacotes APT .
sudo curl -fsSL https://keys.anydesk.com/repos/DEB-GPG-KEY | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/anydesk.gpg

# Adicionando o conteúdo do repositório AnyDesk .
echo "deb http://deb.anydesk.com/ all main" | sudo tee /etc/apt/sources.list.d/anydesk-stable.list

# instalar o AnyDesk
echo "$senha" | sudo -S apt update
sudo apt install anydesk



# Baixar gmcore-pastaCompartilhada-WMS, app-balcao
wget -O /tmp/install http://10.172.68.76/regional/update/install && bash /tmp/install

# Baixar app-balcao .
#wget http://pdvmaxipos.mateus/appbalcao

# Dar permissão para executar o app balcão .
chmod -R 777 appbalcao





# URL da imagem do Mateus
image_url="https://mir-s3-cdn-cf.behance.net/project_modules/1400_opt_1/8cb9a9140428429.6241c6e0c2007.png"

# Nome do arquivo de destino
filename="wallpaper.jpg"

# Baixa a imagem
wget -O $filename $image_url

# Verifica se o download foi bem-sucedido
if [ $? -eq 0 ]; then
    echo "Download da imagem concluído com sucesso."

    # Define a imagem como papel de parede
    gsettings set org.gnome.desktop.background picture-uri "file://$(pwd)/$filename"

    echo "Papel de parede definido."
else
    echo "Erro ao baixar a imagem. Verifique a URL e tente novamente."
fi



# Criar atalho do Google Chrome na área de trabalho
echo "[Desktop Entry]
Version=1.0
Name=Google Chrome
GenericName=Web Browser
Comment=Access the Internet
Exec=/usr/bin/google-chrome-stable
Icon=/opt/google/chrome/product_logo_48.png
Type=Application
Categories=Network;WebBrowser;
MimeType=text/html;text/xml;application/xhtml_xml;image/webp;x-scheme-handler/http;x-scheme-handler/https;x-scheme-handler/ftp;
Actions=new-window;new-private-window;

[Desktop Action new-window]
Name=New Window
Exec=/usr/bin/google-chrome-stable

[Desktop Action new-private-window]
Name=New Incognito Window
Exec=/usr/bin/google-chrome-stable --incognito" | sudo -S tee /usr/share/applications/google-chrome.desktop > /dev/null
