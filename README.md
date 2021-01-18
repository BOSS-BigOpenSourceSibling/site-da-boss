# Big Open Source Sister - Site

### Pré requisitos

📌 Tenha instalado o [Docker](https://docs.docker.com/get-docker/) e o [Docker Compose](https://docs.docker.com/compose/install/#install-compose)

### Rodar o site localmente
1. Clone o repositório
```Power Shell
git clone https://github.com/BOSS-BigOpenSourceSister/site-da-boss.git
```
2. Dentro do diretório do site, contrua o contêiner
```Power Shell
sudo docker-compose up --build
```
3. Acesse a porta 8000 em seu navegador
```Power Shell
http://127.0.0.1:8000/
```
A próxima vez que for rodar o site, é necessário apenas subir o contêiner
```Power Shell
sudo docker-compose up
```
