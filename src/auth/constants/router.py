from auth.schemas.route import RouteSchema
from auth.utils.route import get_route_path


class AuthRoutes:
    PREFIX = "/auth"

    class Path:
        HEALTH_CHECK = RouteSchema(path="/health-check", code=1)
        REGISTER = RouteSchema(path="/register", code=2)


all_auth_router = get_route_path(route_class=AuthRoutes)
