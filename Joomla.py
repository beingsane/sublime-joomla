import sublime, sublime_plugin

try:
  from .joomla.commands.components.create_component import CreateComponentCommand
except (ImportError, ValueError):
  from joomla.commands.components.create_component import CreateComponentCommand
