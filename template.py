# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 23:51:19 2022

@author: syed_
"""

import os


dirs = [
       os.path.join("data","raw"),
        os.path.join("data","processed"),
        "notebooks",
        "save_models",
        "src"
        
        ]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok= True)
    print(dir_)
    
    with open(os.path.join(dir_,".gitkeep"),"w") as f:
        pass  
        
    

file_ = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")

    ]


for files in file_:
    with open(files, "w") as f:
        pass
    

    
    
