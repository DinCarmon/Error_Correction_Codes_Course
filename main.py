import Visual

def main():
    vis_inst = Visual.Visual()
    delta_arr, graph_arr = vis_inst.calculate_delta_to_rate_plot()
    vis_inst.print_elaborate(delta_arr, graph_arr)

if __name__ == "__main__":
    main()
