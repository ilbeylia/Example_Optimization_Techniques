# Gezgin Satıcı Problemi (TSP):

# Bir satıcı, belirli bir sayıda şehiri ziyaret etmek istiyor. Her şehir arasındaki mesafeler biliniyor. 
# Satıcının amacı, her şehri tam olarak bir kez ziyaret edip, başlangıç noktasına dönerek toplam seyahat mesafesini minimize etmektir.

# Şehirler ve aralarındaki mesafeler:

# Şehirler: A, B, C, D
# Mesafeler:
# - A'dan B'ye: 2 birim
# - A'dan C'ye: 3 birim
# - A'dan D'ye: 1 birim
# - B'den A'ya: 2 birim
# - B'den C'ye: 4 birim
# - B'den D'ye: 2 birim
# - C'den A'ya: 3 birim
# - C'den B'ye: 4 birim
# - C'den D'ye: 3 birim
# - D'den A'ya: 1 birim
# - D'den B'ye: 2 birim
# - D'den C'ye: 3 birim

# Satıcının bu şehirleri ziyaret sırasını optimize etmeye çalışıyorum



# Karınca kolonisi optimizyonu
import numpy as np
import Function


distances = np.array([
    [0, 2, 3, 1],
    [2, 0, 4, 2],
    [3, 4, 0, 3],
    [1, 2, 3, 0]
])

best_route = Function.ant_colony(distances, n_ants=4, n_best=2, decay=0.95, alpha=1, beta=2, n_iterations=100)
print("En iyi yol:", best_route)



