# ensure that PyGTK 2.0 is loaded - not an older version
import pygtk
pygtk.require('2.0')
# import the GTK module
import gtk

class Entrada:

  def __init__( self, title):
    self.window = gtk.Window()
    self.title = title
    self.window.set_title( title)
    self.window.set_size_request( -1, -1)
    self.window.connect( "destroy", self.destroy)
    self.create_interior()
    self.window.show_all()

  def create_interior( self):
    self.mainbox = gtk.VBox()
    self.window.add( self.mainbox)
    # label
    self.label_template = "File: <b>%s</b>\nDir: <b>%s</b>\nSize: <b>%s</b>"
    self.label = gtk.Label( self.label_template % ("","",""))
    self.label.set_use_markup( True)
    self.mainbox.pack_start( self.label, padding=10)
    self.label.show()
    # button that triggers the FileChooserDialog
    b = gtk.Button( "Select file..")
    self.mainbox.pack_start( b, expand=False)
    b.show()
    b.connect( "clicked", self.open_file)
    # show the box
    self.mainbox.show()

  def main( self):
    gtk.main()

  def destroy( self, w):
    gtk.main_quit()

  def open_file( self, w, data=None):
    d = gtk.FileChooserDialog( title="Select a file",
                               parent=self.window,
                               action=gtk.FILE_CHOOSER_ACTION_OPEN,
                               buttons=("OK",True,"Cancel",False)
                               )
    ok = d.run()
    if ok:
      import os
      fullname = d.get_filename()
      dirname, fname = os.path.split( fullname)
      size = "%d bytes" % os.path.getsize( fullname)
      text = self.label_template % (fname, dirname, size)
    else:
      text = self.label_template % ("","","")
    self.label.set_label( text)
    # make the dialog disappear, don't do it before you get all data from it
    d.destroy() #@+


if __name__ == "__main__":
  m = MyGUI( "Open File")
  m.main()
