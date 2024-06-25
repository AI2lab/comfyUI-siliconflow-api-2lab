

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
