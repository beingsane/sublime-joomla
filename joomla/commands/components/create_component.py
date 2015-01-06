import sublime
import sublime_plugin
import os

class CreateComponentCommand(sublime_plugin.WindowCommand):
  def get_config_path(self):
    try:
      project_file_path = self.window.project_file_name()
      return os.path.dirname(project_file_path)
    except AttributeError:
      return self.window.folders()[0]

      def run(self, *args, **kwargs):
        self.get_config_path()