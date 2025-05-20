
from task_manager import TaskManager
from storage import load_tasks, save_tasks


def main():
    task_manager = TaskManager()
    task_manager.tasks = load_tasks()

    while True:
        print("\n=== TaskMate - Aplikasi Pengingat Tugas Kuliah ===")
        print("1. Tambah Tugas")
        print("2. Lihat Daftar Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        
        pilihan = input("Pilih menu (1-4): ")

        if pilihan == '1':
            judul = input("Masukkan judul tugas: ")
            matkul = input("Masukkan nama mata kuliah: ")
            deadline = input("Masukkan deadline (YYYY-MM-DD): ")
            task_manager.tambah_tugas(judul, matkul, deadline)
            save_tasks(task_manager.tasks)
        elif pilihan == '2':
            task_manager.lihat_tugas()
        elif pilihan == '3':
            task_manager.lihat_tugas()
            indeks = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
            task_manager.hapus_tugas(indeks)
            save_tasks(task_manager.tasks)
        elif pilihan == '4':
            print("Terima kasih telah menggunakan TaskMate!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")


if __name__ == "__main__":
    main()
