from ipywidgets import interactive_output, widgets, HBox, VBox, Layout

def create_widgets( run ):
    style = {'description_width': 'initial'}

    intMin = widgets.FloatText(value=0, min=0, max=1e5, 
                               continuous_update=False, 
                               description='Minimo:', 
                               style=style)
    intMax = widgets.FloatText(value=0, min=0, max=1e5, 
                               continuous_update=False, 
                               description='Massimo:',
                               style=style)
                   
    name  = widgets.Select(options=['LNGS senza schermatura','LNGS con schermatura di Pb'],
                           value='LNGS senza schermatura',
                           description='Spettri:',
                           disabled=False)
    scale = widgets.Select(options=['Lineare','Logaritmica'],
                           value='Lineare',
                           description='Scala:',
                           disabled=False)

    layout    = Layout(border='2px solid grey',width='1050px',height='',flex_flow='row',display='flex',justify_content='center')

    right_box  = VBox([scale, intMax])
    left_box   = VBox([name, intMin])
    ui         = HBox([left_box, right_box], layout=layout)
   
    w  = interactive_output(run,
                            { 
                                "intMin"   : intMin,
                                "intMax"   : intMax,
                                "name"     : name,
                                "scale"    : scale
                            }
                           )

    return ui, w
