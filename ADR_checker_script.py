from abc import ABC
import os

# import cchardet # speeds up encoding detection
# import re # regular expressions
# from difflib import SequenceMatcher
# from bs4 import BeautifulSoup

# crawl the dataset and get a list of all filenames relative to the "dataset" folder as root
def fcrawl(current_working_dir, fullpath:bool = False):
    # found files
    foundF = []
    # Iterate over files in "dataset" directory
    for dirpath, dirnames, filenames in os.walk(current_working_dir):
        # add the path to allFiles
        for filen in filenames:
            currentFile = filen
            if (fullpath):
                currentFile = os.path.relpath(os.path.join(dirpath, filen), current_working_dir)      
            foundF.append(currentFile)

    return foundF

""" Interface for ADR checks """
# All checks that inherit from this must
# implement a "result" method which performs the check
class ADR_Check(ABC):
    def __init__(self, project_root:str) -> None:
        if not os.path.exists(project_root):
            raise Exception
        self.root = project_root
        pass
    
    def result(self) -> bool:
        return False

class File_Existence_Check(ADR_Check):
    def __init__(self,  project_root:str, filename:str, filetype:str, parentdir:str="") -> None:
        self.filename = filename
        self.filetype = filetype
        self.parentdir = project_root
        if parentdir != "":
            self.parentdir = parentdir
        super().__init__(project_root)

    def result(self) -> bool:
        considered_files = fcrawl(self.parentdir)
        return self.filename + "." + self.filetype in considered_files

# file directory primitives; current working directory
cwd_root = os.getcwd()

# example file existence check, place in cloned_366 folder!
# checks if package.json exists
test = File_Existence_Check(cwd_root, "package", "json")
print(f"Checking for Node.js\nRESULT: {test.result()}")




    
    
