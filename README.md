<h1 align="center">HTTP Client-Server Python Socket Programming</h1>

<p align="center">
  <img src="https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Socket%20Programming-003366?style=flat&logo=socket.io&logoColor=white"/>
  <img src="https://img.shields.io/badge/-HTTP%20Protocol-228B22?style=flat&logo=httpie&logoColor=white"/>
  <img src="https://img.shields.io/badge/-MultiThreading-6A1B9A?style=flat&logoColor=white"/>
  <img src="https://img.shields.io/badge/-Client--Server%20Architecture-FF7043?style=flat"/>
</p>

<div style="background-color:#E3F2FD;padding:15px;border-radius:10px;border-left:5px solid #2196F3;">
  <strong>📌 Deskripsi:</strong><br>
  Proyek ini merupakan implementasi client dan server HTTP sederhana menggunakan socket programming di Python. Aplikasi ini digunakan untuk mengirim request HTTP GET dan menerima response dari server layaknya sebuah browser, namun dijalankan melalui terminal.
</div>

<br>

Tugas besar mata kuliah Lab Jaringan Komputer
Dibentuk oleh:

- Fathan Arya Maulana / 103012300083
- Dzaky Alfaris / 103012300391
- M. Rifqi Dzaky Azhad / 103012330009

<div style="background-color:#FFF3E0;padding:15px;border-radius:10px;border-left:5px solid #FF9800;">
  <strong>🚀 Fitur:</strong><br>
  <ul>
    <li><strong>Client:</strong>
      <ul>
        <li>Mengirim permintaan HTTP GET ke server.</li>
        <li>Menerima dan menampilkan respon dari server.</li>
        <li>Mengakhiri koneksi dengan mengetik <code>exit</code>.</li>
      </ul>
    </li>
    <li><strong>Server:</strong>
      <ul>
        <li>Membaca permintaan HTTP dari client.</li>
        <li>Menyediakan konten file jika tersedia.</li>
        <li>Merespon dengan HTTP 404 jika file tidak ditemukan.</li>
        <li>Versi multi-threaded untuk melayani banyak klien secara simultan.</li>
      </ul>
    </li>
  </ul>
</div>

<br>

<div style="background-color:#E8F5E9;padding:15px;border-radius:10px;border-left:5px solid #4CAF50;">
  <strong>🛠️ Cara Menjalankan:</strong><br><br>
  <strong>1. Menjalankan Server</strong><br>

<em>a. Single-threaded Server:</em><br>

  <pre><code>python server_single_thread.py</code></pre>

<em>b. Multi-threaded Server:</em><br>

  <pre><code>python server_multithread.py</code></pre>

<strong>2. Menjalankan Client</strong><br>

  <pre><code>python client.py &lt;server_host&gt; &lt;server_port&gt;</code></pre>

<em>Contoh:</em>

  <pre><code>python client.py 127.0.0.1 4321</code></pre>

Setelah terhubung, masukkan nama file yang ingin diminta dari server. Misalnya: <code>index.html</code>.<br>
Ketik <code>exit</code> untuk mengakhiri koneksi.

</div>

<br>

<div style="background-color:#F3E5F5;padding:15px;border-radius:10px;border-left:5px solid #9C27B0;">
  <strong>📁 Struktur File:</strong>
  <ul>
    <li><code>client.py</code>: Program client untuk mengirim request HTTP GET.</li>
    <li><code>server_single_thread.py</code>: Server HTTP sederhana, menangani satu koneksi pada satu waktu.</li>
    <li><code>server_multithread.py</code>: Server HTTP multi-threaded, dapat melayani banyak koneksi secara bersamaan.</li>
    <li>File HTML sebagai contoh.</li>
  </ul>
</div>

<br>

<div style="background-color:#FFEBEE;padding:15px;border-radius:10px;border-left:5px solid #F44336;">
  <strong>📝 Catatan:</strong>
  <ul>
    <li>Semua komunikasi menggunakan protokol TCP.</li>
    <li>Hanya metode HTTP GET yang didukung.</li>
    <li>File yang diminta harus berada di folder yang sama dengan server.</li>
  </ul>
</div>

<br>

<div style="background-color:#ECEFF1;padding:15px;border-radius:10px;border-left:5px solid #607D8B;">
  <strong>📤 Contoh Output:</strong>

  <pre><code>
Isi nama file (atau 'exit'): index.html
HTTP/1.1 200 OK

&lt;html&gt;
  &lt;body&gt;
    Hello, world!
  &lt;/body&gt;
&lt;/html&gt;
  </code></pre>
</div>

<br>
