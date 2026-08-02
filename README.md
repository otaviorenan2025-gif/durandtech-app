# DurandTech Systen - App Android

## Como gerar APK sem instalar Linux (GitHub Actions - 5 min)

1. Crie um repositório novo no GitHub chamado durandtech-app
2. Arraste TODOS os arquivos desta pasta pra lá
3. Vá em Actions > vai ver "Build APK" rodando
4. Quando terminar (10-15min), baixe o APK em Artifacts

## Como gerar no Linux local (se quiser dual boot / VM)

1. sudo apt install python3-pip openjdk-17-jdk unzip -y
2. pip3 install buildozer --break-system-packages
3. buildozer android debug
4. APK em bin/

URL do app: https://www.durandtechsysten.com.br
Icone: icon.png (copie seu logo DTS pra cá se quiser trocar)
