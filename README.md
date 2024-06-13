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
      - [Construção da View Chão - Plano 2D (BRUNO)](#construção-da-view-chão---plano-2d-bruno)
      - [Textura do chão (BRUNO)](#textura-do-chão-bruno)
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
**PREENCHER** Processos para construção do cenário, pseudo MVC que tá sendo usado e afins
#### Construção da View Nave - Polígono
- A nave é uma matriz que forma o polígono de uma pirâmide de base triangular e as asas são dois triângulos planos;
- Para evitar a definição de várias matrizes para cada triângulo, apenas uma matriz estrutural principal é utilizada e os índices são utilizados para construir o polígono com triângulos;
- As linhas também foram adicionadas com largura maior para ressaltar as arestas;
- O processo de renderização apenas da nave é:
  - Definir a geometria;
  ```python
  def create_geometry(self):
      # Pontos no espaço
      self.vertices = [
          [0.0, 1.0, 0.0],   # Topo
          [-1.0, -1.0, 1.0], # Frente esquerda
          [1.0, -1.0, 1.0],  # Frente direita
          [1.0, -1.0, -1.0], # Traseira direita
          [-1.0, -1.0, -1.0] # Traseira esquerda
      ]
      # Ligar os pontos
      self.indices = [
          0, 1, 2,
          0, 2, 3,
          0, 3, 4,
          0, 4, 1,
          1, 2, 3,
          1, 3, 4
      ]
      # Textura
      self.tex_coords = [
          [0.5, 1.0], # Topo
          [0.0, 0.0], # Frente esquerda
          [1.0, 0.0], # Frente direita
          [1.0, 1.0], # Traseira direita
          [0.0, 1.0]  # Traseira esquerda
      ]
      # Linhas
      self.edges = [
          [0, 1], [0, 2], [0, 3], [0, 4],
          [1, 2], [2, 3], [3, 4], [4, 1]
      ]
  ```
  - Criar instância da nave;
  - Renderizar na View (pirâmide, textura e linhas).
  ``` python
  def render_spacecraft(self):
      glBindTexture(GL_TEXTURE_2D, self.spacecraft_texture_id)
      glPushMatrix()
      glTranslatef(*self.spacecraft.position)
      glRotatef(self.spacecraft.rotation[0], 1.0, 0.0, 0.0)
      glRotatef(self.spacecraft.rotation[1], 0.0, 1.0, 0.0)
      glRotatef(self.spacecraft.rotation[2], 0.0, 0.0, 1.0)
      glScalef(*self.spacecraft.scale)

      glBegin(GL_TRIANGLES)
      for i in range(0, len(self.spacecraft.indices), 3):
          for j in range(3):
              glTexCoord2f(*self.spacecraft.tex_coords[self.spacecraft.indices[i + j]])
              vertex = self.spacecraft.vertices[self.spacecraft.indices[i + j]]
              glVertex3f(*vertex)
      glEnd()

      glLineWidth(4.0)
      glColor3f(1.0, 0.0, 0.0)
      glBegin(GL_LINES)
      for edge in self.spacecraft.edges:
          for vertex in edge:
              glVertex3f(*self.spacecraft.vertices[vertex])
      glEnd()
      glColor3f(1.0, 1.0, 1.0)
      glPopMatrix()

  ```

#### Textura da Nave
- A aplicação de textura envolve o uso de coordenadas de textura (UV mapping), que mapeiam uma imagem de textura aos vértices do objeto 3D;
- Cada face do triângulo recebe a mesma textura;
- As transformações aplicadas à nave (translação, rotação e escala) são aplicadas à matriz de modelagem. Em OpenGL, essas transformações afetam todas as operações de desenho subsequentes, incluindo as coordenadas de vértice e as coordenadas de textura. 
- É feito um bind da textura com `glBindTexture(GL_TEXTURE_2D, self.spacecraft_texture_id)`, vale ressaltar que com o bind das cordenadas de textura 2D as operações de `glTranslatef`, `glRotatef` e `glScalef` também serão aplicadas para textura conforme texto supracitado.
- O processo de renderização da nave com textura é:
  - Renderização padrão da nave;
  - Bind de textura;
  - Definir as matrizes de tranformação;
  ```python
    glPushMatrix()
    glTranslatef(*self.spacecraft.position)
    glRotatef(self.spacecraft.rotation[0], 1.0, 0.0, 0.0)
    glRotatef(self.spacecraft.rotation[1], 0.0, 1.0, 0.0)
    glRotatef(self.spacecraft.rotation[2], 0.0, 0.0, 1.0)
    glScalef(*self.spacecraft.scale)

  ```
  - Renderizar com as coordenadas de textura
  ```python
    glBegin(GL_TRIANGLES)
    for i in range(0, len(self.spacecraft.indices), 3):
        for j in range(3):
            glTexCoord2f(*self.spacecraft.tex_coords[self.spacecraft.indices[i + j]])
            vertex = self.spacecraft.vertices[self.spacecraft.indices[i + j]]
            glVertex3f(*vertex)
    glEnd()

  ```
#### Construção da View Chão - Plano 2D (BRUNO)
**PREENCHER** Explicar que chão é uma matriz do plano 2D
#### Textura do chão (BRUNO)
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
