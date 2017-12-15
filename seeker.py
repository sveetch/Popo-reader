"""
A very basic script to seek for every font and texts from a PSD file

Actually, every font setted in PSD are returned, this can include default
Photoshop font families. Didn't finded how to filter for only used font type.
"""
import json

from psd_tools import PSDImage


SEEKED_TEXTS = []
SEEKED_FONTS = []


def seek_layers(layers):
    for layer in layers:
        if layer.kind == 'group':
            print("Group:", layer.name)
            seek_layers(layer.layers)
            print()
        elif layer.kind == 'type':
            print(layer.kind, ":", layer.name)
            for item in layer.fontset:
                print("-", item[b'Name'], item[b'FontType'])
                if item[b'Name'] not in SEEKED_FONTS:
                    SEEKED_FONTS.append(item[b'Name'])
            SEEKED_TEXTS.append(layer.text)



if __name__ == '__main__':
    import os
    import argparse
    import json

    description = ('Open a PSD file to search for texts and font families')

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('filepath', metavar='filepath',
                        help='an integer for the accumulator')

    args = parser.parse_args()

    if os.path.exists(args.filepath):
        print("Opening file:", args.filepath)
        psd = PSDImage.load(args.filepath)
        seek_layers(psd.layers)

        datas = {
            'FONTS': SEEKED_FONTS,
            'TEXTS': SEEKED_TEXTS,
        }
        print()
        print(json.dumps(datas, indent=4))
    else:
        print("Given path does not exists:", args.filepath)