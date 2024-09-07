def render_error_code(api_code: int, http_code: int, api_code_detail: int):
    return f"ERR-{api_code:03d}-{http_code:03d}-{api_code_detail:03d}"
