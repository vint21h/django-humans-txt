# -*- coding: utf-8 -*-

# django-humans-txt
# humans_txt/__init__.py


from typing import List  # pylint: disable=W0611


__all__ = ["default_app_config"]  # type: List[str]


default_app_config = "humans_txt.apps.DjangoHumansTxtConfig"  # type: str
