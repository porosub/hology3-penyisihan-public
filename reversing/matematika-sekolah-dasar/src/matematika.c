#include <stdlib.h>
#include <stdio.h>
#include <time.h>
		
int ii[26] = {106, 111, 105, 110, 117, 98, 98, 101, 116, 104, 101, 98, 101, 115, 116, 115, 101, 108, 97, 108, 117, 100, 104, 97, 116, 105};
int jj[26] = {2, 0, 5, 1, 18, 27, 81, 30, 25, 92, 17, 7, 40, 18, 0, 66, 14, 13, 21, 30, 20, 8, 92, 80, 64, 20};
int iii[16] = {106, 111, 105, 110, 117, 98, 98, 101, 116, 104, 101, 98, 101, 115, 116, 50};
int jjj[16] = {41, 32, 63, 39, 49, 83, 91, 35, 38, 45, 32, 46, 32, 50, 38, 124};

void status(){
    printf("berhasil");
}

int jumlah(int num1,int num2){
	return num1+num2;}
int kurang(int num1,int num2){
	return num1-num2;}
int kali(int num1,int num2){
	return num1*num2;}
float bagi(float num1,float num2){
	return num1/num2;}
	
int main(){
	unsigned short pilihan;
	int jawaban;
	srand(time(0));
	int hasil;
	char redeem[26];
	int cntredeem;
	int num1=rand()%(100+1-1)+1;
	int num2=rand()%(100+1-1)+1;
	printf("Kumpulan Soal Latihan Matematika\n");
	printf("1. Penjumlahan\n");
	printf("2. Pengurangan\n");
	printf("3. Perkalian\n");
	printf("4. Pembagian\n");
	printf("0. Keluar\n");
	printf("Pilih salah satu menu\n");
	scanf("%d",&pilihan);
	switch(pilihan){
		case 1:
		printf("Anda memilih penjumlahan\n");
		hasil=jumlah(num1,num2);
		printf("%d + %d = ",num1,num2);
		scanf("%d",&jawaban);
		if(jawaban==hasil){
			printf("jawaban benar");
		}else{
			printf("jawaban salah");
		}
		break;
		case 2:
		printf("Anda memilih pengurangan\n");
		hasil=kurang(num1,num2);
		printf("%d - %d = ",num1,num2);
		scanf("%d",&jawaban);
		if(jawaban==hasil){
			printf("jawaban benar");
		}else{
			printf("jawaban salah");
		}
		break;
		case 3:
		if(pilihan == 3){
			printf("Latihan hanya bisa penjumlahan dan pengurangan\n");
			printf("Jika punya kode masukkan\n");
			scanf("%s",&redeem);
			for(int i = 0; i <= 15; i++){
				if((iii[i]^redeem[i])==jjj[i]){
					++cntredeem;
				}
			}
			if(cntredeem == 16){
				puts("berhasil");
				printf("Anda memilih perkalian\n");
				hasil=(double)kali(num1,num2);
				printf("%d * %d = ",num1,num2);
				scanf("%d",&jawaban);
				if(jawaban==hasil){
					printf("jawaban benar");
				}else{
					printf("jawaban salah");
				}
			}else{
				puts("salah");
			}
		}else{
			puts("Program akan keluar");
			exit(0);
		}
		break;
		case 4:
		if(pilihan == 4){
			printf("Latihan hanya bisa penjumlahan dan pengurangan\n");
			printf("Jika punya kode masukkan\n");
			scanf("%s",&redeem);
			for(int i = 0; i <= 25; i++){
				if((ii[i]^redeem[i])==jj[i]){
					++cntredeem;
				}
			}
			if(cntredeem == 26){
				puts("berhasil");
				printf("Anda memilih pembagian\n");
				hasil = bagi(num1,num2);
				printf("%d / %d = ",num1,num2);
				scanf("%d",&jawaban);
				if(jawaban==hasil){
					printf("jawaban benar");
				}else{
					printf("jawabansalah");
				}
			}else{
				puts("salah");
			}
		}else{
			puts("Program akan keluar");
			exit(0);
		}
		break;
		case 0:
		exit(0);
		break;
		default:
		printf("Pilihan diluar ketentuan\n");
		exit(0);
		}
}
	
	
	
