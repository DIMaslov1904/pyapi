from src.users.routes import router as users_router


def setup_routes(app):
    app.include_router(users_router)