# Implementasi Teori Graf Menggunakan Python

Proyek ini adalah implementasi teori graf menggunakan Python dan library NetworkX. Program ini memungkinkan Anda untuk membuat graf, menambah node dan edge, menghitung jalur terpendek, memvisualisasikan graf, dan lainnya.

## Prasyarat
Sebelum menjalankan kode, pastikan Anda memiliki Python dan library berikut terinstal:

- **Python 3.6 atau lebih baru**
- Library Python berikut:
  - `networkx`
  - `matplotlib`

### Instalasi Library
Jalankan perintah berikut untuk menginstal library yang dibutuhkan:
```bash
pip install networkx matplotlib
```

## Cara Menjalankan Kode
1. **Clone atau Unduh Repository**
   Clone repository ini atau unduh file `graf.py` ke komputer Anda.

2. **Jalankan Kode**
   Gunakan terminal atau command prompt untuk menjalankan kode:
   ```bash
   python graf.py
   ```

3. **Ikuti Hasil yang Ditampilkan**
   Program akan menampilkan graf, jalur terpendek, dan informasi tambahan di terminal.

## Contoh Penggunaan
Berikut adalah contoh cara menggunakan kelas `Graf` yang telah dibuat:

### Membuat Graf dan Menambah Node serta Edge
```python
from graf import Graf

graph = Graf()

graph.add_node(1)
graph.add_node(2)
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)

graph.add_edge(1, 2, weight=4.5)
graph.add_edge(1, 3, weight=3.2)
graph.add_edge(2, 4, weight=2.7)
graph.add_edge(3, 4, weight=1.8)
graph.add_edge(1, 4, weight=6.7)
graph.add_edge(3, 5, weight=2.7)
```

### Visualisasi Graf
```python
graph.visualize_graph()
```

### Menghitung Jalur Terpendek
```python
path = graph.shortest_path(1, 5)
print("Jalur terpendek dari 1 ke 5:", path)
```

### Visualisasi Jalur Terpendek
```python
graph.visual_shortest_path(1, 5)
```

### Metode Tambahan
Program ini juga memiliki metode tambahan seperti:
- `is_connected()`
- `node_degree(node)`
- `get_all_paths(start, end)`
- `total_weight()`
- `clustering_coefficient(node=None)`

Berikut contoh penggunaannya:
```python
print("Apakah graf terhubung?", graph.is_connected())
print("Derajat node 3:", graph.node_degree(3))
print("Semua jalur dari 1 ke 5:", graph.get_all_paths(1, 5))
print("Total bobot graf:", graph.total_weight())
print("Koefisien klastering:", graph.clustering_coefficient())
```

## Catatan
- Jika Anda menemukan masalah, pastikan semua library terinstal dengan benar.
- File ini dapat diunggah ke platform seperti GitHub untuk memudahkan kolaborasi.

## Lisensi
Proyek ini dilisensikan di bawah lisensi MIT.
