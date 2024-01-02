# Changelog

## 0.1.1
- Set the `_ll_lazily_loaded` module attribute to `True` if the module has been loaded lazily. This allows users to check if a module was loaded lazily, which can be useful for enforcing certain modules from *only* being imported through the lazy loader.

## 0.1.0
- Initial version
