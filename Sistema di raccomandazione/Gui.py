import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

from DataFromInput import *
from DataFromWeb import *
from MkTable import *
from Recommended import *


class MyWin(Gtk.ApplicationWindow) :
    def __init__ (self, app) :
        Gtk.Window.__init__(self, title=app.table.title, application=app)
        self.set_default_size(500,500)
        self.set_border_width(5)
#qui sotto
        adj = Gtk.Adjustment(value = 0, lower = 1, upper = len(app.table.table), step_increment = 1, page_increment = 10, page_size = 0)
        self.scale = Gtk.Scale(orientation=Gtk.Orientation.HORIZONTAL, 
                adjustment=adj)

        self.scale.set_digits(0)
        self.scale.set_hexpand(True)
        self.scale.set_valign(Gtk.Align.START)
        self.scale.connect("value-changed", self.scaleMoved)

        self.label = Gtk.Label()
        
        l = "Head Concept: "+ app.table.h_conc+"\tModifier Concept: "+app.table.m_conc
        
        rec = recommended(app.table)
        if rec != [] :
            l += '\nRecommended scenarios N°:'
            for x in rec :
                self.scale.add_mark(x+1, Gtk.PositionType.TOP, None)  
                l += ' '+str(x+1)+' '
        else :  l += '\nNO recommended scenarios!'

        self.scaleMoved(None)
        
        self.label1 = Gtk.Label()
        
        
        self.label1.set_text(l)
        
        grid = Gtk.Grid()
        grid.set_column_spacing(10)
        grid.set_column_homogeneous(True)
        grid.set_row_spacing(15)

        grid.attach(self.label1, 0, 0, 2, 1)
        grid.attach(self.scale, 0, 1, 2, 1)
        grid.attach(self.label, 0, 2, 2, 1)

        self.add(grid)

#qui sotto
    def scaleMoved(self, event) :
        used_attrs = "  This concept instance is :\n"

        for x in range(len(app.table.tipical_attrs)) :
            if (app.table.sorted_table[int(self.scale.get_value())-1][x] == '1') :
                used_attrs += "    "
                used_attrs += (app.table.tipical_attrs[x][0])

                if (app.table.tipical_attrs[x][2]) :
                    used_attrs += (" (from "+app.table.h_conc+")\n")
                else:
                    used_attrs += (" (from "+app.table.m_conc+")\n")

        self.label.set_text("The scale is on percentage "+ 
                str(app.table.sorted_table[int(self.scale.get_value())-1][len(app.table.tipical_attrs)])+
                "%\n" + used_attrs)



class MyApp(Gtk.Application) :
    
    def __init__(self, table) :
        Gtk.Application.__init__(self)
        self.table = table


    def do_activate(self) :
        win = MyWin(self)
        win.show_all()

    def do_startup(self) :
        Gtk.Application.do_startup(self)



#dict_of_attr = DataFromWeb.DictOfAttr()
#tab = MkTable.Table(dict_of_attr.getSortedDict()[-10:])

if __name__ == '__main__' :

    if len(sys.argv) == 2 :
        input_data = ReadAttributes(sys.argv[1])
        del sys.argv[1]
    else :
        input_data = ReadAttributes()

    tab = Table(input_data)

    app = MyApp(tab)
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)


