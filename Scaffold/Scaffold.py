import sublime, sublime_plugin

class ScaffoldCommand(sublime_plugin.WindowCommand):
  def run(self):
    settings = sublime.load_settings("Scaffold.sublime-settings")
    self.scaffolds = settings.get("scaffolds")

    if self.scaffolds is None:
      sublime.status_message("No Scaffolds defined!")
      return
    self.window.show_quick_panel()
