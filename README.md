# Formula-Bhaskara.NiCoding

Este repositório contém o código-fonte desenvolvido para o **Episódio 1** do seriado **NiCoding**, focado na resolução de equações do 2º grau utilizando a linguagem **Python** e a clássica **Fórmula de Bhaskara**.

---

## 📺 Sobre o seriado NiCoding

O **NiCoding** é uma série prática e didática de projetos em programação voltada para o aprendizado progressivo de conceitos da lógica de programação e matemática computacional. Cada episódio aborda a implementação de soluções de forma acessível e direta ao ponto, acessável via YouTube.

[https://www.youtube.com/](https://www.youtube.com/watch?v=v958owy8YQI)

## + Curiosidades

Este programa foi um dos meus primeiros desenvolvidos na minha vida como desenvolvedor, na descoberta da linguagem Python e do poder
de criação que eu tinha, a primeira coisa em que pensei foi na aceleração do processo matemático da equação do 2º grau, e assim aprendi os
primeiros conceitos de Python, desenvolvendo a fórmula de Bhaskara.

Por esse mesmo motivo, decidi que esse deveria ser o primeiro episódio do meu seriado.
---

## 📌 Sobre o Projeto (EP1)

O script em Python recebe os coeficientes $a$, $b$ e $c$ de uma equação quadrática ($ax^2 + bx + c = 0$) e realiza os seguintes cálculos:

1. **Cálculo do Delta ($\Delta$):**
   $$\Delta = b^2 - 4ac$$

2. **Cálculo das Raízes ($x_1$ e $x_2$):**
   - Verifica se existem raízes reais ($\Delta \ge 0$).
   - Aplica a fórmula de Bhaskara:
     $$x = \frac{-b \pm \sqrt{\Delta}}{2a}$$

3. **Análise Gráfica da Parábola:**
   - **Vértice da Parábola:** Cálculo dos pontos $(X_v, Y_v)$:
     $$X_v = \frac{-b}{2a}, \quad Y_v = \frac{-\Delta}{4a}$$
   - **Intercepto $Y$:** Ponto de intersecção no eixo vertical $(0, c)$.
   - **Concavidade:** Determina se a parábola é voltada para cima ($a > 0$) ou para baixo ($a < 0$).

---

## 🚀 Como Executar

1. Certifique-se de ter o **Python 3** instalado em sua máquina.
2. Clone este repositório ou baixe o arquivo `formula-bhaskara.py`.
3. Execute o script no terminal:

```bash
python formula-bhaskara.py
