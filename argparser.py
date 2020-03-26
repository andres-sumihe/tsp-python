import argparse

parser = argparse.ArgumentParser(
      description = "Program TSP dengan algoritma sederhana ")

parser.add_argument (
      "-n"
    , "--terdekat"
    , action  = "store_true"
    , dest    = "terdekat"
    , default = False
    , help    = "menghitung jarak perjalanan terdekat"
    )

parser.add_argument (
      "-f"
    , "--terjauh"
    , action  = "store_true"
    , dest    = "terjauh"
    , default = False
    , help    = "menghitung jarak perjalanan terjauh"
    )

parser.add_argument (
      "-i"
    , "--terurut"
    , action  = "store_true"
    , dest    = "terurut"
    , default = False
    , help    = "menghitung jarak yang ditempuh sesuai urutan [1..n,1]"
    )

parser.add_argument (
      "-p"
    , "--print-tours"
    , action  = "store_true"
    , dest    = "need_tours_printed"
    , default = False
    , help    = "print tour"
    )

parser.add_argument (
      "tsp_queue"
    , nargs   = "+"
    , metavar = "PATH"
    , help    = "Path menuju ke file tsp, jika path adalah sebuah direktori, maka"
                "ssemua file tsp di direktori tersebut akan di jalankan"
    )
