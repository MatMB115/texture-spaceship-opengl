<p align="center">
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/count/MatMB115/texture-spaceship-opengl?color=a015f5">

  <img alt="Repository size" src="https://img.shields.io/github/repo-size/MatMB115/texture-spaceship-opengl">

  <a href="https://github.com/MatMB115/texture-spaceship-opengl/releases/tag/texture-spaceship-opengl">
    <img alt="Application Status" src="https://img.shields.io/badge/app status-running-6bd630">
  </a>

  <a href="https://github.com/MatMB115/repime_web/commits/main">
    <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/MatMB115/texture-spaceship-opengl">
  </a>

<img alt="License" src="https://img.shields.io/badge/license-GPLv3-blue">
  <a href="https://github.com/MatMB115/texture-spaceship-opengl/stargazers">
    <img alt="Stargazers" src="https://img.shields.io/github/stars/MatMB115/texture-spaceship-opengl?style=social">
  </a>
</p>

<p align="center">
  <a href="https://github.com/MatMB115/texture-spaceship-opengl">
    <img src="https://imgur.com/MnrwuJn.gif" height="260" width="600" alt="space" />
  </a>
</p>

<p align="center">
    <a href="https://www.python.org/">
        <img alt="NextJs" height="60" width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg">
    </a>
    <b>+</b>
    <a href="https://opengl.org/">
        <img alt="opengl" height="60" width="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/opengl/opengl-plain.svg">
    </a>
</p>

# texture-spaceship-opengl

## Nave com OpenGl

Explorando o uso de texturas no OpenGL com Python.

---
### Sobre :information_source:
**PREENCHER** Descrição do trabalho

As orientações estão divididas nos seguintes tópicos:

- [texture-spaceship-opengl](#texture-spaceship-opengl)
  - [Nave com OpenGl](#nave-com-opengl)
    - [Sobre :information\_source:](#sobre-information_source)
    - [Funcionalidades :gear:](#funcionalidades-gear)
    - [Etapas](#etapas)
      - [Construção da View Nave - Polígono](#construção-da-view-nave---polígono)
      - [Textura da Nave](#textura-da-nave)
      - [Construção da View Chão - Plano 2D](#construção-da-view-chão---plano-2d)
      - [Textura do chão](#textura-do-chão)
      - [Controles da Nave](#controles-da-nave)
      - [Animação do chão](#animação-do-chão)
    - [Configuração de ambiente](#configuração-de-ambiente)
    - [Tecnologias :technologist:](#tecnologias-technologist)
      - [Aplicação](#aplicação)
      - [Utilitários](#utilitários)
    - [Contribuidores](#contribuidores)

---
### Funcionalidades :gear:

 - [x] Mover nave nos eixos (X,Y);
 - [x] Rotaciona a nave nos eixos (X,Y);
 - [x] Rotaciona nave no eixo Z;
 - [x] Move câmera cima/baixo;
 - [X] Move câmera esquerda/direita;
 - [x] Move câmera frente/trás;
 - [X] Aumenta/diminui escala da nave;

---
### Etapas
**PREENCHER** Processos para construção do cenário
#### Construção da View Nave - Polígono
**PREENCHER** Explicar a matriz do polígono da nave (é uma pirâmide de base triangular e as asas são dois triângulos planos)
#### Textura da Nave
**PREENCHER** Explicar como textura é aplicada
#### Construção da View Chão - Plano 2D
**PREENCHER** Explicar que chão é uma matriz do plano 2D
#### Textura do chão
**PREENCHER** Explicar que a textura do chão
#### Controles da Nave
**PREENCHER** Só incrementa, subtrai e multiplica valores
#### Animação do chão
**PREENCHER** Explicar que a textura do chão é alterada conforme diferença de tempo

### Configuração de ambiente
``` bash
# Clone o repo
git clone https://github.com/MatMB115/texture-spaceship-opengl.git

# Acessar path
cd texture-spaceship-opengl

# Crie o env python
python -m venv nave_env

# Ativar o enviroment
source nave_env/bin/activate

# Instale as depedências
pip install -r requirements.txt

# Executar o projeto
python main.py

# Desativar o env
deactivate
```

---
### Tecnologias :technologist:
    O ponto de início deste projeto é um enviroment python, as dependências utilizadas estão presentes no requirements.txt. 

---
#### Aplicação

> glfw==2.7.0

> numpy==1.26.4

> pillow==10.3.0

> PyOpenGL==3.1.7
---

#### Utilitários
> Visual Studio Code 1.89.1

---  

### Contribuidores

<table>
  <tr>
    <td align="center"><a href="https://github.com/bjmvercelli"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/61213222?v=4" width="100px;" alt=""/><br /><sub><b>Bruno Vercelli</b></sub></a><br /><a href="https://github.com/bjmvercelli" title="RepiMe">:technologist:</a></td>
    <td align="center"><a href="https://github.com/GabrielCiriaco"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/90142790?v=4" width="100px;" alt=""/><br /><sub><b>Gabriel Ciriaco</b></sub></a><br /><a href="https://github.com/GabrielCiriaco" title="RepiMe">:technologist:</a></td>
    <td align="center"><a href="https://github.com/Lfseibel"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/43753872?v=4" width="100px;" alt=""/><br /><sub><b>Luiz Fernando</b></sub></a><br /><a href="https://github.com/Lfseibel" title="RepiMe">:technologist:</a></td>
    <td align="center"><a href="https://github.com/MatMB115"><img style="border-radius: 50%;" src="https://avatars.githubusercontent.com/u/63670910?v=4" width="100px;" alt=""/><br /><sub><b>Matheus Martins</b></sub></a><br /><a href="https://github.com/MatMB115" title="RepiMe">:technologist:</a></td>
  </tr>
</table>
