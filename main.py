from argparser  import parser
from tsp   import baca_tsp_file
from proses import ( kalk_rute_terdekat_tour
                       , kalk_rute_terurut
                       , kalk_rute_terjauh_tour)


from glob    import iglob
from os.path import isfile, isdir, join, exists

def glean_tsp_files(path_arg_list):
    for path_arg in path_arg_list:

        if isdir(path_arg):
            for filepath in iglob(join(path_arg,"*.tsp")):
                yield filepath

        elif isfile(path_arg) & str(path_arg).endswith(".tsp"):
            yield path_arg

        elif isfile(path_arg) & (not path_arg.endswith(".tsp")):
            print("Tidak Bisa Membuka,``{0}'': Bukan .tsp file".format(path_arg))

        elif exists(path_arg):
            print("Path {0} Bukan File Maupun Dire".format(path_arg))

        else:
            print("Path {0} Tidak Ditemukan".format(path_arg))

def print_results_from_tsp_path(call_args, tsp_path):
    tsp = baca_tsp_file(tsp_path)
    print("TSP Problem:              {}".format(tsp["NAME"]))
    print("PATH:                     {}".format(tsp_path))

    if call_args.terurut:
        print("Panjang Rute Sesuai Urutan:     {}"
             . format(kalk_rute_terurut(tsp)))

    if call_args.terdekat:
        print("Rute Terdekat:  {}"
             . format(kalk_rute_terdekat_tour(tsp)))

    if call_args.terjauh:
        print("Rute Terjauh: {}"
             . format(kalk_rute_terjauh_tour(tsp)))

    print("")
    del(tsp)

def main():
    call_args = parser.parse_args()
    for tsp_path in glean_tsp_files(call_args.tsp_queue):
        print_results_from_tsp_path(call_args,tsp_path)

if __name__ == "__main__":
    main()
