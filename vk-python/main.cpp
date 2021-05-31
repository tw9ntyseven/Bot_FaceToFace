#include <iostream>

int main(int argc, const char * argv[]) {
    // insert code here...
    // std::cout << system("python3 ./python/main.py");
    char command[10000] = "python3 python/sys.py asdasdasdas cfgvhjbkgvyhb";
    char something = system(command);

    std::cout << something;
    return 0;
}
