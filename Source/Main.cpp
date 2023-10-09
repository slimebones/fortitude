#include <iostream>
#include "Saver.h"

int main()
{
    std::cout << "Fortitude" << std::endl << std::endl;
    std::cout << "Please enter a command" << std::endl;

    std::string cmd = "";
    Saver saver;

    while (true)
    {
        std::cin >> cmd;
        saver.Save(cmd);
        std::cout << "Written: " << cmd << std::endl;
    }

    return 0;
}
