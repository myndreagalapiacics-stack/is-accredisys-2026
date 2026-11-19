import app as pkg

application = pkg.create_app() if hasattr(pkg, "create_app") else pkg.app
