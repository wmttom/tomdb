import distutils.core

version = "0.1"

distutils.core.setup(
    name="tomdb",
    version=version,
    py_modules=["tomdb"],
    author="Tom",
    author_email="wmttom@gmail.com",
    url="https://github.com/wmttom/tomdb",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    description="A simple wrapper around MySQLdb.",
    )