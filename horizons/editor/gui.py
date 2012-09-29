# ###################################################
# Copyright (C) 2012 The Unknown Horizons Team
# team@unknown-horizons.org
# This file is part of Unknown Horizons.
#
# Unknown Horizons is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the
# Free Software Foundation, Inc.,
# 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
# ###################################################

from horizons.gui.tabs import TabWidget
from horizons.gui.tabs.tabinterface import TabInterface
from horizons.util.python.callback import Callback


class SettingsTab(TabInterface):
	widget = 'editor_settings.xml'

	def __init__(self, world_editor):
		super(SettingsTab, self).__init__(widget=self.widget)

		self._world_editor = world_editor

		for i in range(1, 4):
			b = self.widget.findChild(name='size_%d' % i)
			b.capture(Callback(self._change_brush_size, i))

		# Activate radio button for default brush size
		self._change_brush_size(self._world_editor.brush_size)

	def _change_brush_size(self, size):
		"""Change the brush size and update the gui."""
		images = {
		  'box_highlighted': 'content/gui/icons/ship/smallbutton_a.png',
		  'box': 'content/gui/icons/ship/smallbutton.png',
		}

		b = self.widget.findChild(name='size_%d' % self._world_editor.brush_size)
		b.up_image = images['box']

		self._world_editor.brush_size = size
		b = self.widget.findChild(name='size_%d' % self._world_editor.brush_size)
		b.up_image = images['box_highlighted']


class EditorGui(object):

	def __init__(self, world_editor, ingame_gui):
		self._world_editor = world_editor
		self._ingame_gui = ingame_gui

		self._ingame_gui.widgets['minimap'].mapEvents({'build': self._show_settings})

	def _show_settings(self):
		"""Display settings widget to change brush size and select tiles."""
		tab = TabWidget(self._ingame_gui, tabs=[SettingsTab(self._world_editor)])
		self._ingame_gui.show_menu(tab)
