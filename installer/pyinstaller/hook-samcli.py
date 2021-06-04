from PyInstaller.utils import hooks

# This is a PyInstaller hook file. A hook file defines additional
# source files or data files to/not to import.
# https://pyinstaller.readthedocs.io/en/stable/hooks.html

hiddenimports = [
    "cookiecutter.extensions",
    "jinja2_time",
    "text_unidecode",
    "samtranslator",
    "samcli.commands.init",
    "samcli.commands.validate.validate",
    "samcli.commands.build",
    "samcli.commands.local.local",
    "samcli.commands.package",
    "samcli.commands.deploy",
    "samcli.commands.logs",
    "samcli.commands.publish",
    # default hidden import 'pkg_resources.py2_warn' is added
    # since pyInstaller 4.0.
    "pkg_resources.py2_warn",
    "aws_lambda_builders.workflows",
    "configparser",
]
datas = (
    hooks.collect_data_files("samcli")
    + hooks.collect_data_files("samtranslator")
    + hooks.collect_data_files("aws_lambda_builders")
    + hooks.collect_data_files("text_unidecode")
)
