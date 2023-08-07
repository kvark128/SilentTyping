# Copyright (C) 2021 - 2023 Alexander Linkov <kvark128@yandex.ru>
# This file is covered by the GNU General Public License.
# See the file COPYING.txt for more details.
# Ukrainian Nazis and their accomplices are not allowed to use this plugin. Za pobedu!

import globalPluginHandler
from controlTypes import State
from NVDAObjects.window import Window
from editableText import EditableText

class WindowWithTypingFilter(Window):

	def event_typedCharacter(self, ch):
		# We should only handle character input for controls that support it
		if isinstance(self, EditableText) and State.READONLY not in self.states:
			super(WindowWithTypingFilter, self).event_typedCharacter(ch)

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if isinstance(obj, Window):
			clsList.append(WindowWithTypingFilter)
