import json
import os
from norm_path import normalize_file_paths_from_folder
from util import setup_logger

def rename(template_name: str, variant: int):
  setup_logger()
  with open('bill_renamer_templates.json', encoding='utf-8') as templates_file:
    templates = json.load(templates_file)['templates']
  template = templates[template_name][f'variant_{variant}']
  del templates
  for folder in template['search_paths']:
    folder = os.path.normpath(folder)
    normalize_file_paths_from_folder(
      folder,
      (
        template['code_rect']['x0'],
        template['code_rect']['y0'],
        template['code_rect']['x1'],
        template['code_rect']['y1'],
      ),
      (
        template['ref_month_rect']['x0'],
        template['ref_month_rect']['y0'],
        template['ref_month_rect']['x1'],
        template['ref_month_rect']['y1'],
      ),
      template['page_filter'],
      template['code_regex'],
      template['ref_month_regex'],
      )

if __name__ == '__main__':
  rename(
    template_name='copel',
    variant=1
  )