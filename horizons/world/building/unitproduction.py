# ###################################################
# Copyright (C) 2008-2016 The Unknown Horizons Team
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


from building import BasicBuilding
from buildable import BuildableSingle, BuildableSingleOnOcean
from horizons.world.building.buildingresourcehandler import BuildingResourceHandler
from horizons.component.storagecomponent import StorageComponent

class Barracks(BuildingResourceHandler, BuildableSingle, BasicBuilding):

	def __init__(self, **kwargs):
		super(Barracks, self).__init__(**kwargs)

	def initialize(self, **kwargs):
		super(Barracks, self).initialize(**kwargs)
		self.get_component(StorageComponent).inventory.limit = 5

class BoatBuilder(BuildingResourceHandler, BuildableSingleOnOcean, BasicBuilding):

	def __init__(self, **kwargs):
		super(BoatBuilder, self).__init__(**kwargs)

	def initialize(self, **kwargs):
		super(BoatBuilder, self).initialize(**kwargs)
		self.get_component(StorageComponent).inventory.limit = 10