from jointer import main as joint
from namer import main as name
from util import setup_logger

def test_jointer_copel():
  search_paths = [
    r'\\172.25.0.250\Fontesul\OEM\database\saoSebastiao\faturas',
    r'\\172.25.0.250\Fontesul\OEM\database\pauFurado\faturas',
  ]
  # Gedisa
  code_rect = (76, 70, 200, 81)
  ref_month_rect = (95, 250, 170, 267)
  joint(search_paths, code_rect, ref_month_rect)

def test_namer_copel():
  # Copel
  code_rect = (226, 138, 317, 155)
  ref_month_rect = (0, 212, 90, 231)
  page_filter = "Copel Distribuição S.A."
  
  search_paths = [
    #r'\\172.25.0.250\Fontesul\OEM\database\pachalki\faturas',
    #r'\\172.25.0.250\Fontesul\OEM\database\janines\faturas',
    r'\\172.25.0.250\Fontesul\OEM\database\saoSebastiao\faturas',
    #r'\\172.25.0.250\Fontesul\OEM\database\aurora\faturas',
    #r'\\172.25.0.250\Fontesul\OEM\database\tocantins\faturas',
    #r'\\172.25.0.250\Fontesul\OEM\database\tioMucufa\faturas',
    #r'\\172.25.0.250\Fontesul\OEM\database\kossatz\faturas',
    #r'\\172.25.0.250\Fontesul\OEM\database\pauFurado\faturas',
  ]
  name(search_paths, code_rect, ref_month_rect, page_filter)

def test_namer_energisa():
  code_rect = (235, 185, 325, 208)
  ref_month_rect = (45, 245, 145, 275)
  page_filter = "ENERGISA MATO GROSSO DO SUL - DISTR. DE ENERGIA S.A."
  search_paths = [
      r'\\172.25.0.250\Fontesul\OEM\database\cassems\faturas_teste'
  ]
  name(search_paths, code_rect, ref_month_rect, page_filter)

if __name__ == '__main__':
  setup_logger()
  test_namer_energisa()