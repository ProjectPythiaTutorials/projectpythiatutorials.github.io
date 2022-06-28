import yaml
from gallery_generator import build_from_items, generate_menu


def main(app):

    with open('tutorial_gallery.yaml') as fid:
        all_items = yaml.safe_load(fid)

    title = 'Tutorials Gallery'
    subtext = 'Pythia Tutorials provide content for virtual tutorials.'
    menu_html = generate_menu(all_items)
    build_from_items(all_items, 'index', title=title, subtext=subtext, menu_html=menu_html)


def setup(app):
    app.connect('builder-inited', main)
