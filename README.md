

# on local project

> folder structure

another-demo-package
├── another_package                 # ->this goes to pyproject.toml
│   ├── another_package_module.py
│   ├── class_module.py
│   ├── __init__.py
│   └── say_hello_module.py
├── another_package.egg-info
├── pyproject.toml
└── README.md


> pyproject.toml
[project]
name = "another_package"
version = "2024.0.0"

> __init__.py
from .say_hello_module import say_hello
from .class_module import ClassModule


# on the target directory
python -m pip install -e /home/miros/DataOps/developer/white/another-demo-package     

> import statements
from another_package import say_hello, say_bye, ClassModule
#OR
import another_package

# class_instance = ClassModule()
# hello = class_instance.say_hello() 
# print(hello)


> when running pip list
Package            Version     Editable project location
------------------ ----------- --------------------------------------------------------
another_package    2024.0.0    /home/miros/DataOps/developer/white/another-demo-package

> vscode settings
{
    "python.analysis.extraPaths": [
        "/home/miros/DataOps/developer/white/another-demo-package"
    ]
}