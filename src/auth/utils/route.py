from auth.schemas.route import RouteSchema


def get_route_path(route_class):
    return {
        f"{route_class.PREFIX}{route.path}": route.code
        for route in vars(route_class.Path).values()
        if isinstance(route, RouteSchema)
    }
