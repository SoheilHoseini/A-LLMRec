import os

def get_project_path():
    """Get the base project path from environment variable or default"""
    return os.environ.get('PROJECT_BASE_PATH', '/content/drive/MyDrive/Rec_Proj_DL')

def get_data_path():
    """Get the data directory path"""
    return os.path.join(get_project_path(), 'data', 'amazon')

def get_pretrain_path():
    """Get the pre_train directory path"""
    return os.path.join(get_project_path(), 'pre_train')

def get_models_path():
    """Get the models directory path"""
    return os.path.join(get_project_path(), 'models')
