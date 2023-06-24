from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import Paragraph
from datetime import datetime
import textwrap
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Registro das fonte #
pdfmetrics.registerFont(TTFont('DMSans-Regular', 'C:/Users/Usuario/DEV2022/SISTEMA PARA CERTIFICADO ESTETICA/PyCharm/fontes/DMSans-Regular.ttf'))
pdfmetrics.registerFont(TTFont('PinyonScript-Regularr', 'C:/Users/Usuario/DEV2022/SISTEMA PARA CERTIFICADO ESTETICA/PyCharm/fontes/PinyonScript-Regular.ttf'))

# Registre a fonte "Overpass"
font_path = "C:/Users/Usuario/DEV2022/SISTEMA PARA CERTIFICADO ESTETICA/PyCharm/fontes/"

# Registrar a fonte para o nome do curso
pdfmetrics.registerFont(TTFont('FonteCurso', f"{font_path}DMSans-Regular.ttf"))

# Registrar a fonte para o nome do aluno
pdfmetrics.registerFont(TTFont('FonteAluno', f"{font_path}PinyonScript-Regular.ttf"))

# Registrar a fonte para o nome do aluno 2
pdfmetrics.registerFont(TTFont('FonteAluno2', f"{font_path}PinyonScript-Regular.ttf"))

# Carregar imagem do certificado
certificado_path = 'novocertificado.png'

# Configurações do PDF
pdf_title = 'Certificado de Conclusão de Curso Mentoria-Ticiane'

# Coletar informações do formulário
nome_aluno = input("Digite o nome do aluno: ")

# Permitir a entrada de texto multilinhas
print("Digite o nome do curso (pressione Enter duas vezes para finalizar):")
nome_curso_lines = []
while True:
    line = input()
    if line == "":
        break
    nome_curso_lines.append(line)
nome_curso = "\n".join(nome_curso_lines)

# Gerar PDF
agora = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
pdf_name = f'Certificado_{nome_aluno}_{agora}.pdf'
c = canvas.Canvas(pdf_name, pagesize=letter)
c.setTitle(pdf_title)

# Adicionar imagem
c.drawImage(ImageReader(certificado_path), 0, 0, width=8.5*inch, height=11*inch, preserveAspectRatio=True)

# Configurar o posicionamento do texto
c.setFillColor(colors.black)  # Definir a cor do texto para preto

# Definir o estilo para o nome do curso
style_curso = ParagraphStyle(name='Left', fontName='FonteCurso', fontSize=10, leading=10, alignment=TA_LEFT)

# Quebrar o texto em linhas
lines = nome_curso.splitlines()

# Desenhar as linhas do nome do curso
y = 6.0 * inch  # Aumente ou diminua este valor para mover o texto verticalmente
left_margin = 3.7 * inch  # Ajuste este valor para mover o texto horizontalmente
for line in lines:
    p = Paragraph(line, style_curso)
    w, h = p.wrap(11.2 * inch, 0)
    x = left_margin
    p.drawOn(c, x, y - h)
    y -= h + 0.1 * inch

# Definir o estilo para o nome do aluno
style_aluno = ParagraphStyle(name='Center', fontName='FonteAluno', fontSize=38, alignment=TA_CENTER)

# Criar um parágrafo com o nome do aluno e o estilo personalizado
nome_aluno_paragrafo = Paragraph(nome_aluno, style_aluno)

# Calcular a largura e a altura do parágrafo
available_width = 8.5 * inch  # Aumentar a largura disponível na página
width, height = nome_aluno_paragrafo.wrap(available_width, 0)

# Ajuste as coordenadas X e Y para deslocar o nome do aluno
x_position = (11.5 * inch - width) / 2  # Centralizar o nome do aluno
#y_position = 6.8 * inch
y_position = (6.8 - 0.2) * inch
#y_position = 6.8 * inch  # Definição inicial da posição vertical
#y_position = 0.5 * y_position  # Baixa o nome do aluno pela metade


# Desenhar o parágrafo alinhado à direita com as novas coordenadas
nome_aluno_paragrafo.drawOn(c, x_position, y_position)

# Definir o estilo para o segundo nome do aluno
style_aluno2 = ParagraphStyle(name='Center2', fontName='DMSans-Regular', fontSize=9, alignment=TA_LEFT)

# Criar um parágrafo com o nome do aluno e o segundo estilo personalizado
nome_aluno_paragrafo2 = Paragraph(nome_aluno, style_aluno2)

# Calcular a largura e a altura do segundo parágrafo
available_width2 = 8.5 * inch
width2, height2 = nome_aluno_paragrafo2.wrap(available_width2, 0)

# Ajuste as coordenadas X e Y para deslocar o segundo nome do aluno
x_position2 = 6.3 * inch
y_position2 = 3.0 * inch

# Desenhar o segundo parágrafo alinhado à esquerda com as novas coordenadas
nome_aluno_paragrafo2.drawOn(c, x_position2, y_position2)

# Salvar PDF
c.save()
print(f'Certificado salvo em "{pdf_name}"')
