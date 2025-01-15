from importlib.metadata import Distribution, PackageNotFoundError

try:
    __VERSION__ = Distribution.from_name('pbcore').version
except PackageNotFoundError:
    __VERSION__ = 'unknown'
