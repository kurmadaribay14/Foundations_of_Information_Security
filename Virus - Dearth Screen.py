import gtk
import pango
import cairo

cfg = {
       'foreground': '#FFFFFF',
       'background': '#0000AA',
       'font-desc' : 'fixedsysttf 14',
      }

class BSOD(Gtk.Window):
  def __init__(self):
    super(BSOD, self).__init__()

    self.connect('realize', self.realize_cb)
    self.connect('delete-event', Gtk.main_quit)
    self.fullscreen()

    ebox = Gtk.EventBox()
    ebox.modify_bg(Gtk.STATE_NORMAL, Gtk.gdk.color_parse(cfg['background']))
    self.add(ebox)

    label = Gtk.Label()
    label.modify_fg(Gtk.STATE_NORMAL, Gtk.gdk.color_parse(cfg['foreground']))
    label.modify_font(pango.FontDescription(cfg['font-desc']))
    label.set_justify(Gtk.JUSTIFY_CENTER)
    padding = 67
    lines = []
    lines.append(" WINDOWS ".center(padding)\
                 % (cfg['background'], cfg['foreground']))
    lines.append("")
    lines.append("A fatal exception 0E has occurred at 0020:c0011E3G in VXD VMM(01) +")
    lines.append("00010E3G. The current application will be terminated.")
    lines.append("")
    lines.append("*  Press any key to terminate the current application.")
    lines.append("*  Press CTRL+ALT+DEL again to restart your computer. You will")
    lines.append("   lose any unsaved information in all applications.")
    lines.append("")
    lines.append("Press any key to continue _".center(padding))

    label.set_markup("\n".join(map(lambda l: l.ljust(padding), lines)))
    ebox.add(label)

    self.show_all()

  def realize_cb(self, widget):
    pix_data = """/* XPM */
    static char * invisible_xpm[] = {
    "1 1 1 1",
    "       c None",
    " "};"""
    color = Gtk.gdk.Color()
    pix = Gtk.gdk.pixmap_create_from_data(self.window, pix_data, 1, 1, 1,
                                          color, color)
    invisible = Gtk.gdk.Cursor(pix, pix, color, color, 0, 0)

    self.window.set_cursor(invisible)


  def start(self):
    try:
      Gtk.main()
    except KeyboardInterrupt:
      pass


if __name__ == '__main__':
  BSOD().start()
