def includeme(config):
    config.add_route('index', '/')
    config.add_route('hello', '/hello')
    config.add_route('auth-login', '/login')
    config.add_route('auth-logout', '/logout')
    config.add_route('auth-register', '/register')
    config.add_route('blog-create', '/blog/create')
    config.add_route('blog-delete', '/blog/{id}/delete')
    config.add_route('blog-update', '/blog/{id}/update')
