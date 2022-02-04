import PySimpleGUI as sg
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
import Visual
import Compute
import webbrowser
import Config

global list_of_shown_bounds
list_of_shown_bounds = []

bound_formal_name_to_func_name = {
    "Hamming Bound": "generalized_hamming_bound",
    "Gilbert Vershamov Bound": "gilbert_vershamov_bound",
    "Singleton Bound": "singleton_bound",
    "Plotkin Bound": "plotkin_bound",
    "Elias-Bassalygo Bound": "elias_bassalygo_bound",
}


def is_already_shown(bound_ins):
    for bound in list_of_shown_bounds:
        if bound[0] == bound_ins[0] and bound[1] == bound_ins[1]:
            return True
    return False


def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.get_tk_widget().forget()
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

def delete_figure_agg(figure_agg):
    figure_agg.get_tk_widget().forget()

global figure_agg
figure_agg = None


def gui_build():
    fig = Visual.vis_inst.fig_empty()

    matplotlib.use("TkAgg")

    description_openning_text = "Welcome to the the visualiser. Enjoy!"
    description_closing_text = "All rights reserved to Din Carmon but of course you can " \
                               "change and imporve the code:"


    graph_adder_layout = [[sg.Text('Bound Type:'),
                           sg.Combo(["Hamming Bound",
                                     "Gilbert Vershamov Bound",
                                     "Singleton Bound",
                                     "Plotkin Bound",
                                     "Elias-Bassalygo Bound"],
                                    default_value='',
                                    key='bound_type_req'),
                           sg.Text('q = '),
                           sg.InputText(key="q_req", size=(8, 2))],
                          [sg.Button("Add", button_color='Green')]]
    layout = [[sg.Text(description_openning_text)],
              [sg.Canvas(key="-CANVAS-")],
              [sg.Column(graph_adder_layout, element_justification='center', expand_x=True)],
              # for debugging
              # [sg.Text("list of bounds shown:")],
              # [sg.Text("", key="list_of_bounds_shown")],
              [sg.Button("Reset", button_color='Red')],
              [sg.Button("Exit")],
              [sg.Text(description_closing_text)],
              [sg.Text(Config.link_to_git,
                       enable_events=True,
                       text_color='Blue',
                       tooltip=Config.link_to_git)]]

    # Create the window
    window = sg.Window("Error Correcting Codes Bounds Visualizer",
                       layout,
                       margins=(100, 100),
                       location=(0, 0),
                       finalize=True,
                       element_justification="center",
                       font="Helvetica 18")

    # Add the plot to the window
    global figure_agg
    figure_agg = draw_figure(window["-CANVAS-"].TKCanvas, fig)
    return window


def gui_run(window):
    global figure_agg
    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "Add":
            # optional: reset to input boxes to blank
            # window["q_req"].update("")
            # window["bound_type_req"].update("")

            q_req = values['q_req']
            bound_type_req = values['bound_type_req']
            # check input is valid
            try:
                q_req = int(q_req)
                if q_req < 2:
                    continue
                if bound_type_req == '':
                    continue
            except ValueError:
                continue

            global list_of_shown_bounds
            # check bound is not already checked
            if not is_already_shown((bound_formal_name_to_func_name[bound_type_req], q_req)):
                new_bound = Compute.create_bound(bound_formal_name_to_func_name[bound_type_req], q_req)
                list_of_shown_bounds.append(new_bound)
                fig = Visual.vis_inst.update_fig(new_bound[2],
                                                 new_bound[3],
                                                 new_bound[4])
                delete_figure_agg(figure_agg)
                figure_agg = draw_figure(window["-CANVAS-"].TKCanvas, fig)
                # for debugging
                """
                last_list = window['list_of_bounds_shown'].get()
                window["list_of_bounds_shown"].update(last_list +
                                                      bound_type_req +
                                                      ", q = " +
                                                      str(q_req) +
                                                      "\n")"""
        if event == "Reset":
            window["q_req"].update("")
            window["bound_type_req"].update("")
            delete_figure_agg(figure_agg)
            fig = Visual.vis_inst.fig_empty()
            figure_agg = draw_figure(window["-CANVAS-"].TKCanvas, fig)
            list_of_shown_bounds = []
            # for debugging
            """window["list_of_bounds_shown"].update("")"""
        if event == Config.link_to_git:
            webbrowser.open(Config.link_to_git)
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()


def gui():
    window = gui_build()
    gui_run(window)
