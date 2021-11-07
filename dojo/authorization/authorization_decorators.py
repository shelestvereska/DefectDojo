import functools
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from dojo.authorization.authorization import user_has_global_permission_or_403, user_has_permission_or_403, user_has_configuration_permission


def user_is_authorized(model, permission, arg, lookup="pk", func=None):
    """Decorator for functions that ensures the user has permission on an object.
    """

    if func is None:
        return functools.partial(user_is_authorized, model, permission, arg, lookup)

    @functools.wraps(func)
    def _wrapped(request, *args, **kwargs):
        # Fetch object from database
        if isinstance(arg, int):
            # Lookup value came as a positional argument
            args = list(args)
            lookup_value = args[arg]
        else:
            # Lookup value was passed as keyword argument
            lookup_value = kwargs.get(arg)

        # object must exist
        obj = get_object_or_404(model.objects.filter(**{lookup: lookup_value}))

        user_has_permission_or_403(request.user, obj, permission)

        return func(request, *args, **kwargs)

    return _wrapped


def user_has_global_permission(permission, func=None):
    """Decorator for functions that ensures the user has a (global) permission
    """

    if func is None:
        return functools.partial(user_has_global_permission, permission)

    @functools.wraps(func)
    def _wrapped(request, *args, **kwargs):
        user_has_global_permission_or_403(request.user, permission)
        return func(request, *args, **kwargs)

    return _wrapped


def user_is_authorized_for_configuration(permission, legacy):
    """
    Decorator for views that checks whether a user has a particular permission enabled.
    """
    def check_permission(user):
        if user_has_configuration_permission(user, permission, legacy):
            return True
        else:
            raise PermissionDenied

    return user_passes_test(check_permission)
