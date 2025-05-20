

class TaskManager:
    def __init__(self):
        self.tasks = []

    def tambah_tugas(self, judul, matkul, deadline):
        tugas = {
            "judul": judul,
            "matkul": matkul,
            "deadline": deadline
        }
        self.tasks.append(tugas)
        print("Tugas berhasil ditambahkan!")

    def lihat_tugas(self):
        if not self.tasks:
            print("Belum ada tugas.")
            return
        print("\nDaftar Tugas:")
        for idx, tugas in enumerate(self.tasks, start=1):
            print(f"{idx}. {tugas['judul']} - {tugas['matkul']} (Deadline: {tugas['deadline']})")

    def hapus_tugas(self, indeks):
        if 0 <= indeks < len(self.tasks):
            removed = self.tasks.pop(indeks)
            print(f"Tugas '{removed['judul']}' berhasil dihapus.")
        else:
            print("Nomor tugas tidak valid.")
