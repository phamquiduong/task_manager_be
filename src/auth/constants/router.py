from auth.schemas.route import RouteSchema
from auth.utils.route import get_route_path


class AuthRoutes:
    PREFIX = "/auth"

    class Path:
        REGISTER = RouteSchema(path="/register", code=1)


all_auth_router = get_route_path(route_class=AuthRoutes)
