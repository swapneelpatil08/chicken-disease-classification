import os
from box.config_box import ConfigBox
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from pathlib import Path
from typing import Any
import base64 


@ensure_annotations
def read_yaml(filepath: Path) -> ConfigBox:
    """
    Read a YAML file and return a ConfigBox object.
    
    Parameters
    ----------
    filepath : Path
        Path to the YAML file.

    Returns
    -------
    ConfigBox
        ConfigBox object.
    """
    try:
        with open(filepath, "r") as f:
            content = yaml.safe_load(f)
            logger.info(f"Successfully read {filepath} as {type(content)}")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"BoxValueError: Failed to read {filepath}: {e}")
        raise e
    except Exception as e:
        logger.error(f"Exception: Failed to read {filepath}: {e}")
        raise e

@ensure_annotations
def create_directories(path_to_directory: list, verbose: bool = False):
    """
    Create a list of directories.
    
    Parameters
    ----------
    path_to_directory : list
        List of directories to create.
    verbose : bool, optional
        If True, print the directories that are created. The default is False.

    Returns
    -------
    list
        List of directories that were created.
    """
    directories = []
    for directory in path_to_directory:
        if not os.path.exists(directory):
            os.makedirs(directory)
            directories.append(directory)
            if verbose:
                logger.info(f"Successfully created directory {directory}")
        else:
            if verbose:
                logger.info(f"Directory {directory} already exists")
    return directories



@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save a dictionary to a JSON file.
    
    Parameters
    ----------
    path : Path
        Path to the JSON file.
    data : dict
        Dictionary to save.
    """
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
    logger.info(f"Json file successfully saved: {path}")
    
    
@ensure_annotations
def load_json(path: Path):
    """
    Load a JSON file.
    
    Parameters
    ----------
    path : Path
        Path to the JSON file.

    Returns
    -------
    dict
        Dictionary loaded from the JSON file.
    """
    with open(path, "r") as f:
        content = json.load(f)
        
    logger.info(f"Json file successfully loaded: {path}")
    return ConfigBox(content)        
    


@ensure_annotations
def save_bin(path: Path, data: Any):
    """
    Save a dictionary to a binary file.
    
    Parameters
    ----------
    path : Path
        Path to the binary file.
    data : Any
        Dictionary to save.
    """
    joblib.dump(value= data, filename = path)
    logger.info(f"Bin file successfully saved: {path}")

    
@ensure_annotations
def load_bin(path: Path) -> ConfigBox:
    """
    Load a binary file.
    
    Parameters
    ----------
    path : Path
        Path to the binary file.

    Returns
    -------
    ConfigBox
        ConfigBox object.
    """
    with open(path, "rb") as f:
        content = joblib.load(f)
        
    logger.info(f"Bin file successfully loaded: {path}")
    return ConfigBox(content)

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file.
    
    Parameters
    ----------
    path : Path
        Path to the file.

    Returns
    -------
    str
        Size of the file.
    """
    size = os.path.getsize(path)
    if size < 1024:
        return f"{size} bytes"
    elif size < 1024 ** 2:
        return f"{size / 1024:.2f} KB"
    elif size < 1024 ** 3:
        return f"{size / 1024 ** 2:.2f} MB"
    elif size < 1024 ** 4:
        return f"{size / 1024 ** 3:.2f} GB"
    else:
        return f"{size / 1024 ** 4:.2f} TB"
    
    
def decodeImage(imageString: str, fileName):
    imgData = base64.b64decode(imageString)
    with open(f"{fileName}.png", "wb") as f:
        f.write(imgData)
        f.close()
        
        
def encodeImageIntoBase64(imgPath: Path):
    with open(imgPath, "rb") as f:
        imgData = f.read()
    return base64.b64encode(imgData).decode("utf-8")