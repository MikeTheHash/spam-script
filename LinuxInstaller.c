#include <stdio.h>
#include <string.h>

int main(){
	printf("Do you want to install python? [Y/N] > ");
	char input[1];
	scanf("%s", input);
	if(strcmp(input, "Y") == 0 || strcmp(input, "y") == 0){
		printf("Installing Python3...");
		system("sudo apt-get install python3");
		system("sudo apt install python3-pip");
	}
	else{
		printf("Python: Skipped\n");
	}
	printf("Installing the libraries used in the script...\n");
	system("pip install pyautogui");
	system("pip install kivy");
	printf("Libraries installed successfully!\n");
	return 0;
}
