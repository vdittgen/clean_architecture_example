import redislite


class RedisLite:
    def __init__(self, app=None, **kwargs):
        self.server = None
        if app is not None:
            self.init_app(app, **kwargs)

    def init_app(self, app, **kwargs):
        self.server = redislite.Redis(serverconfig=kwargs)

        @app.teardown_appcontext
        def shutdown_redis_server(exception=None):
            self.server.redis_stop()
