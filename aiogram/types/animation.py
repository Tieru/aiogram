from . import base
from . import fields
from . import mixins
from .photo_size import PhotoSize


class Animation(base.TelegramObject, mixins.Downloadable):
    """
    You can provide an animation for your game so that it looks stylish in chats
    (check out Lumberjack for an example).
    This object represents an animation file to be displayed in the message containing a game.

    https://core.telegram.org/bots/api#animation
    """

    file_id: base.String = fields.Field()
    thumb: PhotoSize = fields.Field(base=PhotoSize)
    file_name: base.String = fields.Field()
    mime_type: base.String = fields.Field()
    file_size: base.Integer = fields.Field()
