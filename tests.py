from jointer import main as joint
import namer
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
  page_filter = 'Copel Distribuição S.A.'
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
  namer.main(search_paths, code_rect, ref_month_rect, page_filter)

def test_namer_energisa_var1():
  code_rect = (235, 185, 325, 208)
  ref_month_rect = (45, 245, 145, 275)
  page_filter = 'ENERGISA MATO GROSSO DO SUL - DISTR. DE ENERGIA S.A.'
  search_paths = [
    r'\\172.25.0.250\Fontesul\OEM\database\cassems\faturas2'
  ]
  namer.main(search_paths, code_rect, ref_month_rect, page_filter, r'\d{2}/\d{3,10}-\d')

def test_namer_energisa_var2():
  code_rect = (355, 87, 510, 104)
  ref_month_rect = (62, 143, 121, 163)
  page_filter = 'ENERGISA MATO GROSSO DO SUL - DISTR. DE ENERGIA S.A.'
  search_paths = [
    r'\\172.25.0.250\Fontesul\OEM\database\cassems\faturas2'
  ]
  namer.main(search_paths, code_rect, ref_month_rect, page_filter, r'\d{2}/\d{3,10}-\d')

def test_namer_energisa_var3():
  code_rect = (184, 87, 268, 130)
  ref_month_rect = (35, 150, 75, 162)
  page_filter = 'ENERGISA MATO GROSSO DO SUL - DISTR. DE ENERGIA S.A.'
  search_paths = [
    r'\\172.25.0.250\Fontesul\OEM\database\cassems\faturas2'
  ]
  namer.main(search_paths, code_rect, ref_month_rect, page_filter, r'\d{2}/\d{3,10}-\d')

def test_namer_energisa_var4():
  code_rect = ()
  ref_month_rect = ()
  page_filter =  ''
  search_paths = [

  ]
  namer.main(search_paths, code_rect, ref_month_rect, page_filter, r'\d{2}/\d{3,10}-\d')

def test_namer_energisa_var5():
  ...

if __name__ == '__main__':
  setup_logger()
  test_namer_energisa_var3()