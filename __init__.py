import os
import shutil

from .constants import project_root

config_file_path = os.path.join(project_root, "config.json")
if not os.path.exists(config_file_path):
    config_template_file_path = os.path.join(project_root, "config_template.json")
    shutil.copy(config_template_file_path, config_file_path)

from .siliconflow import FreeChat,PaidChat
# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    FreeChat.NAME: FreeChat,
    PaidChat.NAME: PaidChat,
}

# display name
NODE_DISPLAY_NAME_MAPPINGS = {
    PaidChat.NAME: "Siliconflow paid chat",
    FreeChat.NAME: "Siliconflow free chat",
}

__all__ = [NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS]
