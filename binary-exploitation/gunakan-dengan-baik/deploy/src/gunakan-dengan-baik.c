#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>

int main(){
    char nama[8];
    char buf[128]; 
    setvbuf(stdout,NULL,_IONBF,0);
	printf("kamu siapa?\n");
	gets(buf);
	if(memcmp(nama, "correct1",8) == 0){
	    printf("kamu mau flag?");
	    gets(nama);
	    if(strcmp(nama, "glf") == 0){
	        system("cat flag.txt");
	    }
	}else{
	    printf("jangan aneh aneh ya");
	    return 0;
	}
	return 0;
}

void jangankesini(){
	printf("ngapain kamu kesini, keluar!");
}

void kesini(){
	printf("yeay");
}

void kepo(){
	printf("hayo mau ngapain?");
}

