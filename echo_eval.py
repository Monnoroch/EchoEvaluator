import sublime, sublime_plugin


res_var = "_echo_result"
base_str = "%s = []\ndef echo(s):\n\tglobal %s\n\t%s.append(str(s))\n" % (res_var, res_var, res_var)

class EchoEvalCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for s in self.view.sel():
			exec(base_str + self.view.substr(s))
			res = "".join(eval(res_var))
			if res != "":
				self.view.replace(edit, s, res)
