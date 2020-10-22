#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

struct mahasiswa {
	void (*printmahasiswa)();
	char *nama;
	char *namaSekolah;
	char *alamatSekolah;

};

struct mahasiswa *mahasiswalist[10];
int count = 0; 

void print_mahasiswa_detail(struct mahasiswa *this){
	puts(this->nama);
	puts(this->namaSekolah);
	puts(this->alamatSekolah);
}
void apa_ya(){
	puts("bukan apa-apa");
}
void add_mahasiswa(){
	int i ;
	char buf[32];
	int size ;
	if(count > 10){
		puts("Penuh");
		return ;
	}
	for(i = 0 ; i < 10 ; ++i){
		if(!mahasiswalist[i]){
			mahasiswalist[i] = (struct mahasiswa*)malloc(sizeof(struct mahasiswa));
			if(!mahasiswalist[i]){
				puts("Terdapat Error");
				exit(-1);
			}
			mahasiswalist[i]->printmahasiswa = print_mahasiswa_detail;
			printf("ukuran data mahasiswa :");
			read(0,buf,32);
			size = atoi(buf);
			mahasiswalist[i]->nama = (char *)malloc(size);
			if(!mahasiswalist[i]->nama){
				puts("Terdapat Error");
				exit(-1);
			}
			printf("Nama ");
			read(0,mahasiswalist[i]->nama,size);
			mahasiswalist[i]->namaSekolah = (char *)malloc(size);
			if(!mahasiswalist[i]->namaSekolah){
				puts("Alloca Error");
				exit(-1);
			}
			printf("Nama sekolah ");
			read(0,mahasiswalist[i]->namaSekolah,size);
			mahasiswalist[i]->alamatSekolah = (char *)malloc(size);
			if(!mahasiswalist[i]->alamatSekolah){
				puts("Alloca Error");
				exit(-1);
			}
			printf("Alamat sekolah ");
			read(0,mahasiswalist[i]->alamatSekolah,size);
			puts("Berhasil ditambah!");
			count++;
			break;
		}
	}
}
void hello(){
	system("cat flag.txt");
}
void del_mahasiswa(){
	char buf[8];
	int idx ;
	printf("Indeks ke-");
	read(0,buf,8);
	idx = atoi(buf);
	if(idx < 0 || idx >= count){
		puts("Diluar batas!");
		_exit(0);
	}
	if(mahasiswalist[idx]){
		free(mahasiswalist[idx]->nama);
		free(mahasiswalist[idx]->namaSekolah);
		free(mahasiswalist[idx]->alamatSekolah);
		free(mahasiswalist[idx]);
		puts("Berhasil dihapus");
	}
}
void hartaKarun(){
	puts("harta karun itu mitos");
}
void print_mahasiswa(){
	char buf[4];
	int idx ;
	printf("Index ke-");
	read(0,buf,4);
	idx = atoi(buf);
	if(idx < 0 || idx >= count){
		puts("Diluar batas");
		_exit(0);
	}
	if(mahasiswalist[idx]){
		mahasiswalist[idx]->printmahasiswa(mahasiswalist[idx]);
	}
}

void menu(){
	puts("Selamat Datang Angkatan Corona			");
	puts(" 1. Tambah Mahasiswa Baru Angkatan Corona	");
	puts(" 2. Hapus Mahasiswa Baru Angkatan Corona  ");
	puts(" 3. Cetak Mahasiswa Baru Angkatan Corona  ");
	puts(" 4. Keluar				                ");
	printf("Pilihan ");
};
void inikah(){
    puts("cat flag.txt");
}
int main(){
	setvbuf(stdout,0,2,0);
	setvbuf(stdin,0,2,0);
	char buf[8];
	while(1){
		menu();
		read(0,buf,8);
		switch(atoi(buf)){
			case 1 :
				add_mahasiswa();
				break ;
			case 2 :
				del_mahasiswa();
				break ;
			case 3 :
				print_mahasiswa();
				break ;
			case 4 :
				exit(0);
				break ;
			default :
				puts("Pilihan diluar ketentuan");
				break ;

		}
	}
	return 0;
}
