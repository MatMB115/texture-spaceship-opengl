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

O trabalho tem como objetivo fazer o uso da biblioteca pyopenGL para a criação de um sólido de nossa escolha (no nossa caso uma **nave**) para realizar as operações de translação, rotação e escalonamento

As orientações estão divididas nos seguintes tópicos:

- [texture-spaceship-opengl](#texture-spaceship-opengl)
  - [Nave com OpenGl](#nave-com-opengl)
    - [Sobre :information_source:](#sobre-information_source)
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
- [x] Move câmera esquerda/direita;
- [x] Move câmera frente/trás;
- [x] Aumenta/diminui escala da nave;

---

### Etapas

O projeto possui o arquivo -main.py que é responsável por inicializar a aplicação, em conjunto com um pseudo MVC, composto pelos arquivos view.py (responsável por renderizar os componentes, sendo eles o ambiente e a nave), controller.py (responsável por receber as teclas pressionadas do teclado e aplicar as transformações ao sólido) e por fim o model.py (onde é definido 2 classes, uma que representa a nave e outra que representa o chão)

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

  ```python
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

#### Construção da View Chão - Plano 2D

- O chão consiste uma matriz que forma um quadrado plano a partir de dois triângulos;
- O processo de renderização do chão é:

  - Definir a geometria;

  ```python
  class Ground:
      def __init__(self):
          # Vértices no espaço
          self.vertices = np.array([
              [-40.0, -8.0, -40.0],
              [40.0, -8.0, -40.0],
              [40.0, -8.0, 40.0],
              [-40.0, -8.0, 40.0]
          ], dtype=np.float32)

          # Indices dos vértices para ligar os pontos e formar os triângulos
          self.indices = np.array([
              0, 1, 2,
              2, 3, 0
          ], dtype=np.uint32)

          # Textura
          self.tex_coords = np.array([
              [0.0, 0.0],
          ])
  ```

  - Criar instância do chão;
  - Renderizar na View (plano e textura).

  ```python
  def render_ground(self):
        glBindTexture(GL_TEXTURE_2D, self.ground_texture_id)
        glPushMatrix()
        glBegin(GL_QUADS)
        for i, vertex in enumerate(self.ground.vertices):
            glTexCoord2f((i % 2) + self.ground_texture_offset, (i // 2) + self.ground_texture_offset)
            glVertex3f(*vertex)
        glEnd()
        glPopMatrix()
  ```

#### Textura do chão

- A textura do chão é formada a partir da imagem `space.png`, que é carregada e aplicada objeto
- É feito um bind da textura com `glBindTexture(GL_TEXTURE_2D, self.ground_texture_id)`
- O processo de renderização do chão com textura é:

  - Renderização padrão do chão;
  - Bind de textura;
  - Renderizar com as coordenadas de textura

  ```python
    glPushMatrix()
    glBegin(GL_QUADS)
    for i, vertex in enumerate(self.ground.vertices):
        glTexCoord2f((i % 2) + self.ground_texture_offset, (i // 2) + self.ground_texture_offset)
        glVertex3f(*vertex)
    glEnd()
    glPopMatrix()
  ```
#### Controles da Nave

O código controlller.py é responsável pela movimentação da nave. através da classe <b>Controller</b>, o método <b>process_input()</b> é responsável por fazer todas as tranformações de escala, rotação e translação do modelo.

##### Movimentação do Modelo

- **W / S / A / D**: Movimentam o modelo para cima, baixo, esquerda e direita, respectivamente, alterando suas coordenadas de transladação no plano XY.

##### Rotação do Modelo

- **Setas Direcionais (↑ / ↓ / ← / →)**: Rotacionam o modelo ao redor dos eixos X e Y. As teclas de setas para cima e para baixo controlam a rotação em torno do eixo X, enquanto as teclas para esquerda e direita controlam a rotação em torno do eixo Y.
- **Q / E**: Rotacionam o modelo ao redor do eixo Z, com a tecla Q para rotação no sentido anti-horário e a tecla E para rotação no sentido horário.

##### Movimentação da Câmera

- **I / K / J / L / U / O**: Movem a posição da câmera. As teclas I e K controlam o movimento vertical da câmera, J e L controlam o movimento horizontal, e U e O controlam o movimento na profundidade (zoom) da câmera.

##### Escala do Modelo

- **= (igual) / - (traço)**: Aumentam e diminuem a escala do modelo. A tecla = aumenta a escala em todas as direções (x, y, z), enquanto a tecla - diminui a escala, mantendo um valor mínimo de escala de 0.1 para cada eixo.

Este controlador permite uma interação dinâmica com a cena 3D, oferecendo controle sobre o modelo e a visualização através da câmera, facilitando a navegação e manipulação do ambiente virtual criado com OpenGL.

##### Código do controlller.py:
O código do controller é quem define que ações serão feitas com base na tecla que for pressionada, centralizando todas as ações,assim chamando as funções de rotação, translação ou escala no model ou alterando a posição da câmera na view.



##### No model:
As funções abaixo são definidas no model e são responsáveis pela escala, translação e rotação do modelo.
```
def translate(self, dx, dy, dz):
        self.position += np.array([dx, dy, dz], dtype=np.float32)

    def rotate(self, angle, axis):
        self.rotation += np.array(angle) * np.array(axis)

    def scale(self, sx, sy, sz):
        self.scale *= np.array([sx, sy, sz], dtype=np.float32)

```

##### Na view:
Para a movimentaçã oda câmera, a variavel camera_position é alterada.
```
class View:
    def __init__(self, spacecraft, ground, spacecraft_texture_path, ground_texture_path):
        self.spacecraft = spacecraft
        self.ground = ground
        self.spacecraft_texture_path = spacecraft_texture_path
        self.ground_texture_path = ground_texture_path
        self.camera_position = [0.0, 2.0, 25.0]
        self.camera_target = [0.0, 0.0, 0.0]
        self.camera_up = [0.0, 1.0, 0.0]
        self.spacecraft_texture_id = None
        self.ground_texture_id = None
        self.ground_texture_offset = 0.0
```
___

#### Animação do Chão

Para fazer a animação do chão, foi se utilizado uma estratégia utilizando o tempo, conforme o tempo passa a textura é renderizada em uma posição, dessa maneira dando a impressao de que o chão, no caso as estrelas, estão se movendo.

##### Função update_ground_texture_offset

A função `update_ground_texture_offset(self, delta_time)` é responsável por atualizar o deslocamento da textura do chão ao longo do tempo. Ela recebe `delta_time`, que representa o tempo decorrido desde a última atualização, e utiliza esse valor para calcular o novo deslocamento da textura:

```python
def update_ground_texture_offset(self, delta_time):
    self.ground_texture_offset += delta_time * 0.01  # velocidade animação do chão
```

A variável self.ground_texture_offset armazena a posição atual da textura do chão. Multiplicando delta_time por 0.01, a função define a velocidade da animação do chão.

##### Função render_ground

A função render_ground(self) desenha o chão na cena utilizando OpenGL. Ela vincula a textura do chão (self.ground_texture_id) e utiliza self.ground_texture_offset para aplicar o deslocamento na textura:

```
def render_ground(self):
    glBindTexture(GL_TEXTURE_2D, self.ground_texture_id)
    glPushMatrix()
    glBegin(GL_QUADS)
    for i, vertex in enumerate(self.ground.vertices):
        glTexCoord2f((i % 2) + self.ground_texture_offset, (i // 2) + self.ground_texture_offset)
        glVertex3f(*vertex)
    glEnd()
    glPopMatrix()
```
`glBindTexture(GL_TEXTURE_2D, self.ground_texture_id)`: Vincula a textura do chão para uso.

`glTexCoord2f((i % 2) + self.ground_texture_offset, (i // 2) + self.ground_texture_offset)`: Define as coordenadas de textura para cada vértice do chão, aplicando o deslocamento (self.ground_texture_offset) para criar a ilusão de movimento da textura.


##### Função render
A função render(self) é o ponto de entrada para renderizar a cena completa. Ela é chamada repetidamente para atualizar e desenhar todos os elementos na janela OpenGL:

```
def render(self):
    current_time = time.time()
    if not hasattr(self, 'last_time'):
        self.last_time = current_time
    delta_time = current_time - self.last_time
    self.last_time = current_time

    self.update_ground_texture_offset(delta_time)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(
        self.camera_position[0], self.camera_position[1], self.camera_position[2],
        self.camera_target[0], self.camera_target[1], self.camera_target[2],
        self.camera_up[0], self.camera_up[1], self.camera_up[2]
    )

    self.render_ground()
    self.render_spacecraft()
    self.render_commands()

    glfw.swap_buffers(self.window)
```

`self.update_ground_texture_offset(delta_time)`: Chama a função de atualização para mover a textura do chão com base no tempo decorrido desde o último quadro (delta_time).

`self.render_ground()`: Renderiza o chão na posição atualizada, aplicando o deslocamento da textura conforme calculado em update_ground_texture_offset.

`glfw.swap_buffers(self.window)`: Troca os buffers para exibir a cena renderizada na janela.

Essas funções trabalham juntas para criar uma animação contínua e fluida da textura do chão, proporcionando um efeito visual dinâmico à cena 3D renderizada com OpenGL.


### Configuração de ambiente

```bash
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
