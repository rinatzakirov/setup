#! /usr/bin/python3

# tiling.py
# Simple tiling for GTK
import time
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
gi.require_version("Gdk", "3.0")
from gi.repository import Gdk
gi.require_version("GdkX11", "3.0")                                                                                               
from gi.repository import GdkX11

DECOR_HEIGHT = 43

def run():
	while True:
		root = Gdk.get_default_root_window()
		win = root.get_screen().get_active_window()
		geom = root.get_screen().get_display().get_monitor(0).get_geometry()
		screen_width = geom.width
		screen_height = geom.height

		origin = win.get_root_origin()
		#print "orig: %d %d" % (origin[0], origin[1])
		geom = list(win.get_geometry())
		geom[0] += origin[0]
		geom[1] += origin[1]
		#print("%s" % str(geom))
			
		cursor = root.get_pointer()
		#print("%s" % str(cursor))
		is_btn = int(cursor.mask & Gdk.ModifierType.BUTTON1_MASK) != 0
		decor = win.get_decorations()
		is_decorated = (not decor[0]) or (decor[0] and int(decor.decorations) != 0)
		#print("decorated: %s" % str(is_decorated))
		moving = is_btn and cursor.y < geom[1] + (0 if is_decorated else DECOR_HEIGHT)
		#print(moving)
		
		if moving:
			if cursor.y == screen_height - 1:
				snap_coord = screen_width - 1 - 1706
				height = 1359
				width = 0
				if not is_decorated:
					height += DECOR_HEIGHT
				width = 1706
				snap_coord -= width
				if snap_coord < 0: snap_coord = 0
				win.move_resize(snap_coord, 0, width, height)
				win.geometry_changed()
			if cursor.x == screen_width - 1 or cursor.x == 0:
				snap_coord = screen_width - 1
				if cursor.x == 0:
					snap_coord = 0
				height = 1359
				width = 0
				if not is_decorated:
					height += DECOR_HEIGHT
				if cursor.y < 100:
					width = 2416
				elif cursor.y < 1000:
					width = 2560
				else:
					width = 1706
				snap_coord -= width
				if snap_coord < 0: snap_coord = 0
				win.move_resize(snap_coord, 0, width, height)
				win.geometry_changed()
		
		time.sleep(0.1)

while True:
	try:
		run()
	except:
		pass
	time.sleep(1.0)
