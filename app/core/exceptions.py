from fastapi import FASTAPI, Request
from fastapi.responses import JSOnResponse


def register_exception_handlers(app: FASTAPI):
  @app.add_exception_handler(Exception)
  async def unhandled_exception_handler(request: Request, exc: Exception):
    return JSOnResponse(status_code = 500, content ={'detail': str(exc)})