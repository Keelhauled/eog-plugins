from gi.repository import GObject, Eog
import eogtricks_pager

class FitToScreen(GObject.Object, Eog.WindowActivatable):
	# Override EogWindowActivatable's window property
	# This is the EogWindow this plugin instance has been activated for
	window = GObject.property(type=Eog.Window)
	sizeprepid = 0

	def __init__(self):
		GObject.Object.__init__(self)

	def do_activate(self):
		thumbview = self.window.get_thumb_view()
		self.selection_changed_handler_id = thumbview.connect_after('selection-changed', self.thumb_selection_changed)

	def do_deactivate(self):
		pass

	def thumb_selection_changed(self, thumbview=None):
		if thumbview.get_n_selected() > 0:
			image = thumbview.get_first_selected_image()
			self.sizeprepid = image.connect('size-prepared', self.image_size_prepared)
			
	def image_size_prepared(self, image, width, height):
		image.disconnect_by_func(self.image_size_prepared)
		print(f'{image.get_file().get_path()} {width}x{height}')
		eogtricks_pager.PagerPlugin._set_fit_mode(eogtricks_pager.PagerPlugin, eogtricks_pager.PageFit.MIN)
