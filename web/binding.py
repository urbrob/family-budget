import inject

def includeme() -> None:
    """
    Configure dependency injection for application
    """

    def configure_di(binder: inject.Binder) -> None:
        pass

    inject.clear_and_configure(configure_di)