#!/usr/bin/python3.7

"""
    Folder structure:
    [id]-clase
        -> Clase[id].hs
        -> EjerciciosClase[id].hs
        -> Notes
"""

import os

def create_class_folder(class_id):
    os.mkdir(f"./{class_id}-clase")
    # TODO: Validate if folder created
    return os.path.abspath(f"./{class_id}-clase")

def create_file(filename, class_path, class_id, extension=""):
    file_name = f"{filename}{class_id}{extension}"
    file_path = os.path.join(class_path, file_name)
    open(file_path, 'a').close()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Class creator tool')
    # TODO: Automatically detect the last class id (mmmmmmmmmmmm)
    parser.add_argument('-i', '--id', help='Class id (e.g. 03, Aux, 101)', required=True)
    args = parser.parse_args()
    
    class_folder_path = create_class_folder(class_id=args.id)
    
    create_file(extension=".hs", filename="Clase", class_path=class_folder_path, class_id=args.id)
    
    create_file(extension=".hs",filename="EjerciciosClase", class_path=class_folder_path, class_id=args.id)

    create_file(filename="Notes", class_path=class_folder_path, class_id=args.id)

        
