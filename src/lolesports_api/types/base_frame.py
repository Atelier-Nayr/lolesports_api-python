# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BaseFrame"]


class BaseFrame(BaseModel):
    rfc460_timestamp: datetime = FieldInfo(alias="rfc460Timestamp")
