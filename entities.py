from dataclasses import dataclass

@dataclass
class Word:
  """
  Objeto que guarda uma palavra do arquivo pdf, e suas coordenadas.
  """
  
  x0: float
  y0: float
  x1: float
  y1: float
  text: str
  block_num: int
  line_num: int
  word_num: int