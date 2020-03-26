from collections import deque
from kota        import jarak,  Euc_2D
from tsp         import baca_tsp_file
from numpy       import array

def kalk_jarak(tsp, kota1, kota2):
    kota = tsp["CITIES"]
    return jarak(kota[kota1 - 1], kota[kota2 - 1])

def panjang_rute(tsp,path):
    if len(path) == 1:
        return 0
    else:
        start_node = path.pop()
        next_node  = path[-1]
        return kalk_jarak(tsp,start_node,next_node) + panjang_rute(tsp,path)

def tour_dari_rute(path):
    path.append(path[0])
    return path

def rute_terurut(tsp):
    dim = tsp["DIMENSION"]
    return list(range(1,dim+1))

def tour_terurut(tsp):
    return tour_dari_rute(rute_terurut(tsp))

def kalk_rute_terurut(tsp):
    return panjang_rute(tsp,tour_terurut(tsp))

def rute_terdekat(tsp,belum_dikunjungi,kota_sekarang):
    jarak_ke_kota = lambda city: kalk_jarak(tsp,kota_sekarang,city)
    return min(belum_dikunjungi, key = jarak_ke_kota)

def rute_terjauh(tsp,belum_dikunjungi,kota_sekarang):
    jarak_ke_kota = lambda city: kalk_jarak(tsp,kota_sekarang,city)
    return max(belum_dikunjungi, key = jarak_ke_kota)

def rute_terdekat_tour(tsp):
    rute_terdekat_path = [1]
    kota_sekarang          = 1
    kota_yang_akan_dikunjungi      = set(range(2, tsp["DIMENSION"] + 1))

    while kota_yang_akan_dikunjungi:
        kota_sekarang = rute_terdekat(tsp,kota_yang_akan_dikunjungi,kota_sekarang)
        rute_terdekat_path.append(kota_sekarang)
        kota_yang_akan_dikunjungi.remove(kota_sekarang)

    return tour_dari_rute(rute_terdekat_path)

def rute_terjauh_tour(tsp):
    
    rute_terdekat_path = [1]
    kota_sekarang          = 1
    kota_yang_akan_dikunjungi      = set(range(2, tsp["DIMENSION"] + 1))

    while kota_yang_akan_dikunjungi:
        kota_sekarang = rute_terjauh(tsp,kota_yang_akan_dikunjungi,kota_sekarang)
        rute_terdekat_path.append(kota_sekarang)
        kota_yang_akan_dikunjungi.remove(kota_sekarang)

    return tour_dari_rute(rute_terdekat_path)

def kalk_rute_terdekat_tour(tsp):
    return panjang_rute(tsp,rute_terdekat_tour(tsp))

def kalk_rute_terjauh_tour(tsp):
    return panjang_rute(tsp,rute_terjauh_tour(tsp))
