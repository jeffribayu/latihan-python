
import os
import datetime

class Node:
    def __init__(self, name, motor, keluhan, jenis_servis, phone):
        self.name = name
        self.motor=motor
        self.keluhan = keluhan
        self.jenis_servis = jenis_servis
        self.phone = phone
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add_customer(self, name, motor,keluhan, jenis_servis, phone):
        new_customer = Node(name, motor,keluhan, jenis_servis, phone)

        if self.head is None:
            self.head = new_customer
            
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_customer
            new_customer.prev = current

    def search_customer(self, name):
        current = self.head
        while current:
            if current.name == name:
                return current
            current = current.next
        return None

    def remove_customer(self, name):
        customer = self.search_customer(name)
        if customer:
            if customer.prev:
                customer.prev.next = customer.next
            else:
                self.head = customer.next

            if customer.next:
                customer.next.prev = customer.prev

    def tampilkan_customers(self):
        current = self.head
        if current is None:
            print("Daftar pelanggan kosong.")
        else:
            print("Daftar pelanggan:")
            while current:
                print("Nama:", current.name)
                print("masukan jenis motor:",current.motor)
                print("keluhan motor :",current.keluhan)
                print("jenis servis:",current.jenis_servis)
                print("Nomor telepon:", current.phone)
                print("-----------------------")
                current = current.next


def menu():
    print("\n")
    x = datetime.datetime.now()
    print(x)
    print("========= JEFF MOTOR =========")
    print("1. Tambahkan pelanggan")
    print("2. Cari pelanggan")
    print("3. Hapus pelanggan")
    print("4. Tampilkan semua pelanggan")
    print("0. Keluar")
    print("=======================================")
    

def main():
    linked_list = DoublyLinkedList()
    while True:
        menu()
        choice = input("Pilih menu: ")
        if choice == '1':
            x = datetime.datetime.now()
            print(x)
            name = input("Masukkan nama pelanggan: ")
            motor= input("masuka jenis motor: ")
            keluhan=input("masukn keluhan: ")
            jenis_servis=input("masukan jenis servis: ")
            phone = input("Masukkan nomor telepon pelanggan: ")
            linked_list.add_customer(name, motor, keluhan, jenis_servis, phone)
            print("Pelanggan ditambahkan.")
            
        elif choice == '2':
            x = datetime.datetime.now()
            print(x)
            name = input("Masukkan nama pelanggan yang ingin dicari: ")
            customer = linked_list.search_customer(name)
            if customer:
                print("Nama:", customer.name)
                print("keluhan motor :",customer.keluhan)
                print("jenis servis:",customer.jenis_servis)
                print("Nomor telepon:", customer.phone)
            else:
                print("Pelanggan tidak ditemukan.")

        elif choice == '3':
            os.system("cls")
            name = input("Masukkan nama pelanggan yang akan dihapus: ")
            linked_list.remove_customer(name)
            print("Pelanggan dihapus.")

        elif choice == '4':
            x = datetime.datetime.now()
            print(x)
            linked_list.tampilkan_customers()
        elif choice == '0':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == '__main__':
    main()
